
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import DataMoverConfig

class DataMoverConfigSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataMoverConfig
        fields = '__all__'
