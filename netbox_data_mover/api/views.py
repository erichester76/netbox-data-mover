from ..models import DataMoverDataSource, DataMoverConfig
from ..filtersets import DataMoverConfigFilterSet, DataMoverDataSourceFilterSet 
from .serializers import DataMoverDataSourceSerializer, DataMoverConfigSerializer
from netbox.api.viewsets import NetBoxModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action


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
            datasource_id = request.query_params.get('datasource_id', None)
            instance = self.get_queryset().get(id=datasource_id)
            try:
                field_data = [
                    {
                        "id": 1,
                        "display": 'Testing 123',
                        "name": 'Testing 123',
                    },
                    {
                        "id": 1,
                        "display": 'Testing 4321',
                        "name": 'Testing 4321',
                    },
                ]

                return Response({
                    "count": len(field_data),
                    "next": None,
                    "previous": None,
                    "results": field_data
                })

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