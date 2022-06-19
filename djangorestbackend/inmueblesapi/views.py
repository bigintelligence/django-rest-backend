import os

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from .models import Inmueble
from .serializers import InmuebleSerializer
from .utils import CsvFileInmueblesSaver
import logging

logger = logging.getLogger(__name__)
FILE_PATH = os.path.join(settings.BASE_DIR, '../', 'assets.csv')


class InmuebleViewSet(viewsets.ModelViewSet):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer


class UploadCSVViewSet(APIView):
    """view to handle the first load data"""
    def get(self, request, format=None):
        try:
            # class to handle the file operations
            csv_saver = CsvFileInmueblesSaver(FILE_PATH)
            csv_saver.read_save_file()
            if csv_saver.response['upload_state'] == 'Ok':
                return Response(csv_saver.response, status=200)
            else:
                return Response(csv_saver.response, status=500)

        except Exception as e:
            logger.exception(e)
            return Response({'upload_state': 'Error'}, status=500)