from rest_framework import viewsets
from ..models import DataMoverDataSource, DataMoverConfig
from ..filtersets import DataMoverConfigFilterSet, DataMoverDataSourceFilterSet 
from .serializers import DataMoverDataSourceSerializer, DataMoverConfigSerializer, DataSourceFieldsSerializer
from netbox.api.viewsets import NetBoxModelViewSet
from rest_framework.response import Response

class DataMoverDataSourceViewSet(NetBoxModelViewSet):
    queryset = DataMoverDataSource.objects.all()
    serializer_class = DataMoverDataSourceSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        type_param = request.query_params.get('type', None)

        if type_param == 'endpoints':
            if instance.endpoints:
                # Fake Serializer
                endpoints = instance.endpoints.split(',')
                endpoint_data = []

                for index, endpoint in enumerate(endpoints):
                    endpoint_data.append({
                        "id": index,
                        "url": f"https://{request.get_host()}/api/plugins/netbox_data_mover/endpoints/{index}/",
                        "display": endpoint.strip(),
                        "name": endpoint.strip(),
                        "slug": endpoint.strip().replace(" ", "-").lower(),
                        "description": ""
                    })

                # Response formatted in a similar way to the one provided in your example
                return Response({
                    "count": len(endpoint_data),
                    "next": None,
                    "previous": None,
                    "results": endpoint_data
                })

            return Response({"count": 0, "next": None, "previous": None, "results": []})

        # Default behavior: return the serialized datasource instance
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class DataMoverConfigViewSet(NetBoxModelViewSet):
    queryset = DataMoverConfig.objects.all()
    serializer_class = DataMoverConfigSerializer
    filterset = DataMoverConfigFilterSet

class DataSourceFieldsView(NetBoxModelViewSet):
    queryset = DataMoverDataSource.objects.all()

    @action(detail=True, methods=['get'], url_path='get_fields/(?P<endpoint>[^/.]+)')
    def get_fields(self, request, pk=None, endpoint=None):
        try:
            datasource = self.get_object()
            fields = get_available_fields(datasource, endpoint)
            return Response({'fields': fields})
        except DataMoverDataSource.DoesNotExist:
            return Response({"error": "Data source not found."}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=400)