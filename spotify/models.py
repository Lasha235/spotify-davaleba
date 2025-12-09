from django.db import models


class Artist(models.Model):
    spotify_id = models.CharField(max_length=100, unique=True)
    popularity = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Album(models.Model):
    spotify_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    total_tracks = models.PositiveIntegerField(default=0)
    release_date = models.DateField(null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")

    def __str__(self):
        return self.name
    


class Song(models.Model):
    spotify_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    artists = models.ManyToManyField(Artist, related_name="songs")

    def __str__(self):
        return self.title