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
    def update_location(cls, pk, value):
        cls.objects.filter(pk=pk).update(image=value)


    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()



class Category(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


    

class Images(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length = 500)
    image = models.ImageField(upload_to = 'galy', null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=40, default='admin')

    def __str__(self):
        return self.name
