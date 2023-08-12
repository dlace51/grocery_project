

class ShoppingCart:
    """
      A class to represent a shopping cart with different items and quantities.
    """
    def __init__(self):
        self.cart = {'cookies': 0, 'sandwiches': 0, 'water': 0, 'milk': 0, 'bread': 0, 'eggs': 0}

    def add_item(self, item, quantity):
        """
        Adds a specified quantity of an item to the cart.
        :param item: Name of the item to add
        :param quantity: Quantity of the item to add
                """
        self.cart[item] += quantity

    def get_total(self):
        prices = {
            'cookies': 1.50,
            'sandwiches': 4.00,
            'water': 1.00,
            'milk': 2.50,
            'bread': 1.25,
            'eggs': 2.00
        }
        return sum([self.cart[item] * prices[item] for item in self.cart])

    def __str__(self):
        return ', '.join([f"{value} x {key}" for key, value in self.cart.items() if value > 0])
