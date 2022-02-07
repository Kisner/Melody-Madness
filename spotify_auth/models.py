from django.db import models


# Create your models here.
class Artist(models.Model):
    # setup for the artist model based on jay's implementation
    artist = models.CharField(max_length=100)
    a_uri = models.CharField(max_length=200)
    a_genre = models.CharField(max_length=500)
    a_pop = models.IntegerField()
    a_img = models.ImageField()
