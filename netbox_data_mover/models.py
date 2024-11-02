
from django.db import models
from netbox.models import NetBoxModel

class DataSourceModel(NetBoxModel):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    connection_details = models.JSONField()

    def __str__(self):
        return self.name

class DataDestinationModel(NetBoxModel):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    connection_details = models.JSONField()

    def __str__(self):
        return self.name

class DataMoverConfig(NetBoxModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    schedule = models.CharField(max_length=100)
    source = models.ForeignKey(DataSourceModel, on_delete=models.CASCADE)
    destination = models.ForeignKey(DataDestinationModel, on_delete=models.CASCADE)
    transformations = models.JSONField()  # Transformation details
    last_run_status = models.CharField(max_length=50, null=True, blank=True)
    last_run_records_changed = models.IntegerField(null=True, blank=True)
    last_run_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
