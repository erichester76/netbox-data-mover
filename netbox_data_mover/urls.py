
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DataMoverListView.as_view(), name='datamover_list'),
    path('add/', views.DataMoverEditView.as_view(), name='datamover_add'),
    path('<int:pk>/edit/', views.DataMoverEditView.as_view(), name='datamover_edit'),
    path('<int:pk>/delete/', views.DataMoverDeleteView.as_view(), name='datamover_delete'),
    path('<int:pk>/', views.DataMoverDetailView.as_view(), name='datamover_detail'),
    path('<int:pk>/trigger/', views.DataMoverConfigTriggerJobView.as_view(), name='datamover_trigger_job'),
    path('datasources/', views.DataSourceListView.as_view(), name='datasource_list'),
    path('datasources/add/', views.DataSourceEditView.as_view(), name='datasource_add'),
    path('datasources/<int:pk>/edit/', views.DataSourceEditView.as_view(), name='datasource_edit'),
    path('datasources/<int:pk>/delete/', views.DataSourceDeleteView.as_view(), name='datasource_delete'),
]