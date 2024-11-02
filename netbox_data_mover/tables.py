
import django_tables2 as tables
from .models import DataMoverConfig

class DataMoverConfigTable(tables.Table):
    class Meta:
        model = DataMoverConfig
        fields = ('name', 'description', 'schedule', 'source', 'destination', 'last_run_status', 'last_run_records_changed', 'last_run_time')
