#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program runs a factorial loop for positive integers

import string


def main():
    # this function uses a while loop
    loop_counter = 1
    product = 1

    # this function runs the "factorial loop" program
    # input
    print("Welcome!")
    num_integer = str(input("Please enter a positive integer: "))

    # process and output
    try:
        num_integer = int(num_integer)
        if num_integer >= 0:
            while loop_counter <= num_integer:
                product = product * loop_counter
                loop_counter = loop_counter + 1
            print("{0}! = {1}".format(num_integer, product))
        elif num_integer < 0:
            print("That integer is a negative number!")
    except Exception:
        print("{0} is invalid data.".format(num_integer))
    finally:
        print("")
        print("Thanks for participating!")


if __name__ == "__main__":
    main()
