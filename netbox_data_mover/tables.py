import django_tables2 as tables
from .models import DataMoverConfig, DataMoverDataSource
from netbox.tables import NetBoxTable

class DataMoverConfigTable(NetBoxTable):
    name = tables.Column(linkify=True)
    
    class Meta:
        model = DataMoverConfig
        default_columns = ('name', 'description', 'schedule', 'last_run_status', 'last_run_time')
        fields = ('pk', 'id', 'name', 'description', 'schedule', 'source', 'destination', 'fetch_data_definition', 'transformations', 'last_run_status', 'last_run_records_changed', 'last_run_time')

class DataMoverDataSourceTable(NetBoxTable):
    name = tables.Column(linkify=True)
    
    class Meta:
        model = DataMoverDataSource
        default_columns = ('name', 'type', 'api_url', 'auth_details')
        fields = ('pk', 'id', 'name', 'type', 'api_url', 'auth_details')
        