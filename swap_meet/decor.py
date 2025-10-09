from swap_meet.item import Item
from uuid import uuid1


class Decor(Item):
    def __init__(self, id=uuid1().int, width=0, length=0, condition=0.0):
        super().__init__(id, condition)
        self.width = width
        self.length = length

    def get_category(self):
        return "Decor"

    def __str__(self):
        return f"{super().__str__()} It takes up a {self.width} by {self.length} sized space."
