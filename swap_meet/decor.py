from swap_meet.item import Item
from uuid import uuid1


class Decor(Item):
    def __init__(self, id=uuid1().int, width=0, length=0, condition=0.0):
        self.id = id
        self.width = width
        self.length = length
        self.condition = condition
        pass

    def get_category(self):
        return "Decor"

    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."
