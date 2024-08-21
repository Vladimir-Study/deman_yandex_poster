from django.contrib import admin

from .models import PlaceImage, Place


@admin.register(Place, PlaceImage)
class AdminPlace(admin.ModelAdmin):
    empty_value_display = "-empty-"
