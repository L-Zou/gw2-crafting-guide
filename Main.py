import requests
import json
from obj.Recipe import Recipe
from requests.exceptions import HTTPError

with open('UserInput.json', 'r') as input_file:
    data = input_file.read()

user_input = json.loads(data)
item = Recipe(user_input['item_id'], user_input['amount'], user_input['buy_method'], user_input['daily_craft'])

print(item.create_craft_tree_driver().children[0].children[0].data)
url="https://api.guildwars2.com"
response = requests.get(url)

if not response:
    print("An error occured.")
else:
    print("Good")