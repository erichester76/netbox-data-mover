from django_filters import FilterSet
from .models import DataMoverConfig, DataMoverDataSource
from netbox.filtersets import NetBoxModelFilterSet

class DataMoverConfigFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = DataMoverConfig
        fields = ['name', 'source', 'destination']

class DataMoverDataSourceFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = DataMoverDataSource
        fields = ['name', 'type']