from django import forms
from .models import DataMoverConfig, DataMoverDataSource


class DataMoverConfigForm(forms.ModelForm):
    class Meta:
        model = DataMoverConfig
        fields = ['name', 'schedule', 'description', 'source', 'source_endpoint', 'destination', 'destination_endpoint']
        widgets = {
            'source': forms.Select(attrs={'class': 'form-select'}),
            'source_endpoint': forms.Select(attrs={'class': 'form-select'}),
            'destination': forms.Select(attrs={'class': 'form-select'}),
            'destination_endpoint': forms.Select(attrs={'class': 'form-select'}),
        }
        SCHEDULE_CHOICES = [
            ('0 * * * *', 'Hourly'),
            ('0 0 * * *', 'Daily'),
            ('0 0 * * 0', 'Weekly'),
            ('0 0 1 * *', 'Monthly'),
        ]

        name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control d-inliune-block col-md-6'}))
        schedule = forms.ChoiceField(
        choices=SCHEDULE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select d-inliune-block col-md-6'})
    )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[]
        self.fields['source'].widget.attrs.update({'class': 'form-select d-inline-block col-md-6'})
        self.fields['source_endpoint'].widget.attrs.update({'class': 'form-select d-inline-block col-md-6'})
        self.fields['destination'].widget.attrs.update({'class': 'form-select d-inline-block col-md-6'})
        self.fields['destination_endpoint'].widget.attrs.update({'class': 'form-select d-inline-block col-md-6'})   
            
class DataMoverDataSourceForm(forms.ModelForm):
    class Meta:
        model = DataMoverDataSource
        fields = ['name', 'type', 'module', 'auth_method', 'auth_function', 'find_function', 'create_function', 'update_function', 'fetch_function', 'auth_args', 'base_urls']
