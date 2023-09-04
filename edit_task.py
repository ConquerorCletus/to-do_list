"""
This module is responsible for editing the task.
"""

import os
import datetime
import show

def edit_task():
    """This function edit the tasks"""
    show.show()
    selected_task = show.select()
    time_updated = datetime.datetime.now()

    with open(selected_task, 'r+') as editted_task:
        # task_content = editted_task.read()
        # print(task_content)
        task_line = editted_task.readlines()
        for line, details in enumerate(task_line):
            print(f"{line + 1}: {details}")
            # line 

            # new_desc = input("Enter new task description: ")



edit_task()
