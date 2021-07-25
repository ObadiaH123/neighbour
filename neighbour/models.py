from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from cloudinary.models import CloudinaryField 


class Image(models.Model):
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
        cap = Image.objects.filter(caption=old).update(caption=new)
        return cap

    def __str__(self):
        return self.name

    