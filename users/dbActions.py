from django.db import connection, OperationalError
import random
import time

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
            'phone': row[5],
            'dob': row[6],
            'gender': row[7],
            'address': row[8]
        }
        users.append(user_dict)
    return users

def dlt_user(user_id):
    msg = ''
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM user WHERE id = %s", [user_id])
        msg = 'The delete operation was successful'
    except OperationalError as e:
        msg = "Some error has occured: Error occurred" + str(e)
    
    finally:
        return msg

def insertUser(first_name, last_name, email, phone, dob, gender, address):
    msg = ''
    random_number = randomNumer()
    try:
        query = "INSERT INTO user (first_name, last_name, email, phone, dob, gender, address, password, updated_at) VALUES (%s, %s, %s,%s, %s, %s,%s,%s, NOW())"
        with connection.cursor() as cursor:
            cursor.execute(query, [first_name, last_name, email, phone, dob, gender, address, random_number])
        msg = 'Use the registered email address and reset password with code' + str(random_number)
    except OperationalError as e:
        msg = "Some error has occured: Error occurred" + str(e)
    finally:
        return msg

def updateUser(first_name, last_name, email, phone, dob, gender, address, user_id):
    try:
        query = "UPDATE user SET first_name = %s, last_name = %s, email = %s, phone  = %s, dob = %s, gender = %s, address = %s, updated_at = NOW() WHERE id = %s"
        with connection.cursor() as cursor:
            cursor.execute(query, [first_name, last_name, email, phone, dob, gender, address, user_id])
        msg = "Update successful"
    except OperationalError as e:
        msg = "Some error has occured: Error occurred" + str(e)
    finally:
        return msg

def resetPasswordUser( user_id):
    msg = ''
    random_number = randomNumer()
    try:
        query = "UPDATE user SET password = %s, updated_at = NOW() WHERE id = %s"
        with connection.cursor() as cursor:
            cursor.execute(query, [random_number, user_id])
        msg = 'Password reset Successful, your code:' + str(random_number)
    except OperationalError as e:
        msg = "Some error has occured: Error occurred" + str(e)
    finally:
        return msg

        
def randomNumer():
    timestamp = int(time.time())
    random.seed(timestamp)
    random_number = ''.join(random.choices('0123456789', k=4))
    return random_number


