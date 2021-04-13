from django.db import models
from ingallery import settings

# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=60)
    details = models.TextField()
    photo = models.ImageField(upload_to='galy')

    def __str__(self):
        return self.name
