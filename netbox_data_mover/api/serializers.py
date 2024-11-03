from rest_framework import serializers
from ..models import DataMoverConfig, DataMoverDataSource
from netbox.api.serializers import NetBoxModelSerializer


class DataMoverDataSourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataMoverDataSource
        fields = '__all__'
        extra_kwargs = {
            'url': {
                'view_name': 'plugins-api:netbox_data_mover:datamoverdatasource-detail',
                'lookup_field': 'pk'
            }
        }

class DataMoverConfigSerializer(NetBoxModelSerializer):
    source = serializers.HyperlinkedRelatedField(
        view_name='plugins-api:netbox_data_mover:datamoverdatasource-detail',
        queryset=DataMoverDataSource.objects.all(),
        lookup_field='pk'
    )
    destination = serializers.HyperlinkedRelatedField(
        view_name='plugins-api:netbox_data_mover:datamoverdatasource-detail',
        queryset=DataMoverDataSource.objects.all(),
        lookup_field='pk'
    )

    class Meta:
        model = DataMoverConfig
        fields = '__all__'