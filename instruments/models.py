from io import BytesIO

from PIL import Image
from django.core.files import File
from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.


def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image


class CategoryInstruments(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")


class InstrumentModel(models.Model):
    item_name = models.CharField(max_length=50, verbose_name='Item name')
    descriptions = models.TextField(verbose_name='Description')
    category = models.ForeignKey(CategoryInstruments, on_delete=models.CASCADE, verbose_name='Category')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price')


class ImageInstrument(models.Model):
    image = models.ImageField(upload_to='media')
    instrument = models.ForeignKey(InstrumentModel, on_delete=models.CASCADE, null=True, related_name="images")

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)
