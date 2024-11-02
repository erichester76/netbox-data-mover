
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataMoverConfigViewSet

router = DefaultRouter()
router.register(r'configs', DataMoverConfigViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
