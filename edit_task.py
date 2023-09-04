"""
This module is responsible for editing the task.
"""

import os
import datetime
from details import show_details
import show

def edit_task():
    """This function edit the tasks"""
    show.show()
    selected_task = show.select()
    time_updated = datetime.datetime.now()
   
   # to open the selected task for editting
    with open(selected_task, 'r+') as editted_task:
        task_line = editted_task.readlines()
      
      # show details of tasks with a specific line number
        for line, details in enumerate(task_line):
            print(f"{line + 1}: {details}")
            

        edit_line = int(input("The task line to edit: ")) - 1
        new_content = input("New Task content: ")
       
       # This ensures that user input the correct task line
        if edit_line <= len(task_line):
            task_line[edit_line] = new_content + '\n'
            editted_task.seek(0)
            editted_task.writelines(task_line)
            editted_task.truncate()
            print("Task editted successfully!!")
        else:
            print("Invalid task line selected!!")

        show_option = input("Do you want to see details of task? yes/no: ")
        # show_option = show_option.lower

        if show_option == 'yes':
            show_details()
        elif show_option == 'no':
            print("Exiting!! Exiting!!")
        else:
            print("Invalid choice!! ")




edit_task()
