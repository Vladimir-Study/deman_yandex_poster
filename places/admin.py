from django.contrib import admin
from django.utils.html import format_html, mark_safe
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin

from places.models import PlaceImage, Place


class SubtablesPlaceImages(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    extra = 1
    readonly_fields = [
        "headshot_image",
    ]

    def headshot_image(self, obj):
        src_html = f"src='{obj.photo.url}'"
        img_style_html = "style='max-width: 150px; max-height:150px'"
        return format_html(f"<img {mark_safe(src_html)} {img_style_html}/>")


@admin.register(Place)
class AdminPlace(SortableAdminBase, admin.ModelAdmin):
    empty_value_display = "-empty-"
    inlines = [
        SubtablesPlaceImages,
    ]


@admin.register(PlaceImage)
class AdminPlaceImage(admin.ModelAdmin):
    raw_id_fields = ("place",)
