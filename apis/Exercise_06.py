'''
Done
Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.
'''

import requests
import json

# We need:
# 1 Function to get tasks from url
# 7 Functions for each action
# 1 Function asking which task to complete
# To call which_task() function to start the program
# While Loop to ask to complete another task

# Function to get task data
def get_tasks():
    task_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
    task_request = requests.get(task_url)
    data = task_request.text
    parsed_json = json.loads(data)
    return parsed_json

# Function 1) Create a new account (POST)
def new_account():
    user_url = "http://demo.codingnomads.co:8080/tasks_api/users"
    # Get required info from user
    first_name = input("Please enter your first name: \n")
    last_name = input("Please enter your last name: \n")
    email = input("Please enter your email address: \n")
    # Put info in json format
    body = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    # Post info, check status and give user their user id
    account_post = requests.post(user_url, json=body)
    
    print(f"Response Code: {account_post.status_code}")
    if account_post.status_code == 200:
        print("Congratulations you have created a new account!")
        response = requests.get(user_url)
        data = response.json()
        new_data = data["data"][-1]["id"]
        print(f"Your user id is: \n{new_data}")

# Function 2) View all your tasks (GET)
def view_tasks():
    # Get task data
    task_data = get_tasks()
    # Get only "data"
    user_data = task_data["data"]

    userId_input = int(input("Please enter your user Id: \n"))

    task_list = []
    

    for task_data in user_data:
        task_access = task_data["userId"]
        if task_access == userId_input:
            task = task_data["name"]
            task_list.append(task)
            
    print(f"Here is your task list: \n {task_list}")

# Function 3) View your completed tasks (GET)
def view_completed():
    # Get task data
    task_data = get_tasks()
    # Get only "data"
    user_data = task_data["data"]

    userId_input = int(input("Please enter your us Id: \n"))

    completed_list = []

    for task_data in user_data:
        task_access = task_data["userId"]
        task_status = task_data["completed"]
        task_des = task_data["name"]
        if task_access == userId_input and task_status == True:
            completed_list.append(task_des)

    print(f"Here is your list of completed tasks: \n {completed_list}")


# Function 4) View only your incomplete tasks (GET)
def view_incomplete():
    # Get task data
    task_data = get_tasks()
    # Get only "data"
    user_data = task_data["data"]

    userId_input = int(input("Please enter your us Id: \n"))

    completed_list = []

    for task_data in user_data:
        task_access = task_data["userId"]
        task_status = task_data["completed"]
        task_des = task_data["name"]
        if task_access == userId_input and task_status == False:
            completed_list.append(task_des)

    print(f"Here is your list of completed tasks: \n {completed_list}")

# Function 5) Create a new task (POST)
def create_task():
    task_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
    userId_input = input("Please enter your user id: \n")
    task_name = input("Please enter your task: \n")
    task_des = input("Please enter a description of your task: \n")
    user_flag = input("Is your task already completed? Yes or No\n")
    completed_flag = False
    if user_flag == "Yes":
        completed_flag = True

    body = {
        "userId": userId_input,
        "name": task_name,
        "description": task_des,
        "completed": completed_flag
    }

    task_post = requests.post(task_url, json=body)
    
    if task_post.status_code == 200:
        print("Congratulations you have created a new task!")


# Function 6) Update an existing task (PATCH/PUT)
def update_task():
    # Get task data
    task_data = get_tasks()
    # Get only "data"
    user_data = task_data["data"]

    id = int()
    description = str()
    userId_input = int(input("Please enter your user Id: \n"))

    task_list = []
    
    for task_data in user_data:
        task_access = task_data["userId"]
        if task_access == userId_input:
            task = task_data["name"]
            task_list.append(task)
            
    print(f"Here is your task list: \n {task_list}")
    
    update_task = input("Which task would you like to update to compplete?")
    user_flag = input("Is your task already completed? Yes or No\n")
    completed_flag = False # Defaults to not completed
    if user_flag == "Yes":
        completed_flag = True
    elif user_flag == "No":
        completed_flag = False

    # Get id based on userId and name

    for task in user_data:
        task_access = task["userId"]
        task_name = task["name"]
        if task_access == userId_input and task_name == update_task:
            id = task["id"]
            description = task["description"]

    body = {
        "id": id,
        "userId": userId_input,
        "name": update_task,
        "description": description,
        "completed": completed_flag
    }
    task_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
    task_put = requests.put(task_url, json=body)
    
    if task_put.status_code == 200:
        print("You have updated a task!")



# Function 7) Delete a task (DELETE)
def delete_task():
    task_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"
    task_request = requests.get(task_url)
    data = task_request.text
    parsed_json = json.loads(data)
    id = int()
    
    userId_input = int(input("Please enter your user Id: \n"))

    task_list = []
    user_data = parsed_json["data"]
    
    for task_data in user_data:
        task_access = task_data["userId"]
        if task_access == userId_input:
            task = task_data["name"]
            task_list.append(task)
            
    print(f"Here is your task list: \n {task_list}")

    delete_task = input("Which task would you like to delete?")

    # Get is for task to be deleted
    for task in user_data:
        task_access = task["userId"]
        task_name = task["name"]
        if task_access == userId_input and task_name == delete_task:
            id = task["id"]
        
    response = requests.delete(task_url + "/" + str(id))
    if response.status_code == 200:
        print("You have deleted a task!")


# Function asking which task to complete
def which_task():
    task = int(input(
        "Please select from the following options (enter the number of the action "
        "you'd like to take):\n"
        "1) Create a new account (POST)\n"
        "2) View all your tasks (GET)\n"
        "3) View your completed tasks (GET)\n"
        "4) View only your incomplete tasks (GET)\n"
        "5) Create a new task (POST)\n"
        "6) Update an existing task (PATCH/PUT)\n"
        "7) Delete a task (DELETE)\n"
    ))
    print(f"You have selected option: {task}")

    if task == 1:
        new_account()
    elif task == 2:
        view_tasks()
    elif task == 3:
        view_completed()
    elif task == 4:
        view_incomplete()
    elif task == 5:
        create_task()
    elif task == 6:
        update_task()
    elif task == 7:
        delete_task()

    

which_task()

# Ask to complete another task
# Should i put this into a function?
end_task_flag = False
while end_task_flag == False:
    another_task = input("Would you like to complete another option? Yes or No\n")
    if another_task == "Yes":
        which_task()
        end_task_flag = False
    elif another_task == "No":
        end_task_flag = True
    else:
        print("Invalid response")
        end_task_flag = False

