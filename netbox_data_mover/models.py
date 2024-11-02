
from django.db import models
from netbox.models import NetBoxModel

class DataSource(NetBoxModel):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    api_url = models.URLField(max_length=200)
    auth_details = models.JSONField()  # Authentication details

    def __str__(self):
        return self.name

class DataMoverConfig(NetBoxModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    schedule = models.CharField(max_length=100)
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE, related_name="source")
    destination = models.ForeignKey(DataSource, on_delete=models.CASCADE, related_name="destination")
    fetch_data_definition = models.JSONField()  # JSON to define data fetching
    transformations = models.JSONField()  # Transformation details
    last_run_status = models.CharField(max_length=50, null=True, blank=True)
    last_run_records_changed = models.IntegerField(null=True, blank=True)
    last_run_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name