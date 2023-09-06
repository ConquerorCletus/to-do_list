"""This module shows the task details"""
import show
# import os
import json


def show_details():
    """This shows the details of the tasks"""
    show_task = show.select()
    if show_task == None:
        print("No task available!!")
    else:
        with open(show_task, 'r') as task:
            tasks = json.load(task)

        for key, value in tasks.items():
            print(f"{key} : {value}")

    

show_details()
