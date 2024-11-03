from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'datasources', views.DataMoverDataSourceViewSet, basename='datamoverdatasource')
router.register(r'datamoverconfigs', views.DataMoverConfigViewSet, basename='datamoverconfig')

urlpatterns = router.urls
