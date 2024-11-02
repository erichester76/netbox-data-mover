
from rest_framework import viewsets
from .serializers import DataMoverConfigSerializer
from ..models import DataMoverConfig

class DataMoverConfigViewSet(viewsets.ModelViewSet):
    queryset = DataMoverConfig.objects.all()
    serializer_class = DataMoverConfigSerializer
