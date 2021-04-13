from django.test import TestCase
from .models import *
# Create your tests here.


class EditorTestClass(TestCase):

    def setUp(self):
        self.location = Location.objects.create(name='Kigali')
        self.category = Category.objects.create(name='park')
        self.park= Image(name = 'park', link = 'https', description ='hhhhhhhh',  category = self.category, location = self.location)
 
