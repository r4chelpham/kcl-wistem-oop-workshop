import unittest
from main import VendingMachine, Item 

class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        """Create a fresh vending machine before each test."""
        self.vm = VendingMachine()
        self.chips = Item("Chips", 1.50, 5)
        self.soda = Item("Soda", 1.25, 8)
        self.vm.add_item(self.chips, "A1")
        self.vm.add_item(self.soda, "A2")

    def test_add_item(self):
        """Test adding an item to the vending machine."""
        self.assertIn("A1", self.vm.items)
        self.assertEqual(self.vm.items["A1"], self.chips)
    
    def test_insert_money(self):
        """Test inserting money into the vending machine."""
        self.vm.insert_money(5.00)
        self.assertEqual(self.vm.balance, 5.00)
        
        with self.assertRaises(ValueError):
            self.vm.insert_money(-1)
    
    def test_dispense_item(self):
        """Test dispensing an item with sufficient balance."""
        self.vm.insert_money(2.00)
        self.vm.dispense_item("A1")
        self.assertEqual(self.vm.items["A1"].quantity, 4)
        self.assertEqual(self.vm.balance, 0.50)
    
    def test_dispense_item_insufficient_balance(self):
        """Test that an item is not dispensed if balance is too low."""
        with self.assertRaises(ValueError):
            self.vm.dispense_item("A1")
    
    def test_dispense_out_of_stock(self):
        """Test attempting to dispense an item that is out of stock."""
        self.vm.items["A1"].quantity = 0
        with self.assertRaises(ValueError):
            self.vm.dispense_item("A1")
    
    def test_refund(self):
        """Test refunding the remaining balance."""
        self.vm.insert_money(3.00)
        self.vm.refund()
        self.assertEqual(self.vm.balance, 0.00)
    
    def test_dispense_invalid_slot(self):
        """Test trying to dispense from a non-existent slot."""
        with self.assertRaises(ValueError):
            self.vm.dispense_item("B1")


if __name__ == "__main__":
    unittest.main()
