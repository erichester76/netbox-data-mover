from .serializers import DataMoverConfigSerializer, DataSourceSerializer
from ..models import DataMoverConfig, DataSource
from netbox.api.viewsets import NetBoxModelViewSet

class DataMoverConfigViewSet(NetBoxModelViewSet):
    queryset = DataMoverConfig.objects.all()
    serializer_class = DataMoverConfigSerializer

class DataSourceViewSet(NetBoxModelViewSet):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer