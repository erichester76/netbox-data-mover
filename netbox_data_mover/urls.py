
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DataMoverListView, name='datamover_list'),
    path('/add', views.DataMoverEditView, name='datamover_add'),
    path('<int:pk>/edit', views.DataMoverEditView, name='datamover_edit'),
    path('<int:pk>/delete', views.DataMoverDeleteView, name='datamover_delete'),
    path('<int:pk>/', views.DataMoverView, name='datamover_detail'),
    path('<int:pk>/trigger/', views.trigger_job_view, name='datamover_trigger_job'),
]
