import django_tables2 as tables
from .models import DataMoverConfig, DataMoverDataSource
from netbox.tables import NetBoxTable

class DataMoverConfigTable(NetBoxTable):
    name = tables.Column(linkify=True)
    
    class Meta:
        model = DataMoverConfig
        fields = ('name', 'description', 'schedule', 'source', 'destination', 'last_run_status', 'last_run_records_changed', 'last_run_time')
        default_columns = ('name', 'description', 'schedule', 'last_run_status', 'last_run_time')

class DataMoverDataSourceTable(NetBoxTable):
    name = tables.Column(linkify=True)
    
    class Meta:
        model = DataMoverDataSource
        fields = ('name', 'type', 'api_url', 'auth_details')
        default_columns = ('name', 'type', 'api_url', 'auth_details')