#wave 2
import uuid


class Item:

    def __init__(self, id=None):
        self.id = id or uuid.uuid4().int

    def get_category(self):
        return "Item"