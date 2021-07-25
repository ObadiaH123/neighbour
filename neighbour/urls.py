from django.urls import path
from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
    
    path('',views.index,name = 'index'),
    path('account/', include('django.contrib.auth.urls')),