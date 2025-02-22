"""

This is the boilerplate for the OOP workshop activity.
If you are stuck, use the Python documentation + cheatsheet + Google -
you can also ask us for help

Do not look at the solution until you have exhausted all options! 
Looking at the solution straight away won't help you to learn...
and you'll also have a greater sense of satisfaction from solving it yourself :)

"""


class Item:
    """
    Represents an item in the vending machine.
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        if quantity < 0:
            raise ValueError("Cannot have negative item quantity")
        self.quantity = quantity

    def reduce_quantity(self):
        if self.quantity > 0:
            self.quantity -= 1
        else:
            raise ValueError(f"{self.name} is out of stock!")

    # DO NOT CHANGE BELOW ****
    def __eq__(self, other):
        if isinstance(other, Item):
            return self.name.lower() == other.name.lower()
        return False
    # DO NOT CHANGE ABOVE ****
    

class VendingMachine:
    """
    Represents a vending machine.
    """
    def __init__(self):
      # CHALLENGE: in real vending machines, the slots only have a limited capacity for an item.
      # implement a mechanism to keep track of the maximum capacity of any slot
      # HINT: think about what methods you need to enforce the maximum capacity in.
        self.items = {}
        self.balance = 0.0

    def add_item(self, item, slot):
        """Adds an item to a specific slot in the vending machine."""
        if slot in self.items:
            raise ValueError(f"Slot {slot} is already occupied!")
        # TODO: how do you add the item to the items?
        # CODE STARTS HERE
        pass
        # CODE STOPS HERE
        # HINT: use the Python documentation to find out how a dictionary/map works...

    # DO NOT CHANGE THIS FUNCTION
    def display_items(self):
        print("Items in the vending machine:")
        for slot, item in self.items.items():
            print(f"Slot {slot}: {item.name} - £{item.price:.2f} ({item.quantity} left)")

    def insert_money(self, amount):
        if amount <= 0:
            raise ValueError("Inserted amount must be positive.")
        # TODO: how do you update the vending machine balance?
        # CODE STARTS HERE
        pass
        # CODE STOPS HERE
      
        print(f"Current balance: £{self.balance:.2f}")

    def dispense_item(self, slot):
        """Dispenses an item if enough balance exists and the item is in stock."""
        if slot not in self.items:
            raise ValueError("Invalid slot!")

        item = self.items[slot]

        if item.quantity <= 0:
            raise ValueError(f"{item.name} is out of stock!")

        if self.balance < item.price:
            raise ValueError(f"Insufficient balance. {item.name} costs £{item.price:.2f}.")

        # Dispenses the actual item
        # TODO: what happens when you take the item out of a vending machine?
        # what effects does this have on the state of the vending machine and how can we model this in our system?
        # CODE STARTS HERE
        pass
        # CODE STOPS HERE
        print(f"Dispensing {item.name}. Enjoy!")
        print(f"Remaining balance: £{self.balance:.2f}")

    def refund(self):
        """Refunds the remaining balance."""
        print(f"Refunding £{self.balance:.2f}")
        self.balance = 0.0

    def restock_item(self, item, slot):
      # CHALLENGE : given an item and a slot in our vending machine, restock this item into the vending machine
      # think about what types of cases you need to account for in this method:
      # for example, what if we had a non empty slot, and we try to restock that slot with
      # a different item to the one being stored currently?
        pass     

    def dispense_items(self, slots):
      # CHALLENGE : given a list of slots, dispense these items from the vending machine.
      # HINT 1: we already have a `dispense_item` method, so there is no need to repeat this 
      # logic (think about *abstraction*)
      pass
      
# Demonstration of the vending machine
if __name__ == "__main__":
    # you can create a vending machine instance and play around with it here!
    # this is a sample interaction but feel free to change it about as you wish :) 
    vm = VendingMachine()

    vm.add_item(Item("Chips", 1.50, 10), "A1")
    vm.add_item(Item("Soda", 1.25, 8), "A2")
    vm.add_item(Item("Candy", 0.75, 15), "A3")

    vm.display_items()

    # this is a try-catch block - it tries out something, if it runs into an error rather than crashing, 
    # it will produce a more understandable error message/output
    try:
        vm.insert_money(2.00)
        vm.dispense_item("A2")   # Buy Soda
        vm.dispense_item("A3")   # Buy Candy
        vm.refund()           # Refund remaining balance
    except ValueError as e:
        print(f"Error: {e}")
