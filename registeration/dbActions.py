from django.db import connection, OperationalError
import hashlib
def checkUser(user,password):
      password = hashlib.sha256(password.encode()).hexdigest()
      try: 
            with connection.cursor() as cursor:
                        query = "SELECT id, first_name FROM user WHERE email = %s AND password = %s"
                        cursor.execute(query,[user,password])
                        rows = cursor.fetchone()
                        if rows == None:
                              return [-1]
                        else:
                              return [rows[0], rows[1]]
      except OperationalError as e:
            return [-1, "Some error has occured: Error occurred" + str(e)]

def resetPwdDB(user, code, oldpwd):
      msg = ''
      oldpwd = hashlib.sha256(oldpwd.encode()).hexdigest()
      try:
            with connection.cursor() as cursor:
                        query = "UPDATE user SET password = %s, updated_at = NOW()  WHERE email = %s AND password = %s"
                        cursor.execute(query,[oldpwd, user,code])
                        msg = 'update password successful'
           
      except OperationalError as e:
        msg = "Some error has occured: Error occurred" + str(e)
      finally:
            return msg
