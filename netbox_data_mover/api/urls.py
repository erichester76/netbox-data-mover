from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_data_mover'

router = NetBoxRouter()
router.register(r'datasources', views.DataMoverDataSourceViewSet)
router.register(r'datamoverconfigs', views.DataMoverConfigViewSet)

urlpatterns = router.urls
