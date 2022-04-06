'''
Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''


# We Need:
# Function to get the users and tasks from the url
# Create tables
# Check to see if data already exists in the tables
# Put data in tables

from pprint import pprint
import sqlalchemy
from secret import password
import requests
import json
# import pymysql

engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{password}@localhost/taskDB')
connection = engine.connect()
metadata = sqlalchemy.MetaData()    


# Get user data from API
email_list = []
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
# Get the data
request = requests.get(base_url)
data = request.text
print(type(data)) # data is a string

# Turn it from json into a dict
parsed_json = json.loads(data)
print(parsed_json)
print(type(parsed_json))

user_list = [] # Empty list for emails

def make_email_list():
    user_data = parsed_json['data'] # accessing only the 'data' dict
    for email_data in user_data: # going through all the data in the 'data' dict
        #email_access = email_data['email'] # accessing only the 'email' data
        user_list.append(email_data) # Changed 'email_access' to 'email_data'


make_email_list() # Call the function
print(user_list)
print(type(user_list))


# # Put the API data into the 'users' table

# users = sqlalchemy.Table('users', metadata, autoload=True, autoload_with=engine)
# query = sqlalchemy.insert(users)
# result_proxy = connection.execute(query, user_list)


# # Get data already in the 'users' table

# users_table = sqlalchemy.Table('users', metadata, autoload=True, autoload_with=engine)

# query = sqlalchemy.select([users_table])
# result_proxy = connection.execute(query)
# result_set = result_proxy.fetchall()
# pprint(result_set)


# # Function to get task data
# def get_tasks():
#     task_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
#     task_request = requests.get(task_url)
#     data = task_request.text
#     parsed_json = json.loads(data)
#     return parsed_json

# # Function view all your tasks (GET)
# def view_tasks():
#     # Get task data
#     task_data = get_tasks()
#     # Get only "data"
#     user_data = task_data["data"]

#     userId_input = int(input("Please enter your user Id: \n"))

#     task_list = []
    

#     for task_data in user_data:
#         task_access = task_data["userId"]
#         if task_access == userId_input:
#             task = task_data["name"]
#             task_list.append(task)
            
#     print(f"Here is your task list: \n {task_list}")


# view_tasks()

actor_table = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select(actor_table).where(actor_table.columns.first_name == 'Matthew')
result_proxy = connection.execute(query)

for actor in result_proxy:
    print(actor)