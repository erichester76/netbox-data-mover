from netbox.views import generic
from .models import DataMoverConfig, DataMoverDataSource
from .forms import DataMoverConfigForm, DataMoverDataSourceForm
from .tables import DataMoverConfigTable, DataMoverDataSourceTable

class DataMoverConfigListView(generic.ObjectListView):
    queryset = DataMoverConfig.objects.all()
    table = DataMoverConfigTable
    permission_required = 'netbox_data_mover.view_datamoverconfig'

class DataMoverConfigView(generic.ObjectView):
    queryset = DataMoverConfig.objects.all()
    permission_required = 'netbox_data_mover.view_datamoverconfig'

class DataMoverConfigEditView(generic.ObjectEditView):
    queryset = DataMoverConfig.objects.all()
    form = DataMoverConfigForm
    permission_required = 'netbox_data_mover.add_datamoverconfig'

class DataMoverConfigDeleteView(generic.ObjectDeleteView):
    queryset = DataMoverConfig.objects.all()
    permission_required = 'netbox_data_mover.delete_datamoverconfig'

class DataMoverDataSourceListView(generic.ObjectListView):
    queryset = DataMoverDataSource.objects.all()
    table = DataMoverDataSourceTable
    permission_required = 'netbox_data_mover.view_datamoverdatasource'

class DataMoverDataSourceView(generic.ObjectView):
    queryset = DataMoverDataSource.objects.all()
    permission_required = 'netbox_data_mover.view_datamoverdatasource'

class DataMoverDataSourceEditView(generic.ObjectEditView):
    queryset = DataMoverDataSource.objects.all()
    form = DataMoverDataSourceForm
    permission_required = 'netbox_data_mover.add_datamoverdatasource'

class DataMoverDataSourceDeleteView(generic.ObjectDeleteView):
    queryset = DataMoverDataSource.objects.all()
    permission_required = 'netbox_data_mover.delete_datamoverdatasource'
