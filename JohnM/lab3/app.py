#!/usr/bin/env python3

import random
import time

responses = ["It is certain.",
             "It is decidedly so.",
             "Without a doubt.",
             "Yes - definitely.",
             "You may rely on it.",
             "As I see it, yes.",
             "Most likely.",
             "Outlook good.",
             "Yes.",
             "Signs point to yes.",
             "Reply hazy, try again.",
             "Ask again later.",
             "Better not tell you now.",
             "Cannot predict now.",
             "Concentrate and ask again.",
             "Don't count on it.",
             "My reply is no.",
             "My sources say no.",
             "Outlook not so good.",
             "Very doubtful.",
             ]


def ask_question():
    print(f"\nPlay magic 8Ball or type 'quit()' to quit.")
    question = input("Please ask a question? ")
    if question == "quit()":
        quit()
    elif "?" in question:
        answer = responses[rand_numb]
        time.sleep(random.randint(1, 3))
        print(f"\n{answer}\n")
    else:
        print(f"{question} doesn't look like a question, "
              f"it looks like a statement? \n")
        ask_question()


while True:
    rand_numb = random.randint(0, len(responses)-1)
    ask_question()
