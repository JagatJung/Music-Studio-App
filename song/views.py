from django.shortcuts import render
from django.http import HttpResponse
from song.dbActions import getSongs, dlt_songs, getArtists, updateSongs, insertSongs


def song(request, id = -1):
    if request.method == "POST":
        button_value =request.POST['submit'].split('_')
        print(button_value[0])
        if(button_value[0] == 'dlt') :
            dlt_songs(button_value[1])
            return render(request, "songs_dash.html",  {'songs': getSongs(id), 'artists': getArtists })
        elif (button_value[0] == 'update') :
            updateSongs(request.POST['name'], request.POST['title'], request.POST['album_name'], request.POST['genre'], button_value[1])
            return render(request, "songs_dash.html",  {'songs': getSongs(id), 'artists': getArtists })
        elif (button_value[0] == 'insert') :
            insertSongs(request.POST['name'], request.POST['title'], request.POST['album_name'], request.POST['genre'])
            return render(request, "songs_dash.html",  {'songs': getSongs(id), 'artists': getArtists })
    return render(request, "songs_dash.html",  {'songs': getSongs(id), 'artists': getArtists })

# def song(request, id):
#     if request.method == "POST":
#         button_value =request.POST['submit'].split('_')
#         print(button_value[0])
#         if(button_value[0] == 'dlt') :
#             dlt_songs(button_value[1])
#             return render(request, "songs_dash.html",  {'songs': getSongs, 'artists': getArtists })
#         elif (button_value[0] == 'update') :
#             updateSongs(request.POST['name'], request.POST['title'], request.POST['album_name'], request.POST['genre'], button_value[1])
#             return render(request, "songs_dash.html",  {'songs': getSongs, 'artists': getArtists })
#         elif (button_value[0] == 'insert') :
#             insertSongs(request.POST['name'], request.POST['title'], request.POST['album_name'], request.POST['genre'])
#             return render(request, "songs_dash.html",  {'songs': getSongs, 'artists': getArtists })
#     return render(request, "songs_dash.html",  {'songs': getSongs, 'artists': getArtists })