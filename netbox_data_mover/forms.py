from django import forms
from .models import DataMoverConfig, DataSource
from netbox.forms import NetBoxModelForm

class ConfigForm(NetBoxModelForm):
    class Meta:
        model = DataMoverConfig
        fields = ['name', 'description', 'schedule', 'source', 'destination', 'fetch_data_definition', 'transformations']

class DataSourceForm(NetBoxModelForm):
    class Meta:
        model = DataSource
        fields = ['name', 'type', 'api_url', 'auth_details']