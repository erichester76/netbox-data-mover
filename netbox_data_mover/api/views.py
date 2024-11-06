from ..models import DataMoverDataSource, DataMoverConfig
from ..filtersets import DataMoverConfigFilterSet, DataMoverDataSourceFilterSet 
from .serializers import DataMoverDataSourceSerializer, DataMoverConfigSerializer
from netbox.api.viewsets import NetBoxModelViewSet
from rest_framework.response import Response


class DataMoverDataSourceViewSet(NetBoxModelViewSet):
    queryset = DataMoverDataSource.objects.all()
    serializer_class = DataMoverDataSourceSerializer
    filterset = DataMoverDataSourceFilterSet
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        type_param = request.query_params.get('type', None)
        if type_param == 'endpoints':
            if instance.endpoints:
                # Split endpoints and create a structured response
                endpoints = instance.endpoints.split(',')
                endpoint_data = []

                for index, endpoint in enumerate(endpoints):
                    endpoint_data.append({
                        "id": index,
                        "display": endpoint.strip(),
                        "name": endpoint.strip(),
                        "slug": endpoint.strip().replace(" ", "-").lower(),
                        "description": ""
                    })

                # Response formatted in a similar way to the one provided in your example
                return Response({
                    "count": len(endpoint_data),
                    "next": None,
                    "previous": None,
                    "results": endpoint_data
                })
            return Response({"count": 0, "next": None, "previous": None, "results": []})
    
        elif type_param == 'mapping_fields':
            return Response({"count": 0, "next": None, "previous": None, "results": []})
    
        # Default behavior: return the serialized datasource instance
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    
class DataMoverConfigViewSet(NetBoxModelViewSet):
    queryset = DataMoverConfig.objects.all()
    serializer_class = DataMoverConfigSerializer
    filterset = DataMoverConfigFilterSet