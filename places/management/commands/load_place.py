from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from places.models import Place, PlaceImage

import requests


class Command(BaseCommand):
    help = "Command for add data tothe data base"

    def add_arguments(self, parser):
        parser.add_argument("urls", type=str, action="append", nargs="+")

    def handle(self, *args, **options):
        urls = options.get("urls")[0]
        if urls:
            for url in urls:
                raw_data_place = requests.get(url).json()
                new_place = Place.objects.create(
                    title=raw_data_place.get("title"),
                    short_description=raw_data_place.get("description_short"),
                    long_description=raw_data_place.get("description_long"),
                    coord_lng=raw_data_place.get("coordinates").get("lng"),
                    coord_lat=raw_data_place.get("coordinates").get("lat"),
                )
                self.save_image(raw_data_place.get("imgs"), new_place)

    def save_image(self, images: list, model: Place):
        if images:
            for image in images:
                name = image.split("/")[-1]
                payload_image_data = requests.get(image)
                image_place = ContentFile(payload_image_data.content)
                img = PlaceImage(place=model)
                img.photo.save(name, image_place, save=True)
