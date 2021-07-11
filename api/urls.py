from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('lodging', views.LodgingViewSet, basename='Home')
router.register('lodging-image', views.LodgingImageViewSet, basename='ImageGalery')
router.register('cars-model', views.CarsModelViewSet, basename='CarsModel')
router.register('cars-model-image', views.CarsModelImageViewSet, basename='CarsModelImage')
router.register('driver-profile', views.DriverProfileViewSet, basename='DriverProfile')
router.register('instruments', views.InstrumentsViewSet, basename='instruments')
router.register('category-instruments', views.CategoryInstrumentsViewSet, basename='category instruments')
router.register('image-instrument', views.ImageInstrumentViewSet, basename='image instruments')

urlpatterns = [
    path('', include(router.urls)),
]