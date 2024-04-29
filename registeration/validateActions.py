from django.http import JsonResponse
import re

def validate_email(_email):
    email = _email
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    if not re.match(email_regex, email):
        return False
    return True

def validate_password(_password):
    password = _password
    password_regex = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$'
    if not re.match(password_regex, password):
        return False
    return True
