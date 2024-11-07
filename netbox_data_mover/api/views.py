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

    @action(detail=True, methods=['get'])
    def endpoints(self, request, pk=None):
        """Custom endpoint to get list of endpoints for a given DataMoverDataSource"""
        instance = self.get_object()
        if instance.endpoints:
            endpoints = instance.endpoints.split(',')
            endpoint_data = [
                {
                    "id": index,
                    "display": endpoint.strip(),
                    "name": endpoint.strip(),
                    "slug": endpoint.strip().replace(" ", "-").lower(),
                    "description": ""
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

    @action(detail=True, methods=['get'], url_path='endpoints/(?P<endpoint_name>[^/.]+)/fields')
    def fields(self, request, datasource_id=None, endpoint_name=None):
        """Custom action to get fields for a specific endpoint of a DataMoverDataSource"""
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


    class Meta:
        model = DataMoverDataSource
        fields = ['id', 'name', 'display', 'type', 'module', 'auth_method', 'auth_function', 'endpoints']
        brief_fields=['id', 'display', 'name']
    
class DataMoverConfigViewSet(NetBoxModelViewSet):
    queryset = DataMoverConfig.objects.all()
    serializer_class = DataMoverConfigSerializer
    filterset = DataMoverConfigFilterSet