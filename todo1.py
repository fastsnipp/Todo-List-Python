def task():
    task = []  # empty list
    print("Welcome To the To Do List app . created By SOHAN")
    total_task_taken = input("Enter How Many Tasks You Want To add")
    total_task_taken = int(total_task_taken)
    for i in range(1, total_task_taken + 1):
        task_name = input(f"Enter Task {i}= ")
        task.append(task_name)
    print(f"Okay! So According To You Today's Tasks Are : ", task)
    while True:
        operation = input("Enter 1-add\n2-update\n3-delete\n4-view\n5-stop")
        operation = int(operation)
        if operation == 1:
            add = input("Enter Your Task ")
            task.append(add)
            print("Your Task Is added")
        elif operation == 2:
            up_value = input("Enter The Task You Want To Update ")
            if up_value in task:
                up = input("Enter a new updated Task ")
                ind = task.index(up_value)
                task[ind] = up
                print("Your Task Is updated")
            else:
                print("Task not found")
        elif operation == 3:
            del_value = input("Enter The Task You Want To Delete ")
            if del_value in task:
                ind=task.index(del_value)
                del task[ind]
                print("Task deleted successfully")
            else:
                print("Task not found")
        elif operation == 4:
            print("Your Tasks Are : ", task)
        elif operation == 5:
            print("Stopping The task")
            break
        else:
            print("Invalid operation")
task()