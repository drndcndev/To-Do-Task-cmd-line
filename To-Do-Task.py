import os

TASKS_FILE = "tasks.txt" # File to store tasks


def load_tasks():
    """Load tasks from a file if it exists."""

    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    return []


def add_tasks(tasks):
    """Add a new task to the list."""

    task = input("Enter new task: ").strip()

    if task:
        tasks.append(task)
        print("Task added!\n")
    else:
        print("Task cannot be empty!\n")


def display_tasks(tasks):
    """Display the current tasks."""

    if not tasks:
        print("\nNo tasks found!\n")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    print("\n")


def delete_tasks(tasks):
    """Delete a task from the list."""

    display_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Removed: {removed_task}\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


def save_tasks(tasks):
    """Save tasks to a file."""

    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def main():
    tasks = load_tasks()

    while True:
        print("To-Do List App")
        print("[1] Add Task")
        print("[2] View Tasks")
        print("[3] Delete Task")
        print("[4] Save & Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            delete_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice, please try again!\n")



if __name__ == "__main__":
    main() 
