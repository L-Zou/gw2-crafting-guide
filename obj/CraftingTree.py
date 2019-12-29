from helpers.ItemNametoID import get_item_name
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self, level=-1):
        if(level == -1): 
            ret = "\t"*level+ str(self.data['count']) + "x" + repr(get_item_name(self.data['item_id']))+"\n"
            for child in self.children:
                ret += child.__str__(level+1)
            return ret
        else: 
            ret = "\t"*level+" └── "+ str(self.data[0]['count']) + "x" +repr(get_item_name(self.data[0]['item_id']))+"\n"
            for child in self.children:
                ret += child.__str__(level+1)
            return ret
    #"├── ""│   " "└── " "    "
    def __repr__(self):
        return '<tree node representation>'

    def add_child(self, ingredient):
        self.children.append(ingredient)