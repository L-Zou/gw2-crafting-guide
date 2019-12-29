from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from obj.NumberValidators import NumberValidator
from examples import custom_style_3
from obj.Recipe import Recipe
from obj.CraftingTree import Node
from helpers.ItemNametoID import get_item_id

import requests

import itertools
import threading
import time
import sys

import json
from requests.exceptions import HTTPError

url="https://api.guildwars2.com"
response = requests.get(url)

done = False
def loading_animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rgenerating recipe tree ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

print(r"""
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
    item_id = get_item_id(answers['item_name'])

    if item_id is None:
        print("Unable to find requested item.")
    else: 
        recipe = Recipe(item_id, answers['amount'], answers['buy_method'])
        t = threading.Thread(target=loading_animate)
        t.start()

        crafting_tree = recipe.create_craft_tree_driver()
        done = True
        print("")
        print("")
        print("RECIPE TREE")
        print("=======================================================")
        print(crafting_tree)



    #with open('UserInput.json', 'w') as outfile:
        #json.dump(answers, outfile)