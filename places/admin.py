from django.contrib import admin
from django.utils.html import format_html, mark_safe
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin

from .models import PlaceImage, Place


class PlaceImagesAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    extra = 1
    readonly_fields = [
        "headshot_image",
    ]

    def headshot_image(self, obj):
        return format_html(mark_safe(f"<img src='{obj.url_img.url}' width='150'/>"))


@admin.register(Place)
class AdminPlace(SortableAdminBase, admin.ModelAdmin):
    empty_value_display = "-empty-"
    inlines = [
        PlaceImagesAdmin,
    ]
