from django.db import models
from where_to_go import settings
from tinymce import models as tinymce_model


class Place(models.Model):
    title = models.CharField(max_length=250)
    description_short = models.CharField(max_length=500)
    description_long = tinymce_model.HTMLField()
    coord_lng = models.FloatField()
    coord_lat = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]


class PlaceImage(models.Model):
    place = models.ForeignKey("Place", on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to="img/")
    position = models.PositiveIntegerField("Позиция", default=0)

    @property
    def get_absolute_image_url(self):
        return f"{settings.MEDIA_URL}{self.url_img}"

    def __str__(self):
        return f"{self.id} {self.place}"

    class Meta:
        ordering = ["position"]
        indexes = [models.Index(fields=["position"])]
