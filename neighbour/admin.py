from django.contrib import admin
from .models import Neighbourhood, Location, Hospital
# Register your models here.

admin.site.register(Neighbourhood)
admin.site.register(Location)
admin.site.register(Hospital)