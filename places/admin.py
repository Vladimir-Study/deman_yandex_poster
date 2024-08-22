from django.contrib import admin
from django.utils.html import format_html, mark_safe

from .models import PlaceImage, Place


class PlaceImagesAdmin(admin.TabularInline):
    model = PlaceImage
    readonly_fields = [
        "headshot_image",
    ]

    def headshot_image(self, obj):
        return format_html(mark_safe(f"<img src='{obj.url_img.url}' width='150'/>"))


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    empty_value_display = "-empty-"
    inlines = [
        PlaceImagesAdmin,
    ]
