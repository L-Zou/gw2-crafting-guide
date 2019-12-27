import requests
import json
from requests.exceptions import HTTPError

class Recipe(object):
    def __init__(self, item_id, amount, buy_method, daily_craft):
        self.item_id = item_id
        self.amount = amount
        self.buy_method = buy_method
        self.daily_craft = daily_craft

    def get_recipe_id(self):
        recipe_search_parameters = {"output": self.item_id}
        url = "https://api.guildwars2.com/v2/recipes/search"
        #multiple recipes profession dependent deal with later
        recipe_id_list = requests.get(url, params=recipe_search_parameters) 
        recipe_id = recipe_id_list.json()[0]
        return recipe_id

    def get_recipe_ingrediants(self):    
        recipe_parameters = {"ids": self.get_recipe_id()}
        url = "https://api.guildwars2.com/v2/recipes/" + str(recipe_parameters['ids'])
        recipe = requests.get(url)
        if not recipe:
            return 0
        else:
            ingredients = recipe.json()['ingredients']
            return ingredients
    
    def get_cost(self):
        total = 0
        url = "https://api.guildwars2.com/v2/commerce/prices/"
        for ingredient in self.get_recipe_ingrediants():
            tp_data = requests.get(url + str(ingredient['item_id']))
            tp_price = tp_data.json()['buys']['unit_price']
            total += tp_price * ingredient['count']
        return total