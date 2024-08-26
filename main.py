class Task:
    def __init__(self,description):
        self.description = description
        
    def __str__(self):
        return self.description
    
        
class TodoList:
    def __init__(self):
        self.tasks = []





    def add_task(self, task_description):
        task = Task(task_description)
        self.tasks.append(task)
        print(f"Task '{task}' added")
        
    def view_task(self):
        if self.tasks:
            print("Your tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks yet.")

        
            
    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number")


def main():
    todo_list = TodoList()
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        
        if choice == '1':
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_task()
        elif choice == '3':
            todo_list.view_task()
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")
            
            
            
if __name__ == "__main__":
    main()            
                
                                    
        
