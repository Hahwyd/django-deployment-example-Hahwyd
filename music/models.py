from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=255, blank=False)
    file = models.FileField(upload_to='uploads/')