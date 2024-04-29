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

def validate_phone(phone_number):
    phone_regex = r'^\d{10}$'
    if not re.match(phone_regex, phone_number):
        return False
    return True

def validate_phone(text):
    # Validate text
    if not 2 <= len(text) <= 30:
        return False
    return True

def validate_date(date):
    date_regex = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(date_regex, date):
        return False
    return True
