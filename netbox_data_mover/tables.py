import django_tables2 as tables
from netbox.tables import NetBoxTable
from .models import DataMoverConfig, DataMoverDataSource

class DataMoverConfigTable(NetBoxTable):
    name = tables.Column(linkify=True)
    source_api = tables.Column(linkify=True)
    destination_api = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = DataMoverConfig
        fields = ('pk', 'name', 'description', 'schedule', 'source_api', 'destination_api', 'last_run_status', 'last_run_time')
        default_columns = ('name', 'description', 'schedule', 'source_api', 'destination_api', 'last_run_status', 'last_run_time')

class DataMoverDataSourceTable(NetBoxTable):
    name = tables.Column(linkify=True)
    type = tables.Column()
    module = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = DataMoverDataSource
        fields = ('pk', 'name', 'type', 'module', 'auth_method', 'base_urls')
        default_columns = ('name', 'type', 'module', 'auth_method', 'base_urls')
