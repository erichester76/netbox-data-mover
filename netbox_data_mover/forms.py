
from django import forms
from .models import DataMoverConfig
from netbox.forms import NetBoxModelForm, NetBoxModelImportForm

class ConfigForm(NetBoxModelForm):
    class Meta:
        model = DataMoverConfig
        fields = ['name', 'description', 'schedule', 'source', 'destination', 'transformations']
