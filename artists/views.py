from django.shortcuts import render
from django.http import HttpResponse
from artists.dbActions import getArtist, dlt_artist, updateArtist, insertArtist

def artist(request):
    years =  range(1800,2025)
    if request.method == "POST":
        button_value =request.POST['submit'].split('_')
        if(button_value[0] == 'dlt') :
            dlt_artist(button_value[1])
            return render(request, "artists_dash.html", {'artists':getArtist, 'years': years})
        elif (button_value[0] == 'update') :
            updateArtist(request.POST['name'], request.POST['dob'], request.POST['gender'],request.POST['address'],request.POST['no_of_album'] ,request.POST['first_release'] , button_value[1])
            return render(request, "artists_dash.html", {'artists':getArtist, 'years': years})
        elif (button_value[0] == 'insert') :
            insertArtist(request.POST['name'], request.POST['dob'], request.POST['gender'],request.POST['address'],request.POST['no_of_album'] ,request.POST['first_release'])
            return render(request, "artists_dash.html", {'artists':getArtist, 'years': years})
    return render(request, "artists_dash.html", {'artists':getArtist, 'years': years})