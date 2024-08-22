from django.contrib import admin

from .models import PlaceImage, Place


class PlaceImagesAdmin(admin.TabularInline):
    model = PlaceImage


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    empty_value_display = "-empty-"
    inlines = [
        PlaceImagesAdmin,
    ]
