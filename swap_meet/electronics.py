from swap_meet.item import Item
from uuid import uuid1


class Electronics(Item):
    def __init__(self, id=uuid1().int, type="Unknown", condition=0.0):
        self.id = id
        self.type = type
        self.condition = condition
        pass

    def get_category(self):
        return "Electronics"

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
