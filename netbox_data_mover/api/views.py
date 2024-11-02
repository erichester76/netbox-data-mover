
from .serializers import DataMoverConfigSerializer
from ..models import DataMoverConfig
from netbox.api.viewsets import NetBoxModelViewSet

class DataMoverConfigViewSet(NetBoxModelViewSet):
    queryset = DataMoverConfig.objects.all()
    serializer_class = DataMoverConfigSerializer
