from django import forms
from .models import DataMoverConfig, DataMoverDataSource

class DataMoverConfigForm(forms.ModelForm):
    class Meta:
        model = DataMoverConfig
        fields = ['name', 'description', 'schedule', 'source', 'destination', 'source_endpoint', 'destination_endpoint', 'mappings','last_run_records', 'last_run_status', 'last_run_time']

class DataMoverDataSourceForm(forms.ModelForm):
    class Meta:
        model = DataMoverDataSource
        fields = ['name', 'type', 'module', 'auth_method', 'auth_function', 'find_function', 'create_function', 'update_function', 'fetch_function', 'auth_args', 'base_urls']
