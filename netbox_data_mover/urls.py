
from django.urls import path
from . import views

urlpatterns = [
    path('config', views.DataMoverListView.as_view(), name='datamover_list'),
    path('config/add/', views.DataMoverEditView.as_view(), name='datamover_add'),
    path('config/<int:pk>/edit/', views.DataMoverEditView.as_view(), name='datamover_edit'),
    path('config/<int:pk>/delete/', views.DataMoverDeleteView.as_view(), name='datamover_delete'),
    path('config/<int:pk>/', views.DataMoverDetailView.as_view(), name='datamover_detail'),
    path('config/<int:pk>/trigger/', views.DataMoverConfigTriggerJobView.as_view(), name='datamover_trigger_job'),
    path('datasources/', views.DataMoverDataSourceListView.as_view(), name='datamoverdatasource_list'),
    path('datasources/add/', views.DataMoverDataSourceEditView.as_view(), name='datamoverdatasource_add'),
    path('datasources/<int:pk>/edit/', views.DataMoverDataSourceEditView.as_view(), name='datamoverdatasource_edit'),
    path('datasources/<int:pk>/delete/', views.DataMoverDataSourceDeleteView.as_view(), name='datamoverdatasource_delete'),
    path('datasources/<int:pk>/', views.DataMoverDataSourceDetailView.as_view(), name='datamoverdatasource_detail'),
]