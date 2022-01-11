'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
import requests
import json

email_list = []
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
# Get the data
request = requests.get(base_url)
data = request.text
print(type(data)) # data is a string

# Turn it from json into a dict
parsed_json = json.loads(data)
print(type(parsed_json))

final_email_list = [] # Empty list for emails

def make_email_list():
    user_data = parsed_json['data'] # accessing only the 'data' dict
    for email_data in user_data: # going through all the data in the 'data' dict
        email_access = email_data['email'] # accessing only the 'email' data
        final_email_list.append(email_access) #appending the 'email' data each time its found


make_email_list() # Call the function
print(final_email_list)
print(type(final_email_list))