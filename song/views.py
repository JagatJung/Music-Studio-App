from django.shortcuts import render
from django.http import HttpResponse
from song.dbActions import getSongs, dlt_songs

def song(request):
    if request.method == "POST":
        button_value =request.POST['submit'].split('_')
        if(button_value[0] == 'dlt') :
            print(button_value)
            dlt_songs(button_value[1])
            return render(request, "songs_dash.html",  {'songs': getSongs})
    return render(request, "songs_dash.html",  {'songs': getSongs})