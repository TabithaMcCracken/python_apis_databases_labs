'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''


# We Need To:
# Get users data from the API+
# Get data already in the 'users' table of the database
# Compare data, create new list with new data
# Add new data to the database


from pprint import pprint
import sqlalchemy
from secret import password
import requests
import json
import pymysql

engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{password}@localhost/taskDB')
connection = engine.connect()
metadata = sqlalchemy.MetaData()    


# Function to get user data from API
def get_users():
    base_url = "http://demo.codingnomads.co:8080/tasks_api/users" 
    request = requests.get(base_url) # Gets data
    data = request.text # Data is a string
    parsed_json = json.loads(data) # Converts data from json into a parsed json dict
    return parsed_json

parsed_user_data = get_users()

api_user_list = [] # Empty list for data
def make_user_list(): # Function for accesssing and appending "data"
    user_data = parsed_user_data['data'] # accessing only the 'data' dict
    for data in user_data: # going through all the data in the 'data' dict
        api_user_list.append(data) # Changed 'email_access' to 'email_data'

make_user_list() # Call the function
# pprint(api_user_list) # data is list of dictionaries as "user_list"



# Function to get task data from API
def get_tasks():
    task_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
    task_request = requests.get(task_url)
    data = task_request.text
    parsed_json = json.loads(data)
    return parsed_json


api_task_data = get_tasks()
# pprint(api_task_data)



# Get data already in the 'users' table database

users_table = sqlalchemy.Table('users', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select([users_table])
result_proxy = connection.execute(query)
db_users_list = result_proxy.fetchall()
# pprint(db_users_list)
db_id_list = []
for item in db_users_list:
    db_id_list.append(item[0])
# print(db_id_list)



# Compare user ids in api_user_list to db_users_list
# Create list of new user id's
new_user_id_list = []
for api_item in api_user_list:
    # print(api_item['id'])
    if api_item['id'] not in db_id_list:
        new_user_id_list.append(api_item['id'])
print(new_user_id_list)

# Filter api data to just new user id's data
new_user_list = []

for item in new_user_id_list:
    for dics in api_user_list:
        if dics.get("id") == item:
            new_user_list.append(dics)

print(new_user_list)


# Put the API data into the 'users' table
users = sqlalchemy.Table('users', metadata, autoload=True, autoload_with=engine)
query = sqlalchemy.insert(users)
result_proxy = connection.execute(query, new_user_list)