import csv


class Item:
    def __init__(self, id, name, price, quantity):
        self.id = int(id)
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)


class Stock:
    def __init__(self, filename):
        self.items = []
        with open(filename, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = Item(row["id"], row["name"], row["price"], row["quantity"])
                self.items.append(item)

    def get_item(self, id):
        for item in self.items:
            if item.id == int(id):
                return item
        return None

    def get_name(self, id):
        item = self.get_item(id)
        if item is None:
            return None
        return item.name

    def get_quantity(self, id):
        item = self.get_item(id)
        if item is None:
            return None
        return item.quantity

    def get_price(self, id, quantity):
        item = self.get_item(id)
        if item is None:
            return None
        return item.price * int(quantity)
