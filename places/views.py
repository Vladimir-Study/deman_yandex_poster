from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Place, PlaceImage

places = get_list_or_404(Place)

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
                "detailsUrl": reverse_lazy("place_url", args=[place.id]),
            },
        }
    )

places = {
    "type": "FeatureCollection",
    "features": features,
}


def index_view(request):
    return render(
        request,
        "places/index.html",
        context={"places": places},
    )


def places_view(request, pk):
    place = get_object_or_404(Place, pk=pk)
    place_images = get_list_or_404(PlaceImage, place__id=pk)
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
        response_body, safe=False, json_dumps_params={"ensure_ascii": False}
    )
