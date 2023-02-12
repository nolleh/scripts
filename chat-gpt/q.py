import os
import dotenv
import openai
from termcolor import colored
from pandas import DataFrame
from tabulate import tabulate

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

print(colored('Question> ', 'cyan'))
statement = input()
try:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=statement,
        temperature=0.6,
    )

    df = DataFrame(response.choices)

    print(colored(response.choices[0].text, 'green'))
    print(colored(f'response len:{len(df)}', 'light_magenta'))

    print('=====================')
    
    print(colored(str(tabulate(df, headers = 'keys', tablefmt='psql')), 'light_magenta'))

    # print(colored(str(response), 'blue'))
        
except Exception as e:
    print(colored(f'fail: {e}', 'red'))


