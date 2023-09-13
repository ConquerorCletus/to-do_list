import show
import add_task
import edit_task
import details
import delete
import reminder
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    


def main():
    while True:
        clear_screen()
        print('''

              \t\t\t\t________WELCOME TO TASK MANAGER_________

              \t\t\t\tWE help you manage your day

              \t\t\t\tWhat would you like to do:

              \t\t\t\t(1) ADD A TASK
              \t\t\t\t(2) EDIT A TASK
              \t\t\t\t(3) SHOW YOUR TASKS
              \t\t\t\t(4) DELETE A TASK
              \t\t\t\t(5) QUIT PROGRAM
              
              ''')
        option = int(input("Enter your Option: "))
        if option == 1:
            add_task.add_task()
        elif option == 2:
            edit_task.edit_task()
        elif option == 3:
            show.show()
        elif option == 4:
            delete.delete_task()
        elif option == 5:
            print("EXITING PROGRAM!!!")
            break
        else:
            print("INVALID OPTION. ENTER BETWEEN OPTION (1-5)")

        choice = input("Do you want to continue? Yes/no : ")
        if choice.lower() != 'yes':
            print("GOODBYE !! EXITING PROGRAM !!")
            break



main()
