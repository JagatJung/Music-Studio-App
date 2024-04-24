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

def dlt_artist(artist_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM artist WHERE id = %s", [artist_id]) 

def updateArtist(name, dob, gender, address, no_of_album, first_release, artist_id) :
    query = "UPDATE artist SET name = %s, dob = %s, gender = %s, address  = %s, first_release_year = %s, no_of_album_released = %s, update_ts = NOW() WHERE id = %s"

    # Execute the SQL query
    with connection.cursor() as cursor:
        cursor.execute(query, [name, dob, gender, address, first_release, no_of_album, artist_id])
