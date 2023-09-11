"""This module contains a functions that delete tasks"""

import show
import os

def delete_task():
    """This function delete tasks from tasks"""
    show.show()
    print("Select the task to delete !!")
    task = show.select()

    if task == task:
        option = input("Are you sure you want to delete task? yes/no : ")
        if option == 'yes':
            os.remove(task)
            print("Task deleted !!")
        elif option == 'no':
            print("Have a nice day!!")
        else:
            print("Invalid Option !!")

    else:
        print("No task selected to delete")


# delete_task()
