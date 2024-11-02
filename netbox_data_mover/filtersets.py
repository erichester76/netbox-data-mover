
from django_filters import FilterSet
from .models import DataMoverConfig

class DataMoverConfigFilterSet(FilterSet):
    class Meta:
        model = DataMoverConfig
        fields = ['name', 'source', 'destination']
