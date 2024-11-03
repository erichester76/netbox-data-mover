from netbox.api.routers import NetBoxRouter
from . import views

router = NetBoxRouter()
router.register(r'datasources', views.DataMoverDataSourceViewSet)
router.register(r'datamoverconfigs', views.DataMoverConfigViewSet)

urlpatterns = router.urls
