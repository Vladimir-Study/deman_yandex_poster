from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=250)
    description_short = models.CharField(max_length=500)
    description_long = models.TextField()
    coord_lng = models.FloatField()
    coord_lat = models.FloatField()

    def __str__(self):
        return self.title

class PlaceImage(models.Model):
    place = models.ForeignKey('Place', on_delete=models.CASCADE, null=True)
    url_img = models.URLField()

    def __str__(self):
        return self.place