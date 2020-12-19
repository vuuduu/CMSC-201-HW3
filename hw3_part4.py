"""
File:         hw3_part3.py
Author:       Vu Nguyen
Date:         9/24/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This program takes in two list with the same length and
              merged them into the same list.
"""

if __name__ == "__main__":
    num_element = int(input("How many elements do you want in each list? ").strip())
    first_list = []
    second_list = []
    merged_list = []

    # This loop add elements into the first list
    for i in range(num_element):
        user_num = input("What do you want to put in the first list? ").strip()
        first_list.append(user_num)

    # This loop add elements into the second list
    for i in range(num_element):
        user_num = input("What do you want to put in the second list? ").strip()
        second_list.append(user_num)

    # This loop combine two list
    for i in range(num_element):
        merged_list.append(first_list[i])
        merged_list.append(second_list[i])

    print("The first list is:", first_list)
    print("The second list is:", second_list)
    print("The merged list is:", merged_list)
