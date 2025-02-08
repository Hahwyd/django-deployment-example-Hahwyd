from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255, blank=False)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f"<title={self.title}, file={self.file}>"