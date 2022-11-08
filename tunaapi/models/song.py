from django.db import models


class Song(models.Model):
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    length = models.IntegerField()
    album = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
