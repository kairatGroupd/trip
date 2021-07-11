from urllib import response
from rest_framework.generics import ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from django.conf import settings
from home.models import *
from .serializers import *
from car.models import *
from driver.models import DriverProfile

from instruments.models import InstrumentModel, CategoryInstruments, ImageInstrument


class LodgingViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LodgingSerializer
    queryset = Lodging.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['category', 'count_room', 'conditioner', 'rating']


class LodgingImageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LodgingImageSerializer
    queryset = LodgingImage.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['lodging']


# CarsModel
class CarsModelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CarsModelSerializer
    queryset = CarsModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['category']


class CarsModelImageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CarsModelImageSerializer
    queryset = CarsModelImage.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['сars_id']


class DriverProfileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DriverProfileSerializer
    queryset = DriverProfile.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["id", "first_name", "last_name", "patronymic", "age_driver", "experience", "languages", "languages2", "languages3", "rating", "price",]


class InstrumentsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = InstrumentsSerializer
    queryset = InstrumentModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['item_name', 'descriptions', 'category', ]


class CategoryInstrumentsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategoryInstrumentsSerializer
    queryset = CategoryInstruments.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['name', ]


class ImageInstrumentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ImageInstrumentSerializer
    queryset = ImageInstrument.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['instrument', ]