from ..models import DataMoverConfig, DataMoverDataSource
from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers

class DataMoverDataSourceSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataMoverDataSource
        fields = ['id', 'display', 'display_url', 'name', 'type', 'module', 'auth_method', 'auth_function', 'find_function', 'create_function', 'update_function', 'fetch_function', 'auth_args', 'base_urls']

class EndpointsSerializer(serializers.Serializer):
    # This handles endpoints assuming they are a list of strings
    endpoints = serializers.ListField(
        child=serializers.CharField(max_length=200)
    )
    
class DataMoverConfigSerializer(NetBoxModelSerializer):
    endpoints = EndpointsSerializer(source='get_endpoints_data', read_only=True)

    class Meta:
        model = DataMoverConfig
        fields = ['id', 'display', 'display_url', 'name', 'description', 'schedule', 'source', 'destination', 'endpoints', 'last_run_records_changed', 'last_run_status', 'last_run_time']

    def get_display(self, obj):
        return obj.name

    def get_endpoints_data(self, obj):
        # Custom method to convert the text field into a list of endpoints
        if obj.endpoints:
            return {'endpoints': [endpoint.strip() for endpoint in obj.endpoints.split(',')]}
        return {'endpoints': []}
   

