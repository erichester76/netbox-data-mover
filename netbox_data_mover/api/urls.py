from rest_framework.routers import DefaultRouter
from . import views

app_name = 'netbox_data_mover_api'

router = DefaultRouter()
router.register(r'datamoverdatasources', views.DataMoverDataSourceViewSet, basename='datamoverdatasource')
router.register(r'datamoverconfigs', views.DataMoverConfigViewSet, basename='datamoverconfig')

urlpatterns = router.urls
