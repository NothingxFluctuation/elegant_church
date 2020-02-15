from django.db import models
from django.utils import timezone
# Create your models here.


class ChurchInformation(models.Model):
    regno = models.IntegerField(blank=True, null=True)
    church_name = models.TextField(blank=True, null=True)
    firstname = models.TextField(blank=True, null=True)
    lastname = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    alternative_phone = models.TextField(blank=True, null=True)
    web = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    license_type = models.CharField(max_length=10,blank=True,null=True)




class SongRequest(models.Model):
    church = models.ForeignKey(ChurchInformation, related_name="my_song_requests", on_delete=models.CASCADE)
    date_for = models.CharField(max_length=50)
    song_artist = models.CharField(max_length=150)
    song_title = models.CharField(max_length=1000)
    youtube_link = models.CharField(max_length=1000,blank=True,null=True)
    itunes_link = models.CharField(max_length=1000,blank=True,null=True)
    spotify_link = models.CharField(max_length=1000,blank=True,null=True)
    created = models.DateTimeField(default = timezone.now)


