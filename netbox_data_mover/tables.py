import django_tables2 as tables
from netbox.tables import NetBoxTable
from .models import DataMoverConfig, DataMoverDataSource

class DataMoverConfigTable(NetBoxTable):
    name = tables.Column(linkify=True)
    source = tables.Column(linkify=True)
    destination = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = DataMoverConfig
        fields = ('pk', 'name', 'description', 'schedule', 'source', 'destination', 'source_endpoint', 'destination_endpoint', 'mappings', 'last_run_records_changed', 'last_run_status', 'last_run_time')
        default_columns = ('name', 'description', 'schedule', 'source', 'destination', 'last_run_status', 'last_run_records_changed', 'last_run_time')

class DataMoverDataSourceTable(NetBoxTable):
    name = tables.Column(linkify=True)
    type = tables.Column()
    module = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = DataMoverDataSource
        fields = ('pk', 'name', 'type', 'module', 'auth_method', 'auth_function', 'find_function', 'create_function', 'update_function', 'fetch_function', 'auth_args', 'base_urls')
        default_columns = ('name', 'type', 'module')
