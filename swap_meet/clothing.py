from swap_meet.item import Item
from uuid import uuid1


class Clothing(Item):
    def __init__(self, id=uuid1().int, fabric="Unknown", condition=0.0):
        super().__init__(id, condition)
        self.fabric = fabric
        pass

    def get_category(self):
        return "Clothing"

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
