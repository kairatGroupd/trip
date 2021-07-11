from io import BytesIO

from PIL import Image
from django.core.files import File
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here

def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image


EXPERIENCE = (
    ('1', 'up to 1 year'),
    ('3', 'from 1 to 3 years'),
    ('5', 'from 3 to 5 years'),
)

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
    ('ar', 'Arabic'),
    ('kg', 'Kyrgyz'),
)


class DriverProfile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, verbose_name='Last name')
    patronymic = models.CharField(max_length=50, verbose_name='Patronymic')
    age_driver = models.SmallIntegerField(verbose_name='age')
    experience = models.CharField(max_length=1, choices=EXPERIENCE, null=True, )
    languages = models.CharField(max_length=2, choices=LANGUAGES, null=True, blank=True)
    languages2 = models.CharField(max_length=2, choices=LANGUAGES, null=True, blank=True)
    languages3 = models.CharField(max_length=2, choices=LANGUAGES, null=True, blank=True)
    rating = models.IntegerField(default=1,
                                 validators=[
                                     MaxValueValidator(10),
                                     MinValueValidator(1)
                                 ])
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price')
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)
