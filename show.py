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
    try:
        for task_num in enumerate(tasks):
            task_num = int(input("Select the task number: ")) - 1
            if task_num <= len(tasks) :
                selected_task_name = tasks[task_num]
                selected_task = os.path.join('./task', selected_task_name)
                return (selected_task)
            else:
                print("Invalid task number !!!")
                return None
    except FileNotFoundError:
        print("The task not found!!! ")
    except ValueError:
        print("Invalid task number chosen !!")
    except Exception as e:
        print(f"An error Occured :{e}")

# show()
