"""
File:         hw3_part3.py
Author:       Vu Nguyen
Date:         9/20/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This program allow user to add or remove name based on
              the number of step the user input. It also compare the
              names and display the max_length name if ask.
"""

if __name__ == "__main__":
    num_step = int(input("How many step do you want to run? ").strip())
    name_list = []
    print("Here are your list of command:\n" +
          "add 'Enter a name'\n" +
          "remove 'Enter a name'\n" +
          "max")
    for i in range(num_step):
        command = input("Enter a command: ")
        list_command = command.split(sep=" ")

        # add name to the list
        if list_command[0] == "add":
            name_list.append(list_command[1])
            print(list_command[1], "added")

        # remove name from the list
        elif list_command[0] == "remove":
            if list_command[1] not in name_list:
                print("The name you're trying to remove is not in the list!")
            else:
                name_list.remove(list_command[1])
                print(list_command[1], "removed")
        elif list_command[0] == "max":
            if not name_list:
                print("You have an empty list!")
            else:
                # the -1 is to guarantee that the first string (even if it's 0) will be set as max_string_length.
                max_string_length = -1
                for element in name_list:

                    # This if condition set so that only the string with biggest len can be set as max_string
                    if len(element) > max_string_length:
                        max_string_length = len(element)
                        max_string = element

                    # This elif statement compare element and order them in Lexicographic order.
                    elif len(element) == max_string_length:
                        e_list = []
                        max_list = []

                        # This for loop store each character of the element into e_list
                        for ele_index in element:
                            e_list.append(ele_index)

                        # This for loop store each character into max_list
                        for max_index in max_string:
                            max_list.append(max_index)

                        # This for loop compare the two list char by char
                        for index in range(len(e_list)):
                            if e_list[index] > max_list[index]:
                                max_string = element
                print("The max name is", max_string)



