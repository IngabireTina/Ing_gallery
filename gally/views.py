import os

from django.shortcuts import render
from .models import *
from django.http import HttpResponse, Http404

# Create your views here.


def home(request):
    image = Images.objects.all()
    locations = Location.get_locations()
    category = Category.objects.all()
    context = {'image':image, 'locations': locations, 'category':category}
    return render(request, 'home.html', context )

def location(request, location):
    images = Images.filter_by_location(location)
    locations = Location.get_locations()
    category = Category.objects.all()
    context = {'images':images, 'locations': locations, 'category':category}
    return render(request, 'location.html', context)