from django_filters import FilterSet
from .models import DataMoverConfig, DataSource
from netbox.filtersets import NetBoxModelFilterSet

class DataMoverConfigFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = DataMoverConfig
        fields = ['name', 'source', 'destination']

class DataSourceFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = DataSource
        fields = ['name', 'type']