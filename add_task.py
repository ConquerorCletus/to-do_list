"""
Module contains our add task function.
"""


import datetime
import os
import json

def collect_data():
    # collect input data to store in a dictionary called task
    task_name = input("Enter Task name: ")
    task_desc = input("Enter task Description: ")
    task_created_at = datetime.datetime.now()

    # To Ensure user entered the right time format
    try:
        remind_at = input ("Please enter a time to perform task in HH:MM format: ")
        # to extract the time component only
        time_to_be_reminded = datetime.datetime.strptime(remind_at,'%H:%M')
        # retrieving time only from parsed string
    except ValueError:
        print("Invalid date/time format, use the format HH:MM")

    # The dictionary created to store inputs
    return {
            'task title': task_name,
            'task Description': task_desc,
            'Time logged': task_created_at.isoformat(),
            'Deadline': time_to_be_reminded.strftime('%H:%M')
            }

def add_task():
    """This functions add a task to the To-do List"""
    # file handling section
    tasks = collect_data()
    directory_path = './task'
    file_name = "{}.json".format(tasks['task title'])
    file_path = os.path.join(directory_path, file_name)

    # to create directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    try:
        with open(file_path, 'w') as file:
            json.dump(tasks, file, indent=4)
            print("Task successfully added!!!")

    except Exception as e:
        print(f"You don't have permission to create a file in {e}.")


# add_task()
