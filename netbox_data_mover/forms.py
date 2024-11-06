from django import forms
from netbox.forms import NetBoxModelForm
from .models import DataMoverConfig, DataMoverDataSource
from utilities.forms.fields import DynamicModelChoiceField

class DataMoverConfigForm(forms.ModelForm):
    class Meta:
        
        SCHEDULE_CHOICES = [
            ('','None - Manual Only'),
            ('0 * * * *', 'Hourly'),
            ('0 0 * * *', 'Daily'),
            ('0 0 * * 0', 'Weekly'),
            ('0 0 1 * *', 'Monthly'),
        ]  
        model = DataMoverConfig
        fields = ['name', 'schedule', 'description', 'source', 'source_endpoint', 'destination', 'destination_endpoint']
  
        source_endpoint = DynamicModelChoiceField(
            queryset=DataMoverDataSource.objects.all(),
            required=True,
            query_params={'type': 'endpoints'},
            widget=forms.Select(attrs={'class': 'form-control d-inline-block col-md-6'})
        )

        destination_endpoint = DynamicModelChoiceField(
            queryset=DataMoverDataSource.objects.all(),
            required=True,
            query_params={'type': 'endpoints'},
            widget=forms.Select(attrs={'class': 'form-control d-inline-block col-md-6'})
        )
        
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control d-inline-block col-md-6'}),
            'schedule': forms.Select(choices=SCHEDULE_CHOICES, attrs={'class': 'form-select d-inline-block col-md-6'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['source_endpoint'].choices = ['Please Chose Source First']  # To be dynamically populated
        self.fields['destination_endpoint'].choices = ['Please Chose Destination First']  # To be dynamically populated
        
class DataMoverDataSourceForm(forms.ModelForm):
    class Meta:
        model = DataMoverDataSource
        fields = ['name', 'type', 'module', 'endpoints', 'auth_method', 'auth_function', 'find_function', 'create_function', 'update_function', 'fetch_function', 'auth_args', 'base_urls']