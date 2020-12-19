"""
File:         hw3_part2.py
Author:       Vu Nguyen
Date:         9/20/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This program calculate the Faulhaber's Summation
              given its formula.
"""

if __name__ == "__main__":
    power_p = int(input("What is the power we want to use? ").strip())
    num_term = int(input("How many term do we want to calculate? ").strip())

    if (power_p < 0) or (num_term < 0):
        print('Both "The power" and "The number of terms" must be non-negative? ')
    else:
        faulhaber_sum = 0
        for i in range(1, num_term + 1):
            faulhaber_sum += i**power_p
        print("The Faulhaber sum is", faulhaber_sum)
