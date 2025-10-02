#wave 2
import uuid


class Item:

    def __init__(self, id=None, condition=0.0):
        self.id = id or uuid.uuid4().int
        self.condition = condition

    def get_category(self):
        return "Item"

# wave 3
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

# wave 5
    def condition_description(self):
        if self.condition == 5:
            return "Like new! mint condition!"
        elif self.condition >= 4:
            return "Gently used ! still in great shape"
        elif self.condition >= 3:
            return "Used but works fine but shows some wear."
        elif self.condition >= 2:
            return "Well-worn, you probably want a glove for this one"
        elif self.condition >= 1:
            return "Heavily used, might need some love"
        else:
            return "Barely holding together, handle with care"
