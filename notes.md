To do list app



Features of the To-do List app
1. It manage task - deleting, adding and editing
2. store time (date/day)
3. Reminder.

main program
1.The option as a switch statement
2.Loop until exit is called.

Functions/modules.
1.add task function: **progress = 100%** 
- name of task
- Time and date to carryout task
- store in a file

2.delete task function **progress = 100%** 
- delete task

3.edit task function **progress = 100%**
- Enable to edit task through the add task function

4.Reminder function
- Reminder when it is time for the task.

5. list/show task **progress = 100%**
- show the task through reading from the file.

## Pseudocode 
### add task function.**progress = 100%** 
- import datetime modules
- def add_task()
- input of task name
- user would input time
- record time
- input task description
- open a file in append mode
- store file as format(task/task_name.txt)

### delete task function **progress = 100%** 
- import OS
- def delete_task()
- prompt "are you sure you want to delete?"
- collect input yes/no
- delete file

### Edit task function **progress = 100%** 
- import OS
- import datetime
- def edit_task()
- Open file in read (r+) mode
- input/edit description
- Record/input time.

### show() function **progress = 100%** 
- loop throught the task in that directory.

### select() **progress = 100%** 
- select a task based on index


### Reminder Functions **progress = 0%** 
- def remind_me()
- Prompt (name of task + description of task + Time)

### show task function **progress = 100%** 
- import OS
- def show_task()
- Read file (i.e task directory) 
