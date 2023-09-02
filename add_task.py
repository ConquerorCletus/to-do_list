"""
Module contains our add task function.
"""


import datetime
import os

def add_task():
    task_name = input("Enter Task name: ")
    task_desc = input("Enter task Description: ")
    task_created_at = datetime.datetime.now()
    remind_at = input (" Please enter a time in HH:MM:SS format:")
    # file handling section
    directory_path = './task'
    file_name = "{}.txt".format(task_name)
    file_path = os.path.join(directory_path, file_name)

    # to create directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    try:
        with open(file_path, 'w') as file:
            file.write("Task details!! \n")
            file.write(f'Task: {task_name} \n')
            file.write(f'Description: {task_desc}\n')
            file.write(f'Time logged: {task_created_at} \n')
            file.write(f'Task to complete at: {remind_at} \n')

    except Exception as e:
       print(f"You don't have permission to create a file in {e}.")


add_task()
