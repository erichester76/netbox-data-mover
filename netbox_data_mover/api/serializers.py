from ..models import DataMoverConfig, DataMoverDataSource
from netbox.api.serializers import NetBoxModelSerializer


class DataMoverDataSourceSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataMoverDataSource
        fields = ['id', 'display', 'display_url', 'name', 'type', 'module', 'auth_method', 'auth_function', 'find_function', 'create_function', 'update_function', 'fetch_function', 'auth_args', 'base_urls']

class DataMoverConfigSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataMoverConfig
        fields = ['id', 'display', 'display_url', 'name', 'description', 'schedule', 'source', 'destination', 'last_run_records_changed', 'last_run_status', 'last_run_time']

class DataSourceFieldsSerializer(NetBoxModelSerializer):
    class Meta:
        model = DataMoverDataSource
        fields = ['id', 'display', 'display_url', 'name', 'module', 'auth_function']
