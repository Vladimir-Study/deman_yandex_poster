from django.db import models
from django.conf import settings
from tinymce import models as tinymce_model


class Place(models.Model):
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    short_description = models.TextField(verbose_name="Краткое описание", blank=True)
    long_description = tinymce_model.HTMLField(verbose_name="Описание", blank=True)
    coord_lng = models.FloatField(verbose_name="Долгота")
    coord_lat = models.FloatField(verbose_name="Широта")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(
        "Place", on_delete=models.CASCADE, related_name="image_place"
    )
    photo = models.ImageField(upload_to="img/", verbose_name="Фото")
    position = models.PositiveIntegerField(verbose_name="Позиция", default=0)

    class Meta:
        ordering = ["position"]
        indexes = [models.Index(fields=["position"])]

    def __str__(self):
        return f"{self.id} {self.place}"

    @property
    def get_absolute_image_url(self):
        return f"{settings.MEDIA_URL}{self.photo}"
