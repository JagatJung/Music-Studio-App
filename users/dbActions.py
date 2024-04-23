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

def dlt_user(user_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM user WHERE id = %s", [user_id]) 

def insertUser(first_name, last_name, email, phone, dob, gender, address):
    query = "INSERT INTO user (first_name, last_name, email, phone, dob, gender, address, updated_at) VALUES (%s, %s, %s,%s, %s, %s,%s, NOW())"
    # Execute the SQL query
    with connection.cursor() as cursor:
        cursor.execute(query, [first_name, last_name, email, phone, dob, gender, address])

def updateUser(first_name, last_name, email, phone, dob, gender, address, user_id):
        query = "UPDATE user SET first_name = %s, last_name = %s, email = %s, phone  = %s, dob = %s, gender = %s, address = %s, updated_at = NOW() WHERE id = %s"

        # Execute the SQL query
        with connection.cursor() as cursor:
            cursor.execute(query, [first_name, last_name, email, phone, dob, gender, address, user_id])

def resetPasswordUser( user_id):
        query = "UPDATE user SET password = 0, updated_at = NOW() WHERE id = %s"
     
        # Execute the SQL query
        with connection.cursor() as cursor:
            cursor.execute(query, [user_id])

        
     

