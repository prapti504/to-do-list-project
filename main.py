# Load tasks from file
try:
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    tasks = []

while True:
    print("\n===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

        with open("tasks.txt", "w") as file:
            for t in tasks:
                file.write(t + "\n")

        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_num = int(input("Enter task number to delete: "))

            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)

                with open("tasks.txt", "w") as file:
                    for t in tasks:
                        file.write(t + "\n")

                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")