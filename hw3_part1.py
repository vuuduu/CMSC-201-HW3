"""
File:         hw3_part1.py
Author:       Vu Nguyen
Date:         9/19/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This program asks the user how many task they have and display
              any incomplete task that they haven't completed.

"""

if __name__ == "__main__":
    num_task = int(input("How many task do you have? ").strip())
    list_of_task = []
    if num_task <= 0:
        print("That's either negative or zero!")
    else:

        # This loop asks what type of task the user have
        for i in range(num_task):
            user_tasks = input("Enter the task: ").strip()
            list_of_task.append(user_tasks)

        # This loop shows the tasks that the user input
        print("Here are your tasks:")
        for i in list_of_task:
            print(str(list_of_task.index(i) + 1) + ".", i)

        # This loop ask which task you've completed and displayed the one you didn't
        unfinished_task = []
        for i in range(num_task):
            query_complete = input('Have you completed "' + list_of_task[i] + '" ? (yes/no) ').lower()
            if query_complete == "no":
                unfinished_task.append(list_of_task[i])

        if not unfinished_task:
            print("You have completed all of your tasks!")

        for i in unfinished_task:
            print("The remaining task is", i)





