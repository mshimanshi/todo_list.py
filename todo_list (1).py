tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else: 
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}.{task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    show_tasks()
    try:
        task_no = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_no < len(tasks):
            removed = tasks.pop(task_no)
            print(f"Task '{removed}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n1. Show Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid choice. Please try again.")