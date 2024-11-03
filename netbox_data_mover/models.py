
from django.db import models
from netbox.models import NetBoxModel
from django.urls import reverse  # Import reverse

class DataMoverDataSource(NetBoxModel):
    TYPE_CHOICES = [
        ('api', 'API'),
        ('rest', 'REST API'),
        ('csv', 'CSV'),
        ('snmp', 'SNMP'),
        ('xls', 'XLS'),
        ('sql', 'SQL'),
        ('')
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    module = models.CharField(max_length=100)
    auth_method = models.CharField(max_length=50, blank=True, null=True)
    auth_function = models.TextField(blank=True, null=True) 
    find_function = models.TextField(blank=True, null=True) 
    create_function = models.TextField(blank=True, null=True) 
    update_function = models.TextField(blank=True, null=True) 
    fetch_function = models.TextField(blank=True, null=True)  
    auth_args = models.JSONField(blank=True, null=True)  
    base_urls = models.JSONField()  

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
    schedule = models.CharField(max_length=100)

    source = models.ForeignKey(DataMoverDataSource, on_delete=models.CASCADE, related_name="source")
    source_endpoint = models.CharField(max_length=100)
    
    destination = models.ForeignKey(DataMoverDataSource, on_delete=models.CASCADE, related_name="destination")
    destination_endpoint = models.CharField(max_length=100)

    mappings = models.JSONField()  

    # Run statistics
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
