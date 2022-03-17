from django.db import models
import datetime

class Author(models.Model):
    name = models.CharField(max_length=70)
    age = models.PositiveSmallIntegerField()
    count = models.CharField(max_length=30)
    track = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=50)
    photo = models.URLField(blank=True)
    year = models.DateField()
    author = models.ManyToManyField(Author, related_name='tracks')

    def __str__(self):
        return self.name

class Music(models.Model):
    name = models.CharField(max_length=100)
    year = models.DateField()
    text = models.CharField(max_length=300, blank=True)
    duration = models.DurationField(default=datetime.timedelta(seconds=210), blank=True)
    music = models.URLField()
    listened = models.PositiveIntegerField(default=0)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album')

    def __str__(self):
        return self.name

