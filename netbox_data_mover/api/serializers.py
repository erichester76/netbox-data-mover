from netbox.api.serializers import NetBoxModelSerializer
from ..models import DataMoverConfig, DataMoverDataSource

class DataMoverConfigSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataMoverConfig
        fields = '__all__'

class DataMoverDataSourceSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataMoverDataSource
        fields = '__all__'