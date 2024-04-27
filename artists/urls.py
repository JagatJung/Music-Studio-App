from django.urls import path
from . import views
from song import views as song_view

urlpatterns = [
    path('artist/', views.artist, name='artist'),
    path('artist/artist_music/<int:id>/', song_view.song , name='artist_music'),
]