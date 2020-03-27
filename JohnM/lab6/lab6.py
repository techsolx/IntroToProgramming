#!/usr/bin/env python3
"""
Play rock-paper-scissors with the computer.
The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
Let's list all the cases:
    - rock vs rock (tie)
    - rock vs paper
    - rock vs scissors
    - paper vs rock
    - paper vs paper
    - paper vs scissors
    - scissors vs rock
    - scissors vs paper
    - scissors vs scissor
"""

import random

choices = ["rock", "paper", "scissors"]


def check_winner(u, c):
    if u == "rock" and c == "scissors":
        return True
    elif u == "paper" and c == "rock":
        return True
    elif u == "scissors" and c == "paper":
        return True
    else:
        return False


def main():
    while True:
        question = input("Would you like to play Rouchambaeu, y/n [y]? ")
        if question == "n":
            quit()
        else:
            human_player = input("\nType in rock, paper or scissors ")
            computer_player = random.choice(choices)

        if human_player == computer_player:
            print(
                f"\nTie you picked {human_player},"
                f"the computer picked {computer_player}!\n"
            )
        else:
            result = check_winner(human_player, computer_player)
            if result:
                print(
                    f"\nYou win, you picked {human_player},"
                    f"the computer picked {computer_player}\n"
                )
            else:
                print(
                    f"\nYou lost, you picked {human_player},"
                    f"the computer picked {computer_player}\n"
                )


if __name__ == "__main__":
    main()
