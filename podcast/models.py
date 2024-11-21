from django.db import models

# Create your models here.

class Participant(models.Model):
    username = models.CharField(max_length=40)
    realname = models.CharField(max_length=40, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.username

class Episode(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    pub_date = models.DateField()
    youtube_id = models.CharField(max_length=11)
    participants = models.ManyToManyField(Participant)

    def __str__(self):
        return self.title