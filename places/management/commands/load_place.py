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
                place_data = requests.get(url).json()
                new_place = Place.objects.create(
                    title=place_data.get("title"),
                    description_short=place_data.get("description_short"),
                    description_long=place_data.get("description_long"),
                    coord_lng=place_data.get("coordinates").get("lng"),
                    coord_lat=place_data.get("coordinates").get("lat"),
                )
                self.save_image(place_data.get("imgs"), new_place)

    def save_image(self, images: list, model: Place):
        if images:
            for image in images:
                name = image.split("/")[-1]
                place_data = requests.get(image)
                place_image = ContentFile(place_data.content)
                img = PlaceImage(place=model)
                img.photo.save(name, place_image, save=True)
