
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import DataMoverConfig
from .forms import ConfigForm
from netbox.views import generic
from extras.jobs import get_job


class DataMoverConfigView(generic.ObjectView):
    
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
                if field.name in excluded_extras or ('equirement' in field.name):
                    continue      
                
                value = None
                url = None

                field_data.append({
                    'name': field.verbose_name if hasattr(field, 'verbose_name') else field.name,
                    'value': value,
                    'url': url, 
                })
            
def DataMoverCreateView(request):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('netbox_data_mover:index')
    else:
        form = ConfigForm()
    return render(request, 'netbox_data_mover/create.html', {'form': form})

def trigger_job_view(request, pk):
    config = get_object_or_404(DataMoverConfig, pk=pk)
    # Triggering the DataMoverJob using NetBox's job execution API
    job_class = get_job('netbox_data_mover.jobs.DataMoverJob')
    job_data = {'config_id': config.pk}
    job_result = job_class.enqueue(job_data)
    # Update status to show pending execution
    config.last_run_status = "Pending"
    config.last_run_time = timezone.now()
    config.save()
    return redirect('netbox_data_mover:detail', pk=pk)
