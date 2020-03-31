#!/usr/bin/env python3

"""
Lab 7: Guess the Number, the computer will choose
a `random int` between 1 and 10.
The user will then try to guess the number,
and the program will tell them whether they're right or wrong.

Tell the user whether their guess is above ('too high!')
or below ('too low!') the target value.

Let them keep guessing in a `while` loop.
Keep track of how many guesses the user has made, and tell them at the end.

Using a `while` loop, allow the user to guess 10 times.
If they fail to guess the number after 10 tries, the user is told they've lost.

Tell the user whether their current guess is closer than their last.

Swap the user with the computer:
the user will pick a number,
and the computer will guess until they get it right.
"""

import random


def get_numbers():
    c_int = random.randint(1, 10)
    u_int = int(input("Enter an integer between 1 and 10"))
    if u_int in range(1, 11):
        return c_int, u_int
    else:
        print(f"That number is not in the range of numbers I am looking for,"
              f"please try again.")
        get_numbers()


def main():
    while True:
        question = input(f"Would you like to guess a number between"
                         f"1 and 10, y/n [y] ")
        if question == "n":
            quit()
        else:
            pass


if __name__ == "__main__":
    main()
