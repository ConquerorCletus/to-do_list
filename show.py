"""
This module displays the tasks
"""

import os

def show():
    directory_path = './task'

    # To check if the task exists
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        tasks = os.listdir(directory_path)
        print("Your saved tasks are: ")
        # print()

        for i, saved_task in enumerate(tasks):
            print(f"{i + 1}.{saved_task}")

    else:
        print(" Task does not exist !!!")


# show()
