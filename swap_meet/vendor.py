# wave 1

class Vendor:

    def __init__(self, inventory=None):
        self.inventory = inventory or []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

# wave 2
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item

# wave 3

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    # wave 4

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        my_first = self.inventory[0]
        their_first = other_vendor.inventory[0]
        return self.swap_items(other_vendor, my_first, their_first)
# Wave 6

    def get_by_category(self, category):
        result_Objects = []
        for object in self.inventory:
            if object.get_category() == category:
                result_Objects.append(object)

        return result_Objects

    def get_best_by_category(self, category):
        best_item = None
        for item in self.inventory:
            if item.get_category() == category:
                if best_item is None:
                    best_item = item

                if item.condition > best_item.condition:
                    best_item = item
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        return self.swap_items(other_vendor, my_best_item, their_best_item)
