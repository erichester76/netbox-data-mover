from netbox.api.serializers import NetBoxModelSerializer
from ..models import DataMoverConfig, DataSource

class DataMoverConfigSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataMoverConfig
        fields = '__all__'

class DataSourceSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataSource
        fields = '__all__'