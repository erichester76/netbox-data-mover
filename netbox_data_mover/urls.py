from django.urls import path
from . import views

app_name = 'netbox_data_mover'

urlpatterns = [
    # DataMoverConfig URLs
    path('datamoverconfigs/', views.DataMoverConfigListView.as_view(), name='datamoverconfig_list'),
    path('datamoverconfigs/add/', views.DataMoverConfigEditView.as_view(), name='datamoverconfig_add'),
    path('datamoverconfigs/import/', views.DataMoverConfigBulkImportView.as_view(), name='datamoverconfig_import'),
    path('datamoverconfigs/edit/', views.DataMoverConfigBulkEditView.as_view(), name='datamoverconfig_bulk_edit'),
    path('datamoverconfigs/delete/', views.DataMoverConfigBulkDeleteView.as_view(), name='datamoverconfig_bulk_delete'),
    path('datamoverconfigs/<int:pk>/', views.DataMoverConfigDetailView.as_view(), name='datamoverconfig_detail'),
    path('datamoverconfigs/<int:pk>/edit/', views.DataMoverConfigEditView.as_view(), name='datamoverconfig_edit'),
    path('datamoverconfigs/<int:pk>/delete/', views.DataMoverConfigDeleteView.as_view(), name='datamoverconfig_delete'),

    # DataMoverDataSource URLs
    path('datamoverdatasources/', views.DataMoverDataSourceListView.as_view(), name='datamoverdatasource_list'),
    path('datamoverdatasources/add/', views.DataMoverDataSourceEditView.as_view(), name='datamoverdatasource_add'),
    path('datamoverdatasources/import/', views.DataMoverDataSourceBulkImportView.as_view(), name='datamoverdatasource_import'),
    path('datamoverdatasources/edit/', views.DataMoverDataSourceBulkEditView.as_view(), name='datamoverdatasource_bulk_edit'),
    path('datamoverdatasources/delete/', views.DataMoverDataSourceBulkDeleteView.as_view(), name='datamoverdatasource_bulk_delete'),
    path('datamoverdatasources/<int:pk>/', views.DataMoverDataSourceDetailView.as_view(), name='datamoverdatasource_detail'),
    path('datamoverdatasources/<int:pk>/edit/', views.DataMoverDataSourceEditView.as_view(), name='datamoverdatasource_edit'),
    path('datamoverdatasources/<int:pk>/delete/', views.DataMoverDataSourceDeleteView.as_view(), name='datamoverdatasource_delete'),
]
