#wave 2
import uuid


class Item:
    """Represents a generic item that can be swapped."""

    def __init__(self, id=None):
        """
        Initialize an Item.
        param id: optional integer id; defaults to a unique value.
        """
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def get_category(self):
        """
        Return the category name of this class.
        """
        return self.__class__.__name__
    
#wave 3
    def __str__(self):
        """
        Return a human-readable string for this item.
        """
        return f"An object of type {self.get_category()} with id {self.id}."