from django.db import models
from ingallery import settings

# Create your models here.

CATEGORY = (('TRAVEL','TRAVEL'),('PARTIES','PARTIES'))

class Images(models.Model):
    name = models.CharField(max_length=60)
    details = models.TextField()
    img_category = models.CharField(max_length=100, choices=CATEGORY, default='PARTIES')
    photo = models.ImageField(upload_to='galy')

    def __str__(self):
        return self.name
