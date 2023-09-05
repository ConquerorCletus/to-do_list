"""
Module contains our add task function.
"""


import datetime
import os
import json

def collect_data():
    task_name = input("Enter Task name: ")
    task_desc = input("Enter task Description: ")
    task_created_at = datetime.datetime.now()
    remind_at = input ("Please enter a time to perform task in HH:MM (am/pm)format: ")
    try:
        remind_at = datetime.datetime.strptime(remind_at, '%HH:%MM')
    except ValueError:
        print("Invalid date/time format, use the format HH:MM")
        return None

    tasks = {
            'task title:': task_name,
            'task Description:': task_desc,
            'Time logged:': task_created_at,
            'Deadline:': remind_at.strftime('%HH:%MM')
            }
    # file handling section
    directory_path = './task'
    file_name = "{}.json".format(tasks['task title:'])
    file_path = os.path.join(directory_path, file_name)

    # to create directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    # return(file_path)
    # return (tasks)

def add_task():
    # file_path = collect_data()
    try:
        with open(file_path, 'w') as file:

            # file.write(f'Task: {task_name} \n')
            # file.write(f'Description: {task_desc}\n')
            # file.write(f'Time logged: {task_created_at} \n')
            # file.write(f'Task to complete at: {remind_at} \n')
            print("Task successfully added!!!")

    except Exception as e:
       print(f"You don't have permission to create a file in {e}.")


add_task()
