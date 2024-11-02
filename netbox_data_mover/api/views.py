from rest_framework import viewsets
from ..models import DataMoverDataSource, DataMoverConfig
from .serializers import DataMoverDataSourceSerializer, DataMoverConfigSerializer

class DataMoverDataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataMoverDataSource.objects.all()
    serializer_class = DataMoverDataSourceSerializer

class DataMoverConfigViewSet(viewsets.ModelViewSet):
    queryset = DataMoverConfig.objects.all()
    serializer_class = DataMoverConfigSerializer
