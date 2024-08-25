tasks = []

def add_task():
    task = input('Enter your task:')
    tasks.append(task)
    print(f"Task '{task}' added")
    
def view_task():
    if tasks:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks yet.")

    
        
def delete_task():
    view_task()
    if tasks:
        task_num = int(input("Enter the task number to delete:"))
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number")


def main():
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")
            
            
            
if __name__ == "__main__":
    main()            
                
                                    
        
