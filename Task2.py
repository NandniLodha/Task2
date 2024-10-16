# To-Do List Application

# A dictionary to store the tasks
todo_list = {}

def add_task(task_name):
    task_id = len(todo_list) + 1
    todo_list[task_id] = {"task": task_name, "status": "Pending"}
    print(f"Task '{task_name}' added successfully!")

def update_task(task_id, new_status):
    if task_id in todo_list:
        todo_list[task_id]["status"] = new_status
        print(f"Task {task_id} updated to '{new_status}'!")
    else:
        print(f"Task {task_id} not found.")

def delete_task(task_id):
    if task_id in todo_list:
        del todo_list[task_id]
        print(f"Task {task_id} deleted!")
    else:
        print(f"Task {task_id} not found.")

def view_tasks():
    if todo_list:
        print("\nTo-Do List:")
        for task_id, task_info in todo_list.items():
            print(f"ID: {task_id}, Task: {task_info['task']}, Status: {task_info['status']}")
    else:
        print("No tasks in the list.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                task_name = input("Enter the task description: ")
                add_task(task_name)
            
            elif choice == 2:
                task_id = int(input("Enter the task ID to update: "))
                new_status = input("Enter the new status (Pending/Completed): ")
                update_task(task_id, new_status)
            
            elif choice == 3:
                task_id = int(input("Enter the task ID to delete: "))
                delete_task(task_id)
            
            elif choice == 4:
                view_tasks()
            
            elif choice == 5:
                print("Exiting the To-Do List application.")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
