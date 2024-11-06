from django import forms
from netbox.forms import NetBoxModelForm
from .models import DataMoverConfig, DataMoverDataSource
from utilities.forms.fields import DynamicModelChoiceField


class DataMoverConfigForm(NetBoxModelForm):
    
    

    source = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),
        required=True,        
    )

    destination = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),
        required=True,
    )

    source_endpoint = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),
        required=True,
        query_params={'datamoverdatasourceid': '$source', 'type': 'endpoints'},
    )

    destination_endpoint = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),
        required=True,
        query_params={'datamoverdatasourceid': '$destination', 'type': 'endpoints'},
    )

    class Meta:
        SCHEDULE_CHOICES = [
        ('', 'None - Manual Only'),
        ('0 * * * *', 'Hourly'),
        ('0 0 * * *', 'Daily'),
        ('0 0 * * 0', 'Weekly'),
        ('0 0 1 * *', 'Monthly'),
    ]
        model = DataMoverConfig
        fields = [
            'name', 'schedule', 'description', 
            'source', 'source_endpoint', 'destination', 'destination_endpoint'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control d-inline-block col-md-6'}),
            'schedule': forms.Select(choices=SCHEDULE_CHOICES, attrs={'class': 'form-select d-inline-block col-md-6'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

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
