from rest_framework import viewsets
from ..models import DataSource, DataMoverConfig
from .serializers import DataSourceSerializer, DataMoverConfigSerializer

class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer

class DataMoverConfigViewSet(viewsets.ModelViewSet):
    queryset = DataMoverConfig.objects.all()
    serializer_class = DataMoverConfigSerializer
