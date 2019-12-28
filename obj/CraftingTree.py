class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, ingredient):
        self.children.append(ingredient)

    def render_tree(self, ):
        #"├── ""│   " "└── " "    "
        return 0