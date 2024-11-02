
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import DataMoverConfig
from .forms import ConfigForm
from .tables import DataMoverConfigTable
from .jobs import DataMoverJob

from netbox.views import generic


class DataMoverView(generic.ObjectView):
    
    def get_extra_context(self, request, instance):
            # Extract fields and their values for the object, including relationships
            field_data = []
            object_name = instance._meta.verbose_name
            # Define fields to exclude
            excluded_extras = {
                'id', 
                'custom_field_data', 
                'tags', 
                'bookmarks', 
                'journal_entries', 
                'subscriptions', 
                'tagged_items', 
                'created',
                'last_updated',
                'object_id',
                'object_type'
            }

            # Extract fields and their values for the object, including relationships
            field_data = []
            for field in instance._meta.get_fields():      
                # Skip excluded fields listed above
                if field.name in excluded_extras:
                    continue      
                
                value = None
                url = None

                field_data.append({
                    'name': field.verbose_name if hasattr(field, 'verbose_name') else field.name,
                    'value': value,
                    'url': url, 
                })
            
class DataMoverEditView(generic.ObjectEditView):
    queryset = DataMoverConfig.objects.all()

class DataMoverDeleteView(generic.ObjectEditView):
    queryset = DataMoverConfig.objects.all()
    
class DataMoverListView(generic.ObjectEditView):
    queryset = DataMoverConfig.objects.all()
    table = DataMoverConfigTable

class DataMoverConfigTriggerJobView(generic.ObjectEditView):
    model = DataMoverConfig

    def post(self, request, *args, **kwargs):
        config = get_object_or_404(DataMoverConfig, pk=kwargs['pk'])
        job_instance = DataMoverJob()
        job_instance.enqueue_run({'config_id': config.pk})
        # Update status to show pending execution
        config.last_run_status = "Pending"
        config.last_run_time = timezone.now()
        config.save()
        return redirect('plugins:netbox_data_mover:datamoverconfig_detail', pk=config.pk)
