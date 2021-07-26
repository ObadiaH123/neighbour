from django.contrib import admin
from .models import Post,Profile,Business, Healthcenter, Neighbour

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Neighbour)

admin.site.register(Business)
admin.site.register(Healthcenter)