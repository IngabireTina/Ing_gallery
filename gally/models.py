from django.db import models
from ingallery import settings

# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=60)
    details = models.TextField()
    photo = models.ImageFiel(upload_to='galy')
