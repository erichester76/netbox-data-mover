from ..models import DataMoverConfig, DataMoverDataSource
from netbox.api.serializers import NetBoxModelSerializer


class DataMoverDataSourceSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataMoverDataSource
        fields = '__all__'

class DataMoverConfigSerializer(NetBoxModelSerializer):

    class Meta:
        model = DataMoverConfig
        fields = '__all__'