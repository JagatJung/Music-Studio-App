from django.shortcuts import render
from django.http import HttpResponse
from artists.dbActions import getArtist

def artist(request):
    return render(request, "artists_dash.html", {'artists':getArtist})