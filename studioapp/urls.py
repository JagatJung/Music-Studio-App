from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('registeration.urls')),
    path('', include('artists.urls')),
    path('', include('song.urls')),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
]