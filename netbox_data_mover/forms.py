from django import forms
from .models import DataMoverConfig, DataMoverDataSource

class DataMoverConfigForm(forms.ModelForm):
    class Meta:
        SCHEDULE_CHOICES = [
            ('0 * * * *', 'Hourly'),
            ('0 0 * * *', 'Daily'),
            ('0 0 * * 0', 'Weekly'),
            ('0 0 1 * *', 'Monthly'),
        ]
        model = DataMoverConfig
        fields = ['name', 'schedule', 'description', 'source', 'source_endpoint', 'destination', 'destination_endpoint']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control d-inline-block col-md-6'}),
            'schedule': forms.Select(choices=SCHEDULE_CHOICES, attrs={'class': 'form-select d-inline-block col-md-6'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'source': forms.Select(attrs={'class': 'form-select d-inline-block col-md-6'}),
            'source_endpoint': forms.TextInput(attrs={'class': 'form-control d-inline-block col-md-6'}),
            'destination': forms.Select(attrs={'class': 'form-select d-inline-block col-md-6'}),
            'destination_endpoint': forms.TextInput(attrs={'class': 'form-control d-inline-block col-md-6'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Any custom initialization can go here if required
            
class DataMoverDataSourceForm(forms.ModelForm):
    class Meta:
        model = DataMoverDataSource
        fields = ['name', 'type', 'module', 'auth_method', 'auth_function', 'find_function', 'create_function', 'update_function', 'fetch_function', 'auth_args', 'base_urls']
