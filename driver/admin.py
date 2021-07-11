from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe
from driver.models import DriverProfile

admin.site.site_header = 'HABOUBA.COM'
admin.site.site_title = 'admin-panel'


class DriverProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "patronymic", "age_driver", "experience", "languages", "languages2", "languages3", "rating", "price", "get_html_image")
    list_display_links = ("id", "first_name", "last_name", "patronymic",)
    search_fields = ("first_name", "last_name", "patronymic", "age_driver", "experience", "languages", "rating")
    list_editable = ("age_driver", "experience", "languages", "languages2", "languages3", "rating")
    list_filter = ("id", "first_name", "last_name", "patronymic", "age_driver", "experience", "languages", "rating")
    fields = ("first_name", "last_name", "patronymic", "age_driver", "experience", "languages", "languages2", "languages3",  "rating", "price", "image", "get_html_image",)
    readonly_fields = ("get_html_image", )

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50")

    get_html_image.short_description = "Images"


admin.site.register(DriverProfile, DriverProfileAdmin)
