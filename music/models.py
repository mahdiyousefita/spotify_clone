from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100, verbose_name="Artist name")
    bio = models.TextField(blank=True, verbose_name="Bio")
    image = models.ImageField(upload_to='artists/', verbose_name="Artist Image")

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100, verbose_name="Album name")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums', verbose_name="Artist")
    cover = models.ImageField(upload_to='covers/', verbose_name="Album cover")
    release_date = models.DateField(null=True, blank=True, verbose_name="Release date")

    def __str__(self):
        return f"{self.title} - {self.artist.name}"

class Song(models.Model):
    title = models.CharField(max_length=100, verbose_name="Song Name")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs", verbose_name="Album")
    audio_file = models.FileField(upload_to="songs/", verbose_name="Audio file")
    cover = models.ImageField(upload_to="song_covers/", null=True, blank=True, verbose_name="Song cover")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title