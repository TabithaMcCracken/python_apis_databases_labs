'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "Tabi",
    "last_name": "McCracken",
    "email": "tabithamccracken@aol.com"
}

response = requests.post(base_url,json=body)
print(f"Response Code: {response.status_code}")

response = requests.get(base_url)
print(f"Response Conetent: {response.content}")


