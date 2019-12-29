import requests
import json
from requests.exceptions import HTTPError

url1 = "http://www.gw2spidy.com/api/v0.9/json/item-search/"
url2 = "https://api.guildwars2.com/v2/items/"
        
def get_item_id(item_name):
    search_data = requests.get(url1 + str(item_name) + "/1") 
    if search_data.json()['total'] == 0: 
        return None
    else:
        for results in search_data.json()['results']:
            if results['name'] == item_name:
                return results['data_id']
        return None

def get_item_name(item_id):
    item_data = requests.get(url2 + str(item_id))
    item_name = item_data.json()['name']
    return item_name