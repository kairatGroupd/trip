import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models


# Create your models here.
from django.utils.safestring import mark_safe


def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image


YEAR_CHOICES = []
for r in range(1900, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((r, r))

CATEGORY_CARS = (
    ('s', 'Sedan'),
    ('p', 'Pickup'),
    ('l', 'SUV'),
    ('ps', 'Premium SUV'),
    ('mb', 'Minibus'),
)

CAR_CAPACITY = (
    ('S', '2-4'),
    ('M', '4-6'),
    ('L', '6-8'),
)


class CarsModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='Model car')
    year = models.IntegerField('year', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    category = models.CharField(max_length=2, choices=CATEGORY_CARS, null=True, )
    car_capacity = models.CharField(max_length=1, choices=CAR_CAPACITY, null=True, )
    consumption = models.IntegerField(default=1,
                                      validators=[
                                          MaxValueValidator(30),
                                          MinValueValidator(5)
                                      ])
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price')

    def __str__(self):
        return self.title


class CarsModelImage(models.Model):
    image = models.ImageField(upload_to='media')
    сars_id = models.ForeignKey(CarsModel, on_delete=models.CASCADE, null=True, related_name="images")

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

