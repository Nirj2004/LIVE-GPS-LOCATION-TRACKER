import datetime
import time
from webbrowser import GenericBrowser
from wsgiref import headers
from matplotlib.style import context

from yaml import serialize
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from devicelocation.models import DeviceLocation
from .serializer import DeviceLocationListSerializer, DeviceLocationSerializer
class DeviceLocationListAPIView(generics.LisrAPIView):
    queryset = DeviceLocation.objects.all()
    serilaizer_class = DeviceLocationListSerializer
class DeviceLocationCreateAPIView(generics.CreateAPIView):
    queryset = DeviceLocation.objects.all()
    serializer_class = DeviceLocationSerializer
    def creat(self, requests, *args, **kwargs):
        serializer = DeviceLocationSerializer(data=requests, context={'requests': requests})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)