"""This module is responsible for reminders"""
import time
import show
import details
import schedule
import json
import threading

def alert():
    print("Your task reminder")
    print("Your Task reminder!!!")

def remind_me():
    """This Function reminds me of a task"""
    show.show()
    task = show.select()

    with open(task, 'r') as task:
        tasks = json.load(task)
        remind_time = tasks['Deadline']
        schedule.every().day.at(remind_time).do(alert)

        while True:
            schedule.run_pending()
            time.sleep(1)

        reminder_thread = threading.Thread(target=remind_me)
        reminder_thread.start()
        print("Task scheduled!!")


# remind_me()
