from rest_framework import serializers

from home.models import Lodging, LodgingImage

from car.models import CarsModel, CarsModelImage
from driver.models import DriverProfile

# Lodging model
from instruments.models import InstrumentModel, CategoryInstruments, ImageInstrument


class LodgingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lodging
        fields = '__all__'
        depth = 1


class LodgingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LodgingImage
        fields = '__all__'


# Cars Model
class CarsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsModel
        fields = '__all__'
        depth = 1


class CarsModelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsModelImage
        fields = '__all__'


# DriverProfile
class DriverProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverProfile
        fields = '__all__'
        depth = 1


# Instruments
class InstrumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstrumentModel
        fields = '__all__'
        depth = 1


class CategoryInstrumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryInstruments
        fields = '__all__'
        depth = 1


class ImageInstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageInstrument
        fields = '__all__'
        depth = 1