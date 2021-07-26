
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name = 'index'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<str:username>/',views.profile,name='profile'),
    path('edit/profile/',views.update_profile,name='update'),
    path('image/',views.post,name='post'),
    path('neighbour/',views.neighbour,name='neighbour'),
    path('health/',views.health,name='health'),
    path('business/',views.business,name='business'),
    path('emergency/',views.emergency,name='emergency'),
    path('search/', views.search_profile, name='search'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)