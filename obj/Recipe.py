import requests
import json
from requests.exceptions import HTTPError
from .CraftingTree import Node

class Recipe(object):
    def __init__(self, item_id, amount, buy_method):
        self.item_id = item_id
        self.amount = amount
        self.buy_method = buy_method
        #self.daily_craft = daily_craft
        self.root = Node({'item_id': self.item_id, 'count': self.amount})

    def get_recipe_id(self, item_id):
        recipe_search_parameters = {"output": item_id}
        url = "https://api.guildwars2.com/v2/recipes/search"
        #multiple recipes profession dependent deal with later
        recipe_id_list = requests.get(url, params=recipe_search_parameters) 
        if recipe_id_list.json():
            recipe_id = recipe_id_list.json()[0]
            return recipe_id
        else:
            return None

    def get_recipe_ingrediants(self, item_id):    
        recipe_parameters = {"ids": self.get_recipe_id(item_id)}
        url = "https://api.guildwars2.com/v2/recipes/" + str(recipe_parameters['ids'])
        recipe = requests.get(url)
        ingredients = recipe.json()['ingredients']
        return ingredients

    def get_tpcost(self, item_data):
        total = 0
        url = "https://api.guildwars2.com/v2/commerce/prices/"
        tp_data = requests.get(url + str(item_data['item_id']))
        tp_price = tp_data.json()['buys']['unit_price']
        total += tp_price * item_data['count']
        return total

    def create_craft_tree(self, root, item_id):
        if self.get_recipe_id(item_id) is None:
            return root
        else:
            for ingredient in self.get_recipe_ingrediants(item_id):
                root.add_child(self.create_craft_tree(
                    Node([ingredient, 
                    self.get_tpcost(ingredient)]),
                    ingredient['item_id']))
            return root

    def create_craft_tree_driver(self):
        return self.create_craft_tree(self.root, self.item_id)