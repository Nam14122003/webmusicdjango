from django.db import models
from os import name

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500)
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True, blank=True)
    audio_file = models.FileField(upload_to='musics/')
    cover_image = models.ImageField(upload_to='music_image/')
    # image = models.ImageField()
    # lyrics = models.FileField(upload_to='lyrics/')
    # audio_file = models.FileField(blank=True, null=True)
    # audio_link = models.FileField(max_length=200, blank=True, null=True)
    # duration = models.CharField(max_length=20)
    # paginate_by = 2
    
    def __str__(self):
        return self.title
    
    class META:
        ordering = ['title']
    
class Album(models.Model):
    name = models.CharField(max_length=400)
    
