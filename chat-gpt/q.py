#!python
# cython: language_level=3

import os
import argparse
import dotenv
import openai
from termcolor import colored

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

print(colored("Question> ", "cyan"))


def main(q: str):
    try:
        if len(q) > 0:
            statement = q
        else:
            statement = input()
        message = ""
        while statement != "q":
            if statement == "c":
                statement = "please continue"
            elif len(message) > 0:
                print(colored(message, "light_magenta"))
                print("=====================")
                message = ""
            print(colored(statement, "cyan"))
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=statement,
                temperature=0.6,
                max_tokens=100,
            )
            print(colored(response.choices[0].text, "green"))
            print("press (c): read more, (q): quit")
            statement = input()
            message += response.choices[0].text
        print(colored(message, "light_magenta"))
    except Exception as e:
        print(colored(f"fail: {e}", "red"))


def get_arguments():
    parser = argparse.ArgumentParser()
    # +: # of args. [1,n], *: [0,n]
    # dest: name
    parser.add_argument(nargs="*", help="Example) how are you doing?", dest="question")

    question = parser.parse_args().question
    return question


if __name__ == "__main__":
    q = get_arguments()
    nq = " ".join(q)
    main(nq)
