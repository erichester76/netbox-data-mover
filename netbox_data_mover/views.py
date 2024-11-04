from netbox.views import generic
from .models import DataMoverConfig, DataMoverDataSource
from .forms import DataMoverConfigForm, DataMoverDataSourceForm
from .tables import DataMoverConfigTable, DataMoverDataSourceTable
from .filtersets import DataMoverConfigFilterSet, DataMoverDataSourceFilterSet
from .base_views import BaseChangeLogView,  BaseObjectView, BaseChangeLogView
from django.urls import reverse 
from django.shortcuts import redirect, get_object_or_404
import inspect
import importlib
from django.http import JsonResponse

def inspect_module(request):
    # Get the datasource ID and find the corresponding DataMoverDataSource instance
    datasource_id = request.GET.get('datasource_id')
    try:
        datasource = DataMoverDataSource.objects.get(pk=datasource_id)
        module_name = datasource.module
        class_name = datasource.auth_function

        # Import the module and get the class specified by auth_function
        lib_module = importlib.import_module(module_name)
        class_obj = getattr(lib_module, class_name, None)

        if class_obj is None:
            return JsonResponse({'error': f'Class {class_name} not found in module {module_name}.'}, status=400)

        # Get all attributes and methods of the class
        attributes = [attr for attr, _ in inspect.getmembers(class_obj)]
        response_data = {
            'class_name': class_name,
            'attributes': attributes
        }
        return JsonResponse(response_data)

    except DataMoverDataSource.DoesNotExist:
        return JsonResponse({'error': 'Data source not found.'}, status=404)
    except ModuleNotFoundError:
        return JsonResponse({'error': f'Module {module_name} not found.'}, status=400)


class DataMoverConfigListView(generic.ObjectListView):
    queryset = DataMoverConfig.objects.all()
    table = DataMoverConfigTable
    permission_required = 'netbox_data_mover.view_datamoverconfig'
    
    def get(self, request, *args, **kwargs):
        if not DataMoverDataSource.objects.exists():
            self.extra_context = {
                'no_data_source_warning': "No Data Sources available. Please add a <a href='test'>Data Source</a> before creating a Mover Job."
            }
        return super().get(request, *args, **kwargs)
    
class DataMoverConfigDetailView(BaseObjectView):
    queryset = DataMoverConfig.objects.all()
    permission_required = 'netbox_data_mover.view_datamoverconfig'

class DataMoverConfigEditView(generic.ObjectEditView):
    queryset = DataMoverConfig.objects.all()  
    form = DataMoverConfigForm
    # dynamic javascript template to have more of a wizard feel  
    template_name = 'netbox_data_mover/job_edit.html'
    permission_required = 'netbox_data_mover.add_datamoverconfig'

class DataMoverConfigDeleteView(generic.ObjectDeleteView):
    queryset = DataMoverConfig.objects.all()
    permission_required = 'netbox_data_mover.delete_datamoverconfig'

class DataMoverConfigBulkImportView(generic.BulkImportView):
    queryset = DataMoverConfig.objects.all()
    model_form = DataMoverConfigForm
    permission_required = 'netbox_data_mover.add_datamoverconfig'

class DataMoverConfigBulkEditView(generic.BulkEditView):
    queryset = DataMoverConfig.objects.all()
    filterset = DataMoverConfigFilterSet
    table = DataMoverConfigTable
    form = DataMoverConfigForm
    permission_required = 'netbox_data_mover.change_datamoverconfig'

class DataMoverConfigBulkDeleteView(generic.BulkDeleteView):
    queryset = DataMoverConfig.objects.all()
    filterset = DataMoverConfigFilterSet
    table = DataMoverConfigTable
    permission_required = 'netbox_data_mover.delete_datamoverconfig'

class DataMoverConfighangeLogView(BaseChangeLogView):
    queryset = DataMoverConfig.objects.all()
    permission_required = 'netbox_data_mover.view_datamoverconfig'

class DataMoverDataSourceListView(generic.ObjectListView):
    queryset = DataMoverDataSource.objects.all()
    table = DataMoverDataSourceTable
    permission_required = 'netbox_data_mover.view_datamoverdatasource'

class DataMoverDataSourceDetailView(BaseObjectView):
    queryset = DataMoverDataSource.objects.all()
    permission_required = 'netbox_data_mover.view_datamoverdatasource'

class DataMoverDataSourceEditView(generic.ObjectEditView):
    queryset = DataMoverDataSource.objects.all()
    form = DataMoverDataSourceForm
    permission_required = 'netbox_data_mover.add_datamoverdatasource'

class DataMoverDataSourceDeleteView(generic.ObjectDeleteView):
    queryset = DataMoverDataSource.objects.all()
    permission_required = 'netbox_data_mover.delete_datamoverdatasource'
    
class DataMoverDataSourceBulkImportView(generic.BulkImportView):
    queryset = DataMoverDataSource.objects.all()
    model_form = DataMoverDataSourceForm
    permission_required = 'netbox_data_mover.add_datamoverdatasource'

class DataMoverDataSourceBulkEditView(generic.BulkEditView):
    queryset = DataMoverDataSource.objects.all()
    filterset = DataMoverDataSourceFilterSet
    table = DataMoverDataSourceTable
    form = DataMoverDataSourceForm
    permission_required = 'netbox_data_mover.change_datamoverdatasource'

class DataMoverDataSourceBulkDeleteView(generic.BulkDeleteView):
    queryset = DataMoverDataSource.objects.all()
    filterset = DataMoverDataSourceFilterSet
    table = DataMoverDataSourceTable
    permission_required = 'netbox_data_mover.delete_datamoverdatasource'

class DataMoverDataSourceChangeLogView(BaseChangeLogView):
    queryset = DataMoverDataSource.objects.all()
    permission_required = 'netbox_data_mover.view_datamoverdatasource'
    
class DataMoverDataSourceCloneView(BaseObjectView):
    def get(self, request, pk):
        # Get the existing object to clone
        instance = get_object_or_404(DataMoverDataSource, pk=pk)

        # Clone the instance by copying fields
        instance.pk = None  # Set pk to None to create a new instance
        instance.name = f"Copy of {instance.name}"  # Modify the name to indicate a copy
        instance.save()

        # Redirect to edit view of the cloned object
        return redirect(reverse('plugins:netbox_data_mover:datamoverconfig_edit', kwargs={'pk': instance.pk}))