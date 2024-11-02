
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import DataMoverConfig
from .forms import ConfigForm

def index_view(request):
    configs = DataMoverConfig.objects.all()
    return render(request, 'netbox_data_mover/index.html', {'configs': configs})

def create_view(request):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('netbox_data_mover:index')
    else:
        form = ConfigForm()
    return render(request, 'netbox_data_mover/create.html', {'form': form})

def detail_view(request, pk):
    config = get_object_or_404(DataMoverConfig, pk=pk)
    return render(request, 'netbox_data_mover/view.html', {'config': config})

def trigger_job_view(request, pk):
    config = get_object_or_404(DataMoverConfig, pk=pk)
    # Triggering the DataMoverJob using NetBox's job execution API
    from extras.jobs import get_job
    job_class = get_job('netbox_data_mover.jobs.DataMoverJob')
    job_data = {'config_id': config.pk}
    job_result = job_class.enqueue(job_data)
    # Update status to show pending execution
    config.last_run_status = "Pending"
    config.last_run_time = timezone.now()
    config.save()
    return redirect('netbox_data_mover:detail', pk=pk)
