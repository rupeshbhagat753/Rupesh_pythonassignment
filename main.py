
from todo_operations import add_task , delete_task , view_tasks
from utils import get_input

#  To Display the main menu for the to-do list app.
def display_menu():   
    print("To-Do List App")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")



def main():
    task_list = []
    
    while True:
        display_menu()
        
        choice = get_input("Choose an option : ")

        if choice == '1':
            task = get_input("Enter a new task: ")
            add_task(task)
            print("Task Added Sucessfully.")
            
        elif choice == '2':
            all_tasks = view_tasks()
            if all_tasks:
                print("Your To-Do Tasks List.")
                for index, task in enumerate(all_tasks):
                    print(f"{index + 1}. {task}")
            else :
                print("Your To-Do Tasks list is Empty.")
                
        elif choice == '3':
            all_tasks = view_tasks()
            if all_tasks:
                index = int(get_input("Select the Index of the task to delete.")) -1
                deleted_task = deleted_task(index)
                if deleted_task is not None:
                    print(f"{deleted_task} task deleted sucessfully.")
                else:
                    print("Selected Index is not valid.")
                    
        elif choice == '4':
            print("Exiting To-Do List app. Be sure To come again.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# To Run the app
if __name__ == "__main__":
    main()