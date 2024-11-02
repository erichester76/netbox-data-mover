
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('create/', views.create_view, name='create'),
    path('<int:pk>/', views.detail_view, name='detail'),
    path('<int:pk>/trigger/', views.trigger_job_view, name='trigger_job'),
]
