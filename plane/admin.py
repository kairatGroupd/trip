from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin    

# Register your models here.
admin.site.site_header = 'HABOUBA.COM'
admin.site.site_title = 'admin-panel'


class PlannedTourImageInline(admin.StackedInline):
    model = PlannedTourImage
    max_num = 10
    extra = 0


class PlannedTourAdmin(admin.ModelAdmin):
    list_display = ("id", "name_tour", "numbers_of_day", )
    list_display_links = ("id", "name_tour",)
    search_fields = ("name_tour", "numbers_of_day", )
    list_editable = ()
    list_filter = ("name_tour", "category", "numbers_of_day",)
    inlines = [PlannedTourImageInline, ]


admin.site.register(PlannedTour, PlannedTourAdmin)