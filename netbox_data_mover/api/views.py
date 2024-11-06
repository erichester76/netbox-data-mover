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
    filterset = DataMoverDataSourceFilterSet
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        type_param = request.query_params.get('type', None)

        if type_param == 'endpoints':
            if instance.endpoints:
                # Fake Serializer
                endpoints = instance.endpoints.split(',')
                endpoint_data = []

                endpoint_data = [
                    {
                        "id": index,
                        "display": endpoint.strip(),
                        "name": endpoint.strip()
                    } for index, endpoint in enumerate(endpoints)
                ]

                # Response formatted in a similar way to the one provided in your example
                return Response({
                    "count": len(endpoint_data),
                    "next": None,
                    "previous": None,
                    "results": endpoint_data
                })

            return Response({"count": 0, "next": None, "previous": None, "results": []})

        # Default behavior: return the serialized datasource instance
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class DataMoverConfigViewSet(NetBoxModelViewSet):
    queryset = DataMoverConfig.objects.all()
    serializer_class = DataMoverConfigSerializer
    filterset = DataMoverConfigFilterSet