
#!python
# cython: language_level=3

import os
import dotenv
import openai
from termcolor import colored

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

print(colored('Question> ', 'cyan'))

try:
    statement = input()
    message = ''
    while statement != 'exit':
        if statement == 'c': 
            statement = 'please continue'
        elif len(message) > 0:
            print(colored(message, 'light_magenta'))
            print('=====================')
            message = ''
        print(colored(statement, 'cyan'))
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=statement,
            temperature=0.6,
            max_tokens=100
        )
        print(colored(response.choices[0].text, 'green'))
        print('press (c): read more, (exit): quit')
        statement = input()
        message += response.choices[0].text
    print(colored(message, 'light_magenta'))
except Exception as e:
    print(colored(f'fail: {e}', 'red'))


