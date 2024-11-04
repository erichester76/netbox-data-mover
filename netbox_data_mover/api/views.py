from rest_framework import viewsets
from ..models import DataMoverDataSource, DataMoverConfig
from ..filtersets import DataMoverConfigFilterSet, DataMoverDataSourceFilterSet 
from .serializers import DataMoverDataSourceSerializer, DataMoverConfigSerializer
from netbox.api.viewsets import NetBoxModelViewSet
from django.http import JsonResponse
from ..api_utils import DataSourceAuth
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound

class DataMoverDataSourceViewSet(NetBoxModelViewSet):
    queryset = DataMoverDataSource.objects.all()
    serializer_class = DataMoverDataSourceSerializer
    filterset = DataMoverDataSourceFilterSet

class DataMoverConfigViewSet(NetBoxModelViewSet):
    queryset = DataMoverConfig.objects.all()
    serializer_class = DataMoverConfigSerializer
    filterset = DataMoverConfigFilterSet


class DataSourceFieldsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, datasource_id, format=None):
        datasource_id = request.GET.get('datasource_id')

        try:
            # Retrieve DataMoverDataSource instance
            datasource = DataMoverDataSource.objects.get(pk=datasource_id)

            # Authenticate to the data source
            client = DataSourceAuth.authenticate(datasource)

            # Use the fetch_data method to get the data
            data = DataSourceAuth.fetch_data(datasource, client)

            # Extract fields from the first row of the data
            if isinstance(data, list) and len(data) > 0:
                first_row = data[0]
            elif isinstance(data, dict):
                first_row = data
            else:
                return Response({'error': 'Unexpected data format returned by fetch function.'}, status=400)

            # Extract field names from the first row
            fields = list(first_row.keys()) if isinstance(first_row, dict) else dir(first_row)

            return Response({'fields': fields})

        except DataMoverDataSource.DoesNotExist:
            return Response({'error': 'Data source not found.'}, status=404)
        except ImportError as e:
            return Response({'error': str(e)}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)