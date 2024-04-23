from django.db import connection

def getSongs(): 
    with connection.cursor() as cursor:
            cursor.execute("SELECT ms.id as song_id, ar.id as artist_id, ar.name as name, album_name, title, genre FROM music ms LEFT JOIN artist ar on ms.artist_id = ar.id")
            rows = cursor.fetchall()
    songs = []
    for row in rows:
        song_dict = {
            'song_id': row[0],
            'artist_id': row[1],
            'name': row[2],
            'album_name': row[3],
            'title': row[4],
            'genre': row[5]
        }
        songs.append(song_dict)
    return songs