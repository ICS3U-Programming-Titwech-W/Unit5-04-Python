#!/usr/bin/env python3

# Created by: Titwech Wal
# Created on: May.19 .2022
# program aloows user to enter sign
# with two numbers then it will calculate
# the answer


def calaculate(sign, first_num, second_num):

    if sign == '/':
        result = first_num / second_num
    elif sign == '*':
        result = first_num * second_num
    elif sign == '%':
        result = first_num % second_num
    elif sign == '+':
        result = first_num + second_num
    else:
        result = first_num - second_num
    return result


def main():

    print("This program will perform the calculations between two numbers.")
    print("")

    # get user input
    user_sign = input("Enter the operation you'd to perform (+, -, *, /, %): ")
    print("")

    # See's if user enters valid operation
    if user_sign == "+" or user_sign == "-" or user_sign == "/" \
       or user_sign == "*" or user_sign == "%":

        # gets first number from user
        first_num_string = input("Enter the first number: ")

        try:
            # converts from a string to float
            first_num_float = float(first_num_string)

            # gets the second number as string
            second_num_string = input("Enter the second number: ")

            try:
                # converts from string to float
                second_num_float = float(second_num_string)

                # assigns a variable to function call,
                # giving it a returned value.
                user_results = calaculate(user_sign,
                                          first_num_float, second_num_float)

                # displays results to user
                print("The results of {} {} {} is {:,.2f}."
                      .format(first_num_float, user_sign,
                              second_num_float, user_results))
                print("")

            # checks for any invalid cases
            except Exception:
                print("{} is not a valid number.".format(second_num_string))

        # checks for any invalid cases
        except Exception:
            print("{} is not a valid number.".format(first_num_string))

    else:
        print("{} is not one of the following operations.".format(user_sign))


if __name__ == "__main__":
    main()
