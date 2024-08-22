import os

# Initialize an empty list to store the tasks
tasks = []

def show_menu():
    print("\nTo-Do List Application")
    print("=======================")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Clear All Tasks")
    print("6. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks in the to-do list.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def update_task():
    view_tasks()
    if tasks:
        task_number = int(input("\nEnter the task number to update: "))
        if 0 < task_number <= len(tasks):
            new_task = input("Enter the new task: ")
            tasks[task_number - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number!")

def delete_task():
    view_tasks()
    if tasks:
        task_number = int(input("\nEnter the task number to delete: "))
        if 0 < task_number <= len(tasks):
            tasks.pop(task_number - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")

def clear_tasks():
    global tasks
    tasks = []
    print("All tasks cleared successfully!")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            clear_tasks()
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
