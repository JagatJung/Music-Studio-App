from django.db import connection

def getUsers(): 
    with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM user")
            rows = cursor.fetchall()
    users = []
    for row in rows:
        user_dict = {
            'id': row[0],
            'first_name': row[1],
            'last_name': row[2],
            'email': row[3],
            'password': row[4],
            'phone': row[5],
            'dob': row[6],
            'gender': row[7],
            'address': row[8],
            'created_at': row[9],
            'updated_at': row[10]
        }
        users.append(user_dict)
    return users