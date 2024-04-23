from django.shortcuts import render
from django.http import HttpResponse
from song.dbActions import getSongs

def song(request):
    return render(request, "songs_dash.html",  {'songs': getSongs})