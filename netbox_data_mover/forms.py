
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
        fields = ['__all__']
        
        source = DynamicModelChoiceField(
           queryset=DataMoverDataSource.objects.none(),
           required=True,        
        )
        
        destination = DynamicModelChoiceField(
           queryset=DataMoverDataSource.objects.none(),
           required=True,
        )
        
        source_endpoint = DynamicModelChoiceField(
            queryset=DataMoverDataSource.objects.all(),
            required=True,
            query_params={'endpoint_id': '$source', 'type': 'endpoints'},
        )

        destination_endpoint = DynamicModelChoiceField(
            queryset=DataMoverDataSource.objects.all(),
            required=True,
            query_params={'endpoint_d': '$destination', 'type': 'endpoints'},
        )
        
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
