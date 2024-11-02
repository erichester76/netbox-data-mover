from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import DataSource, DataMoverConfig
from .serializers import DataSourceSerializer, DataMoverConfigSerializer

class DataSourceListAPIView(ListAPIView):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer

class DataMoverConfigListAPIView(ListAPIView):
    queryset = DataMoverConfig.objects.all()
    serializer_class = DataMoverConfigSerializer

class DataMoverConfigDetailAPIView(RetrieveAPIView):
    queryset = DataMoverConfig.objects.all()
    serializer_class = DataMoverConfigSerializer
