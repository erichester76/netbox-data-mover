
from django import forms
from .models import DataMoverConfig

class ConfigForm(forms.ModelForm):
    class Meta:
        model = DataMoverConfig
        fields = ['name', 'description', 'schedule', 'source', 'destination', 'transformations']
