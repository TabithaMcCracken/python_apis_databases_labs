'''
Done
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import json
import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 595,
    "first_name": "Tabitha",
    "last_name": "Mccracker",
    "email": "tabimccrack@aol.com"
}

response = requests.put(base_url, json=body)
print(response.status_code)

response = requests.get(base_url)
print(response.content)
