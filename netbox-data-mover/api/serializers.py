
from rest_framework import serializers
from ..models import DataMoverConfig

class DataMoverConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataMoverConfig
        fields = '__all__'
