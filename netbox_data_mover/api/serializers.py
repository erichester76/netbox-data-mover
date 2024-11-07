from ..models import DataMoverConfig, DataMoverDataSource
from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers

class EndpointSerializer(NetBoxModelSerializer):
    id = serializers.IntegerField()
    display = serializers.CharField()
    name = serializers.CharField()
    slug = serializers.CharField()
    description = serializers.CharField()

class DataMoverDataSourceSerializer(NetBoxModelSerializer):
    endpoints = EndpointSerializer(source='get_endpoints', many=True, read_only=True)

    class Meta:
        model = DataMoverDataSource
        fields = ['id', 'name', 'display', 'type', 'module', 'auth_method', 'auth_function', 'endpoints']
        brief_fields=  ['id', 'display', 'name']
      
class DataMoverConfigSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataMoverConfig
        fields = ['id', 'name', 'display', 'description', 'schedule', 'source', 'destination', 'last_run_records_changed', 'last_run_status', 'last_run_time']
        brief_fields = ['id', 'display', 'name']
