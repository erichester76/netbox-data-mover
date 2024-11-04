from netbox.api.routers import NetBoxRouter
from django.urls import path
from . import views

router = NetBoxRouter()
router.register(r'datasources', views.DataMoverDataSourceViewSet)
router.register(r'datamoverconfigs', views.DataMoverConfigViewSet)

urlpatterns = router.urls + [
    path('get_ds_fields/', views.get_fields, name='datasource_fields'),
]
