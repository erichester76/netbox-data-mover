from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataMoverConfigViewSet, DataSourceViewSet

urlpatterns = [
    path('datasources/', views.DataSourceListAPIView.as_view(), name='datasource_list'),
    path('datamoverconfigs/', views.DataMoverConfigListAPIView.as_view(), name='datamoverconfig_list'),
    path('datamoverconfigs/<int:pk>/', views.DataMoverConfigDetailAPIView.as_view(), name='datamoverconfig_detail'),
]