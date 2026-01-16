import json #JavaScript Object Notation 

#Storation Tasks in JSON file using Dictionary
file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}

def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file)
    except:
        print("Failed to save.")

def view_tasks():
    pass

def create_task(tasks):
    description = input("Enter the task description: ").strip()

def mark_task_complete():
    pass

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            create_task()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            print("Goodbye!")
            break 
        else:
            print("Invalid Choice! Please try again.")

main()