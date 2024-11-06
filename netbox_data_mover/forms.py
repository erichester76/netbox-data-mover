
from django import forms
from netbox.forms import NetBoxModelForm
from .models import DataMoverConfig, DataMoverDataSource
from utilities.forms.fields import DynamicModelChoiceField


class DataMoverConfigForm(NetBoxModelForm):
    
    class Meta:
        SCHEDULE_CHOICES = [
        ('', 'None - Manual Only'),
        ('0 * * * *', 'Hourly'),
        ('0 0 * * *', 'Daily'),
        ('0 0 * * 0', 'Weekly'),
        ('0 0 1 * *', 'Monthly'),
        ]
        
        model = DataMoverConfig
        fields = ['source', 'source_endpoint', 'destination', 'destination_endpoint', 'name', 'schedule', 'description']
        
        source = DynamicModelChoiceField(
            queryset=DataMoverDataSource.objects.all(),
            required=True,
            label="Source",
            help_text="Select the data source."
        )
        
        destination = DynamicModelChoiceField(
            queryset=DataMoverDataSource.objects.all(),
            required=True,
            label="Destination",
            help_text="Select the data destination."
        )
        
        source_endpoint = DynamicModelChoiceField(
            queryset=DataMoverDataSource.objects.none(),
            required=True,
            label="Source Endpoint",
            query_params={'endpoint_id': '$source', 'type': 'endpoints'},
            help_text="Select an endpoint for the chosen source."
        )

        destination_endpoint = DynamicModelChoiceField(
            queryset=DataMoverDataSource.objects.none(),
            required=True,
            label="Destination Endpoint",
            query_params={'endpoint_id': '$destination', 'type': 'endpoints'},
            help_text="Select an endpoint for the chosen destination."
        )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class DataMoverDataSourceForm(NetBoxModelForm):
    class Meta:
        model = DataMoverDataSource
        fields = [
            'name', 'type', 'module', 'endpoints', 'auth_method', 'auth_function', 
            'find_function', 'create_function', 'update_function', 'fetch_function', 
            'auth_args', 'base_urls'
        ]
