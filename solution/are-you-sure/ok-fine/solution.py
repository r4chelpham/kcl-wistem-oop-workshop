class Item:
    """
    Represents an item in the vending machine.
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def reduce_quantity(self):
        if self.quantity > 0:
            self.quantity -= 1
        else:
            raise ValueError(f"{self.name} is out of stock!")

class VendingMachine:
    """
    Represents a vending machine.
    """
    def __init__(self):
        self.items = {}
        self.balance = 0.0

    def add_item(self, item, slot):
        """Adds an item to a specific slot in the vending machine."""
        if slot in self.items:
            raise ValueError(f"Slot {slot} is already occupied!")
        self.items[slot] = item

    def display_items(self):
        print("Items in the vending machine:")
        for slot, item in self.items.items():
            print(f"Slot {slot}: {item.name} - £{item.price:.2f} ({item.quantity} left)")

    def insert_money(self, amount):
        if amount <= 0:
            raise ValueError("Inserted amount must be positive.")
        self.balance += amount
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
        item.reduce_quantity()
        self.balance -= item.price
        print(f"Dispensing {item.name}. Enjoy!")
        print(f"Remaining balance: £{self.balance:.2f}")

    def refund(self):
        """Refunds the remaining balance."""
        print(f"Refunding £{self.balance:.2f}")
        self.balance = 0.0

# Demonstration of the vending machine
if __name__ == "__main__":
    # Create a vending machine instance
    vm = VendingMachine()

    # Add items to the vending machine
    vm.add_item(Item("Chips", 1.50, 10), "A1")
    vm.add_item(Item("Soda", 1.25, 8), "A2")
    vm.add_item(Item("Candy", 0.75, 15), "A3")

    # Display items
    vm.display_items()

    # Simulate a user interaction
    try:
        vm.insert_money(2.00)
        vm.dispense_item("A2")   # Buy Soda
        vm.dispense_item("A3")   # Buy Candy
        vm.refund()           # Refund remaining balance
    except ValueError as e:
        print(f"Error: {e}")
