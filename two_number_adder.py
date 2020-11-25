#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: November 2020
# This program adds 2 numbers

import math


def main():
    # This function gets the value of 2 numbers and outputs their sum

    print("This program adds two numbers")
    number_1_Str = input("Please enter the first number: ")
    number_2_Str = input("Please enter the second number: ")
    number_1 = int(number_1_Str)
    number_2 = int(number_2_Str)
    total = number_1 + number_2
    print("Then the equation is {} + {} = {}".
          format(number_1_Str, number_2_Str, total))


if __name__ == "__main__":
    main()
