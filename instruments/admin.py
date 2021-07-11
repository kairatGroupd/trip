from django.contrib import admin

from .models import *

# Register your models here.
admin.site.site_header = 'HABOUBA.COM'


# class InstrumentModelAdmin(admin.ModelAdmin):
#     list_display = ("title", "price", )


class ImageInstrumentInline(admin.StackedInline):
    model = ImageInstrument
    max_num = 10
    extra = 0


class InstrumentModelAdmin(admin.ModelAdmin):
    list_display = ("id", "item_name", "descriptions", "price", "category")
    list_display_links = ("id", "item_name",)
    search_fields = ("title", "price", "category", )
    list_editable = ("price", "category", )
    list_filter = ("price", "category",)
    inlines = [ImageInstrumentInline, ]


admin.site.register(CategoryInstruments, )
admin.site.register(InstrumentModel, InstrumentModelAdmin)
