from ..models import DataMoverConfig, DataMoverDataSource
from netbox.api.serializers import NetBoxModelSerializer

class DataMoverDataSourceSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataMoverDataSource
        fields = ['id', 'display', 'display_url', 'name', 'type', 'module', 'endpoints', 'auth_method', 'auth_function', 'find_function', 'create_function', 'update_function', 'fetch_function', 'auth_args', 'base_urls']
        brief_fields = ['id', 'display', 'display_url', 'name', 'type', 'endpoints' ] 
        
class DataMoverConfigSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataMoverConfig
        fields = ['id', 'display', 'display_url', 'name', 'description', 'schedule', 'source', 'destination', 'last_run_records_changed', 'last_run_status', 'last_run_time']
