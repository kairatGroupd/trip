from io import BytesIO
from django.core.files import File
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import PIL
from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust, ResizeToFill


# Create your models here.
def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image


# здесь константа для категорий жилья
LODGING_CATEGORY = (
    ('h', 'Hotel'),
    ('y', 'Yurts'),
    ('a', 'Apartments'),
    ('o', 'Other'),
)


# здесь модель жилья
class Lodging(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title', db_index=True)
    count_room = models.SmallIntegerField(verbose_name='Number of rooms')
    conditioner = models.BooleanField(default=True, verbose_name='The presence of an air conditioner')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price')
    category = models.CharField(max_length=1, choices=LODGING_CATEGORY, null=True,)
    rating = models.IntegerField(default=1,
                                 validators=[
                                     MaxValueValidator(10),
                                     MinValueValidator(1)
                                 ])

    def __str__(self):
        return self.title


# здесь модель изоброжений
class LodgingImage(models.Model):
    image = models.ImageField(upload_to='media')  # здесь укажите куда сохранять изображения
    lodging = models.ForeignKey(Lodging, on_delete=models.CASCADE, null=True, related_name="images")

    # функция для сжатия без потерь
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)