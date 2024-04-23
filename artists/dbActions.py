from django.db import connection

def getArtist(): 
    with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, dob, gender, address, first_release_year, no_of_album_released FROM `artist`")
            rows = cursor.fetchall()
    artists = []
    for row in rows:
        artist_dict = {
            'id': row[0],
            'name': row[1],
            'dob': row[2],
            'gender': row[3],
            'address': row[4],
            'debut': row[5],
            'NumberofAlbums': row[6],
        }
        artists.append(artist_dict)
    return artists