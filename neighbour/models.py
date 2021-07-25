from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from cloudinary.models import CloudinaryField 


class Neighbour(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(max_length=100)
    image = CloudinaryField('image') 
    healthcenter =  models.ForeignKey('healthcenter',on_delete=models.CASCADE)
    location =  models.ForeignKey('Location',on_delete=models.CASCADE)

    @classmethod
    def search_by_category(cls,search_term):
        image_category = cls.objects.filter(name__icontains=search_term)
        return image_category


    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

    def save_image(self):
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

class Healthcenter(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()


class Business(models.Model):
    name = models.CharField(max_length =30)
    email = models.CharField(max_length =30)
    neighbour=models.ForeignKey('neighbour', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    def save_location(self):
        self.save()


class Post(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')
    # image = models.ImageField(upload_to = 'gallery/', null=True, blank=True)
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=30)

    class Meta:
        ordering = ["-pk"]


    @classmethod
    def images(cls):
        images = cls.objects.all()
        return images

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,old,new):
        cap = Post.objects.filter(caption=old).update(caption=new)
        return cap

    def __str__(self):
        return self.name

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    photo = CloudinaryField('image') 
    # photo = models.ImageField(upload_to = 'gallery/', null=True, blank=True, default='download.jpeg')
    bio = models.CharField(max_length=300)
    name = models.CharField(blank=True, max_length=120)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def profile(cls):
        profiles = cls.objects.all()
        return profiles

    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def save_profile(self):
        self.user

    def __str__(self):
        return self.name

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

