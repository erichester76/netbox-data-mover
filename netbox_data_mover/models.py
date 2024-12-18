
from django.db import models
from netbox.models import NetBoxModel
from django.urls import reverse  # Import reverse

class DataMoverDataSource(NetBoxModel):
    TYPE_CHOICES = [
        ('api', 'Python SDK/API Call'),
        ('rest', 'Direct REST API Call'),
        ('csv', 'CSV File Import'),
        ('snmp', 'SNMP Query'),
        ('xls', 'XLS(x) File'),
        ('sql', 'SQL Query'),
        ('promql','Prometheus Query'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    module = models.CharField(max_length=100, null=True)
    auth_method = models.CharField(max_length=50, null=True)
    auth_function = models.TextField(null=True) 
    find_function = models.TextField(null=True) 
    create_function = models.TextField(null=True) 
    update_function = models.TextField(null=True) 
    fetch_function = models.TextField(null=True)  
    endpoints = models.TextField(null=True, help_text="Comma separated list of available endpoints.")

    auth_args = models.JSONField(blank=True, null=True)  
    base_urls = models.JSONField(null=True)  
    
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
    schedule = models.CharField(max_length=100,null=True)

    source = models.ForeignKey(DataMoverDataSource, on_delete=models.CASCADE, related_name="source")
    source_endpoint = models.CharField(max_length=100,null=True)
    
    destination = models.ForeignKey(DataMoverDataSource, on_delete=models.CASCADE, related_name="destination")
    destination_endpoint = models.CharField(max_length=100,null=True)

    mappings = models.JSONField(null=True)  

    # Run statistics
    last_run_status = models.CharField(max_length=50, null=True, blank=True)
    last_run_records_changed = models.IntegerField(null=True, blank=True)
    last_run_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = ('Data Mover Job')
        verbose_name_plural = ('Data Mover Jobs')    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_data_mover:datamover_detail', kwargs={'pk': self.pk})
