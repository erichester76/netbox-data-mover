from ..models import DataMoverDataSource, DataMoverConfig
from ..filtersets import DataMoverConfigFilterSet, DataMoverDataSourceFilterSet 
from .serializers import DataMoverDataSourceSerializer, DataMoverConfigSerializer
from netbox.api.viewsets import NetBoxModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from ..api_utils import DataSourceAuth


class DataMoverDataSourceViewSet(NetBoxModelViewSet):
    queryset = DataMoverDataSource.objects.all()
    serializer_class = DataMoverDataSourceSerializer
    filterset_class = DataMoverDataSourceFilterSet
    lookup_field = 'id'
    lookup_url_kwarg = 'datasource_id'

    # overload the list (no pkid) view so we can add arguments to get endpoints and fields as well 
    # using "nest" url param 
    def list(self, request, *args, **kwargs):
        
        if request.query_params.get('nest', 'none') == 'endpoints':
            """Custom endpoint to get list of endpoints for a given DataMoverDataSource"""
            datasource_id = request.query_params.get('datasource_id', None)
            instance = self.get_queryset().get(id=datasource_id)
            if instance.endpoints:
                endpoints = instance.endpoints.split(',')
                endpoint_data = [
                    {
                        "id": index,
                        "display": endpoint.strip(),
                        "name": endpoint.strip(),
                    }
                    for index, endpoint in enumerate(endpoints)
                ]
                return Response({
                    "count": len(endpoint_data),
                    "next": None,
                    "previous": None,
                    "results": endpoint_data
                })
            return Response({"count": 0, "next": None, "previous": None, "results": []})
        
        elif request.query_params.get('nest', 'none') == 'fields':
            instance = self.get_queryset().get(id=datasource_id)
            try:
                # Authenticate and get the client
                client = DataSourceAuth.authenticate(instance)

                if not client:
                    return Response({"detail": "Failed to authenticate with the data source."}, status=status.HTTP_400_BAD_REQUEST)
                
                # Fetch data from the specified endpoint
                if request.query_params.get('endpoint_id', None):
                    
                    endpoint_id = request.query_params.get('endpoint_id', None)
                    # Use the endpoint ID to get the correct endpoint value
                    endpoints = instance.endpoints.split(',')
                    if int(endpoint_id) < len(endpoints):
                        selected_endpoint = endpoints[int(endpoint_id)].strip()
                    else:
                        return Response({"detail": "Invalid endpoint ID."}, status=status.HTTP_400_BAD_REQUEST)

                    # Use fetch_data to fetch the data from the endpoint
                    data = DataSourceAuth.fetch_data(instance, client, selected_endpoint)
                    
                    # If the response is not in the expected format
                    if not data:
                        return Response({"detail": "No data found or failed to fetch data."}, status=status.HTTP_400_BAD_REQUEST)

                    # Step 3: Extract field names from the first record
                    if isinstance(data, list) and len(data) > 0:
                        first_record = data[0]
                    elif isinstance(data, dict):
                        first_record = data.get('results', [data])[0]
                    else:
                        return Response({"count": 0, "next": None, "previous": None, "results": []})

                    # Extract field names
                    fields = [{"id": index, "display": key, "name": key} for index, key in enumerate(first_record.keys())]

                    return Response({
                        "count": len(fields),
                        "next": None,
                        "previous": None,
                        "results": fields
                    })
                else:
                    return Response({"detail": "Endpoint ID is required."}, status=status.HTTP_400_BAD_REQUEST)

            except DataMoverDataSource.DoesNotExist:
                return Response(status=404)
            
        # Default to the standard retrieve behavior
        return super().list(request, *args, **kwargs)

    class Meta:
        model = DataMoverDataSource
        fields = ['id', 'name', 'display', 'type', 'module', 'auth_method', 'auth_function', 'endpoints']
        brief_fields=['id', 'display', 'name']
    
class DataMoverConfigViewSet(NetBoxModelViewSet):
    queryset = DataMoverConfig.objects.all()
    serializer_class = DataMoverConfigSerializer
    filterset = DataMoverConfigFilterSet