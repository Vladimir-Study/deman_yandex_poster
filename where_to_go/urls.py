from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from places.views import index_view, places_view


urlpatterns = [
    path("", index_view),
    path("places/<int:pk>", places_view, name="place_url"),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
