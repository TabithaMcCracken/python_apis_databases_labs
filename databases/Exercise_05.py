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

# Create a new table


# Get user info
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

final_email_list = [] # Empty list for emails

def make_email_list():
    user_data = parsed_json['data'] # accessing only the 'data' dict
    for email_data in user_data: # going through all the data in the 'data' dict
        #email_access = email_data['email'] # accessing only the 'email' data
        final_email_list.append(email_data) # Changed 'email_access' to 'email_data'


make_email_list() # Call the function
print(final_email_list)
print(type(final_email_list))

#Get data into a table
new_products = [ {'product_id':1, 'product_name':'Sleigh Sign', 'product_desc':"5x7 \
                    Sleigh sign: It's Lovely Weather for a slegih ride together", 'product_price':20.00},
                {'product_id':2, 'product_name':'Gold Tree', 'product_desc':"9inch \
                    Christmas tree: O Come Let Us Adore Him", 'product_price':20.00},
                {'product_id':3, 'product_name':'Small Spoons Game', 'product_desc': \
                    "Six player spoons and LRC game", 'product_price':40.00}
                ]
result_proxy = connection.execute(query, final_email_list)

location = sqlalchemy.Table('location', metadata, autoload=True, autoload_with=engine)
query = sqlalchemy.insert(location)
locations = [ {'location_id':1, 'location_name':'Home', 'tax_rate':6.25},
            {'location_id':2, 'location_name':'Aurora', 'tax_rate':8.00},
            {'location_id':3, 'location_name':'South Dakota', 'tax_rate':0.00}
            ]
result_proxy = connection.execute(query, locations)


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