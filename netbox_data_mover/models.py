
from django.db import models
from netbox.models import NetBoxModel
from django.urls import reverse  # Import reverse

class DataMoverDataSource(NetBoxModel):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    api_url = models.URLField(max_length=200)
    auth_details = models.JSONField() 
    
    class Meta:
        ordering = ['name']
        verbose_name = ('Data Source')
        verbose_name_plural = ('Data Sources')    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_data_mover:datamoverdatasource_detail', kwargs={'pk': self.pk})

class DataMoverConfig(NetBoxModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    schedule = models.CharField(max_length=100, null=True, blank=True)
    source = models.ForeignKey(DataMoverDataSource, on_delete=models.CASCADE, related_name="source")
    destination = models.ForeignKey(DataMoverDataSource, on_delete=models.CASCADE, related_name="destination")
    fetch_data_definition = models.JSONField(null=True)  # JSON to define data fetching
    transformations = models.JSONField(null=True, blank=True)  # Transformation details
    last_run_status = models.CharField(max_length=50, null=True, blank=True)
    last_run_records_changed = models.IntegerField(null=True, blank=True)
    last_run_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = ('Job')
        verbose_name_plural = ('Jobs')    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_data_mover:datamover_detail', kwargs={'pk': self.pk})
