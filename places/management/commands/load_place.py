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
        if not urls:
            return
        for url in urls:
            try:
                raw_data_place = requests.get(url)
                if raw_data_place.status_code != 200:
                    return
                raw_data_place = raw_data_place.json()
                new_place = Place.objects.get_or_create(
                    title=raw_data_place["title"],
                    short_description=raw_data_place.get("description_short", ""),
                    long_description=raw_data_place.get("description_long", ""),
                    coord_lng=raw_data_place["coordinates"]["lng"],
                    coord_lat=raw_data_place["coordinates"]["lat"],
                )
                if new_place[1]:
                    self.save_image(raw_data_place.get("imgs", []), new_place[0])
                else:
                    print("Place was added!")
            except requests.exceptions.HTTPError as Exc:
                print(f"Exception {Exc} on get the place {url}")
                continue
            except requests.exceptions.ConnectionError as Exc:
                print(f"Exception {Exc} on get the place {url}")
                continue

    def save_image(self, images: list, model: Place):
        if not images:
            return
        for image in images:
            name = image.split("/")[-1]
            try:
                payload_image_data = requests.get(image)
                if payload_image_data.status_code != 200:
                    return
                PlaceImage(place=model).photo.save(
                    name, ContentFile(payload_image_data.content), save=True
                )
            except requests.exceptions.HTTPError as Exc:
                print(f"Exception {Exc} on get the image {image}")
                continue
            except requests.exceptions.ConnectionError as Exc:
                print(f"Exception {Exc} on get the image {image}")
                continue
