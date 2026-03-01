# To do list
tasks = []

def add():
    user_input1 = input("Enter your task: ")
    user_input2 = input("Enter Priority (High,Medium,Low): ")
    user_input3 = input("Enter the deadline (date/month): ")
    task = {
        "Name": user_input1,
        "Priority": user_input2,
        "Deadline": user_input3
    }

    tasks.append(task)
    print("Task Added Successfully...")


def show():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for index, value in enumerate(tasks):
            print(f"{index}->Task:{value['Name']} \n Priority:{value['Priority']} \n   Deadline:{value['Deadline']}")


def remove():
    show()
    if len(tasks) == 0:
        return
    num = int(input("Enter task number to remove: "))   
    if num >= 0 and num < len(tasks):
        tasks.pop(num)
        print("Task Removed Successfully...")
    else:
        print("Invalid Task Number!")

while True:
    print("\n1 -> Add Task")
    print("2 -> Show Task")
    print("3 -> Remove Task")
    print("4 -> Exit")

    main_input = input("Enter your choice: ")

    if main_input == "1":
        add()
    elif main_input == "2":
        show()
    elif main_input == "3":
        remove()
    elif main_input == "4":
        print("Program Ended.")
        break
    else:
        print("Invalid Choice!")