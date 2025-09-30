import uuid
# Wave 2:


class Item:
    def __init__(self, id=None):
        self.id = id or uuid.uuid1().int

    def get_category(self):
        return "Item"
