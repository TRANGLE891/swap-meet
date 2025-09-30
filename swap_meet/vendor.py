class Vendor:
    """
    Represents a swap-meet participant with an inventory of items.
    """

    def __init__(self, inventory=None):
        """
        Initialize a Vendor.

        :param inventory: optional list of items; defaults to an empty list.
        """
        self.inventory = [] if inventory is None else list(inventory)

    def add(self, item):
        """
        Add an item to the inventory and return the same item.
        """
        self.inventory.append(item)
        return item

    def remove(self, item):
        """
        Remove an item from the inventory.

        :return: the removed item, or False if the item is not present.
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False