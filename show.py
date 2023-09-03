"""
This module displays the tasks
"""

import os

def check_task():
    """Check for tasks in tasks directory"""
    directory_path = './task'

    # To check if the task exists
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        tasks = os.listdir(directory_path)
        return (tasks)

def show():
    """This Function shows the saved task."""
    print("Your saved tasks are: ")
    tasks = check_task()
    if tasks == check_task():
        for i, saved_task in enumerate(tasks):
            print(f"{i + 1}.{saved_task}")

    else:
        print(" Task does not exist !!!")


def select():
    """This function selects a task"""
    tasks = check_task()
    for task_num in enumerate(tasks):
        task_num = int(input("Select the task number: ")) - 1

        if 0 <= task_num < len(tasks) :
            selected_task = tasks[task_num]
            return (selected_task)
        else:
            print("Invalid task number !!!")
            return None

# show()
