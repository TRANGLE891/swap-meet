# Wave 1:
# import item
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
        else:
            return False

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item


# item1 = item.Item("tomato")
# item2 = item.Item("orange")
# item3 = item.Item("apple")

# vegiestore = Vendor([item1, item2, item3])

# print(vegiestore.get_by_id(item2.id))
# # # vegiestore.add("cho"
# # result = vegiestore.remove("minh nguyen")
# # print(result)
