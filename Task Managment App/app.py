def task():
    tasks = [] #Empty list to store tasks
    print("---WELCOME TO TASK MANAGMENT APP---")

    total_tasks = int(input("Enter how many tasks you want to add = "))

    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter task {i} = ") #Enter task here.
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1-add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been added successfully...")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter the new task name = ")
                index = tasks.index(updated_val)
                tasks[index] = up
                print(f"Updated Task {up}")

        elif operation == 3:
            del_val = input("Enter the task you want to delete = ")
            if del_val in tasks:
                index = tasks.index(del_val)
                del tasks[index]
                print(f"Task {del_val} has been deleted successfully...")

        elif operation == 4:
            print(f"Total tasks are: {tasks}")

        elif operation == 5:
            print("Closing the program...")
            break
        else:
            print("Invalied Operation")
task()

