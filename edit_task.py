"""
This module is responsible for editing the task.
"""

import os
import datetime
import show

def edit_task():
    show.show()
    selected_task = show.select()

    with open(selected_task, 'r') as editted_task:
        task_content = editted_task.read()
        print(task_content)


edit_task()
