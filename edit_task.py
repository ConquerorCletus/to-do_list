"""
This module is responsible for editing the task.
"""

import os
import datetime
from details import show_details
import show
import json

def edit_task():
    """This function edit the tasks"""
    show.show()
    selected_task = show.select()
    time_updated = datetime.datetime.now()
    # to open the selected task for editting
    show_details(selected_task)
    
    print('''
         what do you want to edit?\n
         1. Task title
         2. Task Description
         3. Deadline
         4. quit \n
         ''')
    choice = int(input("Enter your choice: "))
    with open(selected_task, 'r+') as editted_task:
        task_line = json.load(editted_task)
        if choice == 1:
            new_task_name = input("Enter your new task name: ")
            task_line['task title'] = new_task_name
            print("Task name editted successfully!!!")
        elif choice == 2:
            new_desc = input("Enter a new task description: ")
            task_line['task Description'] = new_desc
            print("Task Description editted successfully")
        elif choice == 3:
            new_deadline = input("Enter a new task deadline (HH:MM): ")
            deadline = datetime.datetime.strptime(new_deadline, '%H:%M').strftime('%H:%M')
            task_line['Deadline'] = deadline
            print("Task deadline successfully editted!!!")
        elif choice == 4:
            print("Exiting Program!! ")
        else:
            print('Invalid option\n choose between option(1-4)')

        editted_task.seek(0)
        json.dump(task_line, editted_task, indent=4)

        details = input("Do you want to see new details of task? yes/no: ")
        if details == 'yes':
            show_details(selected_task)
        elif details == 'no':
            print("Exiting program!!!")
              
         


# edit_task()
