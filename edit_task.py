"""
This module is responsible for editing the task.
"""

import os
import datetime
import show
import select_task

def edit_task():
    display_task = show.show()
    selected_task = select_task.select()
    
    with open(selected_task, 'a') as editted_task:

# edit_task()
