from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from PyInquirer import Validator, ValidationError
from examples import custom_style_3

import requests
import json
from requests.exceptions import HTTPError

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
            if(int(document.text) < 1):
                raise ValidationError(
                    message='Please enter a number above 0',
                    cursor_position=len(document.text))
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text)) 

url="https://api.guildwars2.com"
response = requests.get(url)

print("""
=================================================================
   _______          _____     _____            __ _            
  / ____\ \        / /__ \   / ____|          / _| |           
 | |  __ \ \  /\  / /   ) | | |     _ __ __ _| |_| |_ ___ _ __ 
 | | |_ | \ \/  \/ /   / /  | |    | '__/ _` |  _| __/ _ \ '__|
 | |__| |  \  /\  /   / /_  | |____| | | (_| | | | ||  __/ |   
  \_____|   \/  \/   |____|  \_____|_|  \__,_|_|  \__\___|_|   
 =================================================================

 """)

if not response:
    print("GW2 Crafter is offline.")
else:
    questions = [
        {
            'type': 'input',
            'name': 'item_name',
            'message': 'What item would you like to craft?'
        }, 
        {
            'type': 'input',
            'name': 'amount',
            'message': 'How many copies of this item would you like to craft?',
            'validate': NumberValidator,
            'filter': lambda val: int(val)
        },
        {
            'type': 'list',
            'name': 'buy_method',
            'message': 'How will you purchase the crafting ingredients you need?',
            'choices': ['Place Order', "Buy Instantly"],
            'filter': lambda val: val.lower()
        },
    ]

    answers = prompt(questions, style=custom_style_3)

    with open('UserInput.json', 'w') as outfile:
        json.dump(answers, outfile)