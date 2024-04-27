from django.db import connection

def getSongs(id = -1): 
    with connection.cursor() as cursor:
            query = "SELECT ms.id as song_id, ar.id as artist_id, ar.name as name, album_name, title, genre FROM music ms INNER JOIN artist ar on ms.artist_id = ar.id"
            if int(id) is not -1:
                query = query + " AND ar.id = " + str(id)
            cursor.execute(query)
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

def getArtists():
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name from artist")
        rows = cursor.fetchall()
    artist = []
    for row in rows:
        artist_dict = {
            'artist_id': row[0],
            'name': row[1],
        }
        artist.append(artist_dict)
    return artist
     

def dlt_songs(song_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM music WHERE id = %s", [song_id]) 

def updateSongs(artist_id, title, album_name, genre, music_id) :
    query = "UPDATE music SET artist_id= %s, title= %s, album_name = %s, genre = %s, update_ts = NOW() WHERE id = %s"

    with connection.cursor() as cursor:
        cursor.execute(query, [artist_id, title, album_name, genre, music_id])

def insertSongs(artist_id, title, album_name, genre):
    query = "INSERT INTO music (artist_id, title, album_name, genre, update_ts) VALUES (%s, %s, %s,%s, NOW())"

    with connection.cursor() as cursor:
        cursor.execute(query, [artist_id, title, album_name, genre])