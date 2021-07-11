from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import CarsModelImage, CarsModel

admin.site.site_header = 'HABOUBA.COM'
admin.site.site_title = 'admin-panel'


class CarsModelImageInline(admin.StackedInline):
    model = CarsModelImage
    max_num = 10
    extra = 0


class CarsModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "year", "category", "car_capacity", "consumption")
    list_display_links = ("id", "title",)
    search_fields = ("title", "price", "year", "category", "car_capacity", "consumption")
    list_editable = ("price", "year", "category", "car_capacity", "consumption")
    list_filter = ("title", "price", "category", "car_capacity", "consumption")
    inlines = [CarsModelImageInline, ]


# admin.site.register(LodgingImage, LodgingImageAdmin)
admin.site.register(CarsModel, CarsModelAdmin)
