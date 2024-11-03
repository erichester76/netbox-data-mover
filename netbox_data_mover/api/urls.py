from netbox.api.routers import OrderedDefaultRouter
from . import views

app_name = 'netbox_data_mover'

router = OrderedDefaultRouter()
router.register(r'datasources', views.DataMoverDataSourceViewSet)
router.register(r'datamoverconfigs', views.DataMoverConfigViewSet)

urlpatterns = router.urls
