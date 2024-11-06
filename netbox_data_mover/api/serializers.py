from ..models import DataMoverConfig, DataMoverDataSource
from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers

class DataMoverDataSourceSerializer(NetBoxModelSerializer):

    class Meta:
        model = DataMoverDataSource
        fields = ['id', 'display', 'name', 'type', 'endpoints']

    def get_endpoints(self, obj):
        return [{'id': idx, 'display': endpoint.strip()} for idx, endpoint in enumerate(obj.endpoints.split(','))]

class DataMoverConfigSerializer(NetBoxModelSerializer):

    class Meta:
        model = DataMoverConfig
        fields = ['id', 'display', 'display_url', 'name', 'description', 'schedule', 'source', 'destination', 'endpoints', 'last_run_records_changed', 'last_run_status', 'last_run_time']
   

