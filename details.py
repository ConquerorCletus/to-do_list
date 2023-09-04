"""This module shows the task details"""
import show
# import os



def show_details():
    """This shows the details of the tasks"""
    show_task = show.select()

    with open(show_task, 'r') as task:
        tasks = task.read()
        print(tasks)

    

# show_details()
