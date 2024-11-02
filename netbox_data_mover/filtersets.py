
from django_filters import FilterSet
from .models import DataMoverConfig
from netbox.filtersets import NetBoxModelFilterSet

class DataMoverConfigFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = DataMoverConfig
        fields = ['name', 'source', 'destination']
