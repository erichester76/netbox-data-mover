from rest_framework import viewsets
from ..models import DataMoverDataSource, DataMoverConfig
from ..filtersets import DataMoverConfigFilterSet, DataMoverDataSourceFilterSet 
from .serializers import DataMoverDataSourceSerializer, DataMoverConfigSerializer
from netbox.api.viewsets import NetBoxModelViewSet
from django.http import JsonResponse
from ..api_utils import DataSourceAuth
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404


class DataMoverDataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataMoverDataSource.objects.all()
    serializer_class = DataMoverDataSourceSerializer
   
    def list(self, request, *args, **kwargs):
        # If 'datamoverdatasourceid' is passed as a query parameter, return only the endpoints.
        datamoverdatasourceid = request.query_params.get('datamoverdatasourceid')
        if datamoverdatasourceid:
            try:
                datasource = self.queryset.get(id=datamoverdatasourceid)
                endpoints = datasource.endpoints.split(',')
                return Response({'results': [{'id': idx, 'display': endpoint.strip()} for idx, endpoint in enumerate(endpoints)]})
            except DataMoverDataSource.DoesNotExist:
                return Response({'results': []})

        # Otherwise, return the full DataMoverDataSource records.
        return super().list(request, *args, **kwargs)
    
class DataMoverConfigViewSet(NetBoxModelViewSet):
    queryset = DataMoverConfig.objects.all()
    serializer_class = DataMoverConfigSerializer
    filterset = DataMoverConfigFilterSet