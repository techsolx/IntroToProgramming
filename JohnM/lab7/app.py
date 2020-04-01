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

user_guesses = []


def get_user_input():
    """
    get the users input,
    return the result.
    """
    u_int = int(input("Enter an integer between 1 and 10: "))
    user_guesses.append(u_int)
    if u_int in range(1, 11):
        return u_int
    else:
        print(f"That number is not in the range of numbers I am looking for,"
              f"please try again.")
        get_user_input()


def check_em(first_int, second_int):
    """
    check 2 integers, if they are the same
    return a match, if they are different,
    return higher or lower.
    """
    if first_int == second_int:
        return True
    elif first_int > second_int:
        print(f"Too low")
    else:
        print(f"Too high")


def main():
    guesses = 0
    print(f"Initial setting of guesses is {guesses}")
    question = input(
        f"Would you like to guess a number between "
        f"1 and 10, y/n [y] "
    )
    if question == "n":
        quit()
    else:
        c_int = random.randint(1, 10)
    while guesses <= 10:
        guesses += 1
        print(f"Current setting of guesses is {guesses}")
        u_int = get_user_input()
        if check_em(c_int, u_int):
            print(f"You got it, it took you {guesses} tries!\n")
            main()
        else:
            u_int = get_user_input()
            check_em(c_int, u_int)


if __name__ == "__main__":
        main()
