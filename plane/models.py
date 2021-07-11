from django.db import models

# Create your models here.
from car.models import CarsModel
from home.models import Lodging
from io import BytesIO
from PIL import Image
from django.core.files import File


def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image

NUMBER_OF_DAYS = (
    ('4', '1-4'),
    ('8', '1-8'),
    ('10', '1-10'),
    ('14', '1-14'),
)

CATEGORY_TOUR = (
    ('', ''),
    ('', ''),
    ('', ''),
)


class PlannedTour(models.Model):
    name_tour = models.CharField(max_length=50, verbose_name='Name tour')
    description = models.TextField(verbose_name='Description')
    cars = models.ForeignKey(CarsModel, on_delete=models.CASCADE, verbose_name='Car', null=True, blank=True)
    home = models.ForeignKey(Lodging, on_delete=models.CASCADE, verbose_name='Home', null=True, blank=True)
    category = models.CharField(max_length=2, choices=CATEGORY_TOUR, null=True, blank=True)
    numbers_of_day = models.CharField(max_length=2, choices=NUMBER_OF_DAYS, null=True, blank=True)
    #  price = model.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price', null=True, blank=True)

class PlannedTourImage(models.Model):
    image = models.ImageField(upload_to='media')
    key = models.ForeignKey(PlannedTour, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

