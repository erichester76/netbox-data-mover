from .models import DataMoverConfig, DataMoverDataSource
from netbox.forms import NetBoxModelForm

class DataMoverForm(NetBoxModelForm):
    class Meta:
        model = DataMoverConfig
        fields = [ 'name', 'description', 'schedule', 'source', 'destination'  ]
        
class DataMoverDataSourceForm(NetBoxModelForm):
    class Meta:
        model = DataMoverDataSource
        fields = ['name', 'type', 'api_url', 'auth_details']