from django.shortcuts import render
from django.http import JsonResponse
from .models import Place, PlaceImage

import json

# moscow_legends = Place.objects.get(pk=1)
# roofs_24 = Place.objects.get(pk=2)
places = Place.objects.all()

features = []
for place in places:
    features.append(
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.show_coord_lng, place.show_coord_lat],
            },
            "properties": {
                "title": place.short_title,
                "placeId": place.id,
                "detailsUrl": None,
            },
        }
    )

places = {
    "type": "FeatureCollection",
    "features": features,
    # "features": [
    #     {
    #         "type": "Feature",
    #         "geometry": {"type": "Point", "coordinates": [37.62, 55.793676]},
    #         "properties": {
    #             "title": moscow_legends.short_title,
    #             "placeId": moscow_legends.id,
    #             "detailsUrl": None,
    #         },
    #     },
    #     {
    #         "type": "Feature",
    #         "geometry": {"type": "Point", "coordinates": [37.64, 55.753676]},
    #         "properties": {
    #             "title": roofs_24.short_title,
    #             "placeId": roofs_24.id,
    #             "detailsUrl": None,
    #         },
    #     },
    # ],
}


def index(request):
    return render(
        request,
        "places/index.html",
        context={"places": places},
    )


def places(request, pk):
    place = Place.objects.get(pk=pk)
    place_images = PlaceImage.objects.filter(place__id=pk)
    imgs = [img.get_absolute_image_url for img in place_images]
    response_body = {
        "title": place.title,
        "imgs": imgs,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.coord_lng,
            "lat": place.coord_lat,
        },
    }
    return JsonResponse(
        response_body,
        safe=False,
        json_dumps_params={'ensure_ascii': False}
    )
