import json
import sqlite3
import os
import sys
import requests
import re

#
#   JSON Data
#

# Does the instructions.json file exist? If not, download it
json_data_url = 'https://raw.githubusercontent.com/apc53c/solving-sol/master/instructions.json'
json_data_file = '../data/instructions.json'

if not os.path.exists(json_data_file):
    print("Downloading from {0}".format(json_data_url))

    r = requests.get(json_data_url)
    with open(json_data_file, 'w') as fh:
        fh.write(r.text)

# Read the contents of the json_data_file
try:
    with open(json_data_file, 'r') as fh:
        json_data = json.load(fh)
except FileNotFoundError:
    print('Unable to locate {0}'.format(json_data_file), file=sys.stderr)
    quit()

#
#   SQLite Database
#

db_file_name = '../data/lewitt_corpus.db'
instruction_table_name = 'instructions'

instruction_table_schema = 'create table {0} (' \
                           'id INTEGER not null primary key,' \
                           'title TEXT, ' \
                           'description TEXT);'.format(instruction_table_name)

table_exists_query = 'select * ' \
                     'from sqlite_master ' \
                     'where type=\'table\' ' \
                        ' and tbl_name = \'{0}\''.format(instruction_table_name)

insert_into_table = 'insert into {0} values (?, ?, ?)'.format(instruction_table_name)

# SQLite Connection
db_connection = sqlite3.connect(db_file_name)

# SQLite Cursor
db_cursor = db_connection.cursor()

# Create the instructions table in the database
if len(db_cursor.execute(table_exists_query).fetchall()) > 0:
    print("Found table {0}".format(instruction_table_name))
else:
    print("creating table {0}".format(instruction_table_name))
    db_cursor.execute(instruction_table_schema)

# Add json_data to the database
for key in json_data.keys():
    id = int(key)
    title = json_data[key]['title']
    description = json_data[key]['description']

    # remove embedded newline characters from the description
    description = re.sub('\s+', ' ', str.strip(description))
    print('id:{0}\n{1}\n'.format(id, description))

    try:
        db_cursor.execute(insert_into_table, (id, title, description))
    except sqlite3.IntegrityError:
        continue

# Commit the changes to the database
db_connection.commit()

