from netbox.api.routers import NetBoxRouter
from django.urls import path
from . import views

router = NetBoxRouter()
router.register(r'datasources', views.DataMoverDataSourceViewSet)
router.register(r'datamoverconfigs', views.DataMoverConfigViewSet)

urlpatterns = router.urls + [
  path('datasources/get_fields/<int:datasource_id>/<str:endpoint>', views.DataSourceFieldsView, name='datasource_fields')
]
