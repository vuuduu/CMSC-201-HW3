"""
File:         hw3_part5.py
Author:       Vu Nguyen
Date:         9/24/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs calculate the part of the eightfold path based on
              a particular angle the user enter. (Preferably divisible by 45)
"""

if __name__ == "__main__":
    angle = int(input("Enter an angle to determine the point on the Eightfold Path: "))
    if (angle % 45) != 0:
        print("You've not reached Enlightenment yet! (Try angle divisible by 45)")
    else:
        eightfold_path = ["Right Resolve", "Right View", "Right Samdhi", "Right Mindfulness",
                          "Right Effort", "Right Livelihood", "Right Conduct", "Right Speech"]
        # This formula help to find the index of the eightfold_path list. (0-7)
        angle = int((((angle / 360) % 1) * 360) / 45)
        print("You have selected", eightfold_path[angle])
