from django.db import connection

def checkUser(user,password): 
    with connection.cursor() as cursor:
            query = "SELECT id, first_name FROM user WHERE email = %s AND password = %s"
            cursor.execute(query,[user,password])
            rows = cursor.fetchone()
            if rows == None:
                  return [-1]
            else:
                  return [rows[0], rows[1]]
