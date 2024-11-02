
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DataMoverListView.as_view(), name='datamover_list'),
    path('add/', views.DataMoverEditView.as_view(), name='datamover_add'),
    path('<int:pk>/edit/', views.DataMoverEditView.as_view(), name='datamover_edit'),
    path('<int:pk>/delete/', views.DataMoverDeleteView.as_view(), name='datamover_delete'),
    path('<int:pk>/', views.DataMoverDetailView.as_view(), name='datamover_detail'),
    path('<int:pk>/trigger/', views.DataMoverConfigTriggerJobView.as_view(), name='datamover_trigger_job'),
    path('datamoverdatasources/', views.DataMoverDataSourceListView.as_view(), name='datamoverdatasource_list'),
    path('datamoverdatasources/add/', views.DataMoverDataSourceEditView.as_view(), name='datamoverdatasource_add'),
    path('datamoverdatasources/<int:pk>/edit/', views.DataMoverDataSourceEditView.as_view(), name='datamoverdatasource_edit'),
    path('datamoverdatasources/<int:pk>/delete/', views.DataMoverDataSourceDeleteView.as_view(), name='datamoverdatasource_delete'),
]