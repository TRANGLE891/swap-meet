#wave 1
class Vendor:
    """
    Represents a swap-meet participant with an inventory of items.
    """

    def __init__(self, inventory=None):
        """
        Initialize a Vendor.

        param inventory: optional list of items; defaults to an empty list.
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

        return: the removed item, or False if the item is not present.
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
#wave 2  
    def get_by_id(self, id):
        """
        Find an item in inventory by its id.

        param id: integer representing the item's id.
        return: the matching item, or None if not found.
        """
        for item in self.inventory:
            if getattr(item, "id", None) == id:
                return item
        return None
    
#wave 3
    def swap_items(self, other_vendor, my_item, their_item):
        """
        Swap items between vendors.

        param other_vendor: the vendor to trade with.
        param my_item: the item to give to the other vendor.
        param their_item: the item to receive from the other vendor.
        return: True on success, False if either item is missing.
        """
        if my_item not in self.inventory:
            return False
        if their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    
#wave 4
    def swap_first_item(self, other_vendor):
        """
        Swap the first item of each vendor's inventory.

        param other_vendor: another Vendor to trade with.
        return: True on success, False if either inventory is empty.
        """
        if not self.inventory or not other_vendor.inventory:
            return False

        my_first = self.inventory[0]
        their_first = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_first, their_first)