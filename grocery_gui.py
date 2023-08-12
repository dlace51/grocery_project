from tkinter import *
from grocery_logic import ShoppingCart


class ShoppingCartApp:
    """
      A class to represent the shopping cart GUI application.
      """
    def __init__(self, window):
        """
                Initialize the GUI with necessary components and layout.
                :param window: tkinter root window
                """
        self.shopping_cart = ShoppingCart()
        self.window = window
        window.title("Grocery Store")
        window.geometry("500x400")

        self.left_frame = Frame(window)
        self.left_frame.pack(side=LEFT, padx=10, pady=10)

        self.right_frame = Frame(window)
        self.right_frame.pack(side=RIGHT, padx=10, pady=0)

        Label(self.left_frame, text="Items", font=("Arial", 24)).pack(pady=10)

        self.item_var = StringVar()
        self.item_var.trace("w", self.adjust_price)  # Trace changes to the item entry
        self.qty_var = IntVar(value=0)
        self.price_var = StringVar(value="$0.00")

        Label(self.left_frame, text="Item").pack()
        Entry(self.left_frame, textvariable=self.item_var).pack(pady=5)

        Label(self.left_frame, text="Price").pack()
        Label(self.left_frame, textvariable=self.price_var).pack(pady=5)

        Label(self.left_frame, text="Qty").pack()
        frame_qty = Frame(self.left_frame)
        frame_qty.pack(pady=5)

        Button(frame_qty, text="-", command=self.decrease_qty).pack(side=LEFT)
        Label(frame_qty, textvariable=self.qty_var).pack(side=LEFT, padx=10)
        Button(frame_qty, text="+", command=self.increase_qty).pack(side=LEFT)

        Button(self.left_frame, text="Add to Cart", command=self.add_to_cart).pack(pady=15)
        Button(self.left_frame, text="View Cart", command=self.view_cart).pack(pady=15)

        self.error_label = Label(self.left_frame, text="", fg="red")
        self.error_label.pack(pady=5)

        Label(self.right_frame, text="Items for Sale:", font=("Arial", 14)).pack(pady=10)
        items_prices = {
            'Cookies': 1.50,
            'Sandwiches': 4.00,
            'Water': 1.00,
            'Milk': 2.50,
            'Bread': 1.25,
            'Eggs': 2.00
        }
        for item, price in items_prices.items():
            Label(self.right_frame, text=f"{item} - ${price:.2f}", font=("Arial", 10)).pack(pady=2)

    def adjust_price(self, *args):
        """
             Adjusts the displayed price based on selected item and quantity.
             """
        item = self.item_var.get().strip().lower()
        prices = {
            'cookies': 1.50,
            'sandwiches': 4.00,
            'water': 1.00,
            'milk': 2.50,
            'bread': 1.25,
            'eggs': 2.00
        }
        if item in prices:
            self.price_var.set(f"${prices.get(item, 0) * self.qty_var.get():.2f}")
            self.error_label.config(text="")
        else:
            self.price_var.set("$0.00")
            self.error_label.config(text="Not a valid item!")

    def increase_qty(self):
        """
        Increases the quantity of the selected item.
                """
        item = self.item_var.get().strip().lower()
        if item in self.shopping_cart.cart:
            self.qty_var.set(self.qty_var.get() + 1)
            self.adjust_price()

    def decrease_qty(self):
        """
             Decreases the quantity of the selected item.
                """
        self.qty_var.set(max(0, self.qty_var.get() - 1))
        self.adjust_price()

    def add_to_cart(self):
        """
                Adds the selected item and quantity to the shopping cart.
                """
        item = self.item_var.get().strip().lower()
        if item in self.shopping_cart.cart:
            self.shopping_cart.add_item(item, self.qty_var.get())
            self.item_var.set("")
            self.qty_var.set(0)
            self.price_var.set("$0.00")
        else:
            self.error_label.config(text="Not a valid item!")

    def view_cart(self):
        cart_window = Toplevel(self.window)
        cart_window.title("Your Cart")
        cart_window.geometry("300x300")

        for item, quantity in self.shopping_cart.cart.items():
            if quantity:
                price_map = {
                    'cookies': 1.50,
                    'sandwiches': 4.00,
                    'water': 1.00,
                    'milk': 2.50,
                    'bread': 1.25,
                    'eggs': 2.00
                }
                Label(cart_window, text=f"{item.capitalize()} x {quantity} = ${quantity * price_map[item]:.2f}").pack(pady=5)

        Label(cart_window, text=f"Total: ${self.shopping_cart.get_total():.2f}").pack(pady=10)
