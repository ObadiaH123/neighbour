from django.db import models

from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField 

class Neighbourhood(models.Model):
    name = models.CharField(max_length=55)
    image = CloudinaryField('image') 
    hospital =  models.ForeignKey('Hospital',on_delete=models.CASCADE)
    location =  models.ForeignKey('Location',on_delete=models.CASCADE)

    @classmethod
    def search_by_category(cls,search_term):
        image_category = cls.objects.filter(title__icontains=search_term)
        return image_category


    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

    def save_neighbour(self):
        self.save()

    @classmethod
    def get_image(cls):
        image= cls.objects.get(pk=id)
        return image

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

class Hospital(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()



