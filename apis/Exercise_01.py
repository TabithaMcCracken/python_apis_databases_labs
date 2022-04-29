'''
Done
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body

'''
import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
request = requests.get(base_url)
print(request.status_code)
print(request.encoding)
print(request.text)