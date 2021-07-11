from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = 'HABOUBA.COM'


class LodgingImageAdmin(admin.ModelAdmin):
    list_display = ("title", "price", )


class LodgingImageInline(admin.StackedInline):
    model = LodgingImage
    max_num = 10
    extra = 0


class LodgingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "conditioner", "rating")
    list_display_links = ("id", "title",)
    search_fields = ("title", "price", "rating", "conditioner",)
    list_editable = ("price", "conditioner", "rating")
    list_filter = ("price", "rating", "conditioner",)
    inlines = [LodgingImageInline, ]


# admin.site.register(LodgingImage, LodgingImageAdmin)
admin.site.register(Lodging, LodgingAdmin)
