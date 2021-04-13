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