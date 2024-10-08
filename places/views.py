from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy

from places.models import Place, PlaceImage


def index_view(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.coord_lng, place.coord_lat],
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse_lazy("place_url", args=[place.id]),
                },
            }
        )

    places = {
        "type": "FeatureCollection",
        "features": features,
    }
    return render(
        request,
        "places/index.html",
        context={"places": places},
    )


def places_view(request, pk):
    place_images = PlaceImage.objects.select_related("place").filter(place__id=pk)
    imgs = [img.get_absolute_image_url for img in place_images]
    response_body = {
        "title": place_images[0].place.title,
        "imgs": imgs,
        "description_short": place_images[0].place.short_description,
        "description_long": place_images[0].place.long_description,
        "coordinates": {
            "lng": place_images[0].place.coord_lng,
            "lat": place_images[0].place.coord_lat,
        },
    }
    return JsonResponse(
        response_body, safe=False, json_dumps_params={"ensure_ascii": False}
    )
