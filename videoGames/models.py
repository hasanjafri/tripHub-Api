from django.db import models


# Create your models here.
class VideoGamePOI(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    mean_rating = models.FloatField()

    def __str__(self):
        return self.name


class Rating(models.Model):
    value = models.IntegerField()
    comment = models.CharField(max_length=300)
    video_game_poi = models.ForeignKey(VideoGamePOI, on_delete=models.CASCADE)

    def __str__(self):
        return '' + str(self.value) + ': ' + self.video_game_poi.name
