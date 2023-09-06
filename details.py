"""This module shows the task details"""
# import show
import json
import os


def show_details(show_task):
    """This shows the details of the tasks"""
    # show_task = show.select()
    # if show_task == None:
    #     print("No task available!!")
    # else:
    try:
        with open(show_task, 'r') as task:
            tasks = json.load(task)
        
        for key, value in tasks.items():
            print(f"{key} : {value}")

    except Exception as e:
        print(f"You encountered this {e}")


# show_details()
