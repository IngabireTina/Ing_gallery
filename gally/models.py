from django.db import models
from ingallery import settings

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    @classmethod
    def update_locations(cls, pk, value):
        cls.objects.filter(pk=pk).update(image=value)

    

    

class Images(models.Model):
    name = models.CharField(max_length=60)
    details = models.TextField()
    img_category = models.CharField(max_length=100, choices=CATEGORY, default='PARTIES')
    photo = models.ImageField(upload_to='galy')

    def __str__(self):
        return self.name
