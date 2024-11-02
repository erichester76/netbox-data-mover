
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DataMoverConfigView, name='datamover_detail'),
    path('create/', views.create_view, name='datamover_adde'),
    path('<int:pk>/', views.detail_view, name='datamover_view'),
    path('<int:pk>/trigger/', views.trigger_job_view, name='datamover_trigger_job'),
]
