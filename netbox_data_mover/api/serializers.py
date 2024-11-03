from rest_framework import serializers
from ..models import DataMoverConfig, DataMoverDataSource
from netbox.api.serializers import NetBoxModelSerializer

class DataMoverDataSourceSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataMoverDataSource
        fields = '__all__'

class DataMoverConfigSerializer(NetBoxModelSerializer):
    source_api = serializers.HyperlinkedRelatedField(
        view_name='plugins-api:netbox_data_mover:datamoverdatasource-detail',
        queryset=DataMoverDataSource.objects.all(),
        lookup_field='pk'
    )
    destination_api = serializers.HyperlinkedRelatedField(
        view_name='plugins-api:netbox_data_mover:datamoverdatasource-detail',
        queryset=DataMoverDataSource.objects.all(),
        lookup_field='pk'
    )

    class Meta:
        model = DataMoverConfig
        fields = '__all__'