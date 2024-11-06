from rest_framework import viewsets
from ..models import DataMoverDataSource, DataMoverConfig
from ..filtersets import DataMoverConfigFilterSet, DataMoverDataSourceFilterSet 
from .serializers import DataMoverDataSourceSerializer, DataMoverConfigSerializer
from netbox.api.viewsets import NetBoxModelViewSet
from rest_framework.response import Response


class DataMoverDataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataMoverDataSource.objects.all()
    serializer_class = DataMoverDataSourceSerializer
   
    def list(self, request, *args, **kwargs):
        
        if request.query_params.get('endpoint_id'):
            try:
                datasource = self.queryset.get(request.query_params.get('endpoint_id'))
                endpoints = datasource.endpoints.split(',')
                return Response({'results': [{'id': idx, 'display': endpoint.strip()} for idx, endpoint in enumerate(endpoints)]})
            except DataMoverDataSource.DoesNotExist:
                return Response({'results': []})
        if request.query_params.get('fields_id'):
            try:
                datasource = self.queryset.get(request.query_params.get('fields_id'))
                return Response({'results': [{'id': 1, 'display': 'Test 123'}]})
            except DataMoverDataSource.DoesNotExist:
                return Response({'results': []})

        # Otherwise, return the full DataMoverDataSource records.
        return super().list(request, *args, **kwargs)
    
class DataMoverConfigViewSet(NetBoxModelViewSet):
    queryset = DataMoverConfig.objects.all()
    serializer_class = DataMoverConfigSerializer
    filterset = DataMoverConfigFilterSet