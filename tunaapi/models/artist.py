from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=75)
    age = models.IntegerField()
    bio = models.CharField(max_length=2048)
