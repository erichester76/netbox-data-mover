
from django import forms
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import DynamicModelChoiceField
from .models import DataMoverConfig, DataMoverDataSource

class DataMoverConfigForm(NetBoxModelForm):
 
    source = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.all(),
        required=True,
        label="Source",
        help_text="Select the data source."
    )
    source_endpoint = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),
        required=True,
        label="Source Endpoint",
        query_params={'datasource_id': '$source', 'type': 'endpoints'},
        help_text="Select an endpoint for the chosen source."
    )
    source_mapping_fields = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),  # Start with none, will be updated dynamically
        required=False,
        label="Source Mapping Field",
        query_params={'datasource_id': '$source_endpoint', 'type': 'mapping_fields'},
        help_text="Select the field for mapping from the source endpoint."
    )
    
    destination = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.all(),
        required=True,
        label="Destination",
        help_text="Select the data destination."
    )
    destination_endpoint = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),
        required=True,
        label="Destination Endpoint",
        query_params={'datasource_id': '$destination', 'type': 'endpoints'},
        help_text="Select an endpoint for the chosen destination."
    )
    destination_mapping_fields = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),  # Start with none, will be updated dynamically
        required=False,
        label="Destination Mapping Field",
        query_params={'datasource_id': '$destination_endpoint', 'type': 'mapping_fields'},
        help_text="Select the field for mapping to the destination endpoint."
    )
    SCHEDULE_CHOICES = [
        ('', 'None - Manual Only'),
        ('0 * * * *', 'Hourly'),
        ('0 0 * * *', 'Daily'),
        ('0 0 * * 0', 'Weekly'),
        ('0 0 1 * *', 'Monthly'),
    ]
    schedule = forms.ChoiceField(choices=SCHEDULE_CHOICES)
           
    class Meta:    
        model = DataMoverConfig
        fields = ['source', 'source_endpoint', 'source_mapping_fields',
                  'destination', 'destination_endpoint', 'destination_mapping_fields',
                  'name', 'schedule', 'description']

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
