import django_tables2 as tables
from .models import DataMoverConfig, DataMoverDataSource
from netbox.tables import NetBoxTable

class DataMoverConfigTable(NetBoxTable):
    name = tables.Column(linkify=True)
    source = tables.Column(linkify=True)
    destination = tables.Column(linkify=True)
 
    
    class Meta:
        verbose_name='Job Configuration'
        verbose_name_plural='Jobs'
        model = DataMoverConfig
        fields = ('name', 'description', 'schedule', 'source', 'destination', 'last_run_status', 'last_run_records_changed', 'last_run_time')

class DataMoverDataSourceTable(NetBoxTable):
    name = tables.Column(linkify=True)

    
    class Meta:
        verbose_name='Data Source Configuration'
        verbose_name_plural='Data Sources'

        model = DataMoverDataSource
        fields = ('name', 'type', 'api_url', 'auth_details')