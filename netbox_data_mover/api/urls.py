from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataMoverConfigViewSet, DataSourceViewSet

router = DefaultRouter()
router.register(r'configs', DataMoverConfigViewSet)
router.register(r'sources', DataSourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]