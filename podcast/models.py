from django.db import models

# Create your models here.

class Participant(models.Model):
    username = models.CharField(max_length=40)
    realname = models.CharField(max_length=40)
    description = models.CharField(max_length=240)

class Episode(models.Model):
    title = models.CharField(max_length=80)
    description = models.ManyToManyRel
    pub_date = models.DateTimeField()
    youtube_id = models.CharField(max_length=11)
    participants = models.ManyToManyField(Participant)