def task():
    tasks = [] #Empty list to store tasks
    print("---WELCOME TO TASK MANAGMENT APP---")

    total_tasks = int(input("Enter how many tasks you want to add = "))

    for i in range(total_tasks + 1):
        task_name = input(f"Enter task {i} = ")
