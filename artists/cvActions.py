import csv
from artists.dbActions import insertArtist
from datetime import datetime

def upload_to_db_from_csv(csv_file):
    decoded_file = csv_file.read().decode('utf-8-sig').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        insertArtist(row['name'], parse_date(row['dob']), parse_gender(row['gender']), row['address'], row['no_of_album_released'], int (row['first_release_year']))

# name, dob, gender, address, no_of_album, first_release
def parse_date(date_str):
    possible_formats =     possible_formats = [
        '%Y-%m-%d', '%m-%d-%Y', '%d-%m-%Y', '%m/%d/%Y', '%d/%m/%Y',
        '%Y/%m/%d', '%Y.%m.%d', '%m.%d.%Y', '%d.%m.%Y', '%Y%m%d', 
        '%m-%d-%y', '%d-%m-%y', '%m/%d/%y', '%d/%m/%y', 
        '%Y-%m-%d %H:%M:%S', '%m-%d-%Y %H:%M:%S', '%d-%m-%Y %H:%M:%S',
        '%m/%d/%Y %H:%M:%S', '%d/%m/%Y %H:%M:%S', 
        '%Y/%m/%d %H:%M:%S', '%Y.%m.%d %H:%M:%S', '%m.%d.%Y %H:%M:%S',
        '%d.%m.%Y %H:%M:%S', '%Y%m%d%H%M%S', '%m-%d-%y %H:%M:%S',
        '%d-%m-%y %H:%M:%S', '%m/%d/%y %H:%M:%S', '%d/%m/%y %H:%M:%S',
    ]
    for fmt in possible_formats:
        try:
            return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue
    return None

def parse_gender(gender):
    input_str = gender.lower()  # Convert input string to lowercase for case-insensitive comparison
    if input_str in ['male','m']:
        rtn_stg = 'm'
    elif input_str is ['female','f']:
        rtn_stg = 'f'
    else:
        rtn_stg = 'o'
    return rtn_stg