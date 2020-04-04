# Greg Elgin
# Last Updated: 4/02/20
# unit tests for Model Restaurant

import unittest
import restaurant
import dish
import patron


class TestBill(unittest.TestCase):
    restaurant = None

    @classmethod
    def setUpClass(cls):
        # Called once at the beginning
        print('Class set up')
        cls.restaurant = restaurant.Restaurant()

        # Create dishes
        cls.lasagna = dish.Dish("Lasagna", "Entree", 12.00)
        cls.chocolate_cake = dish.Dish("Chocolate Cake", "Desert", 13.00)

        # Add dishes to the restaurant
        cls.restaurant.add_dish(cls.lasagna)
        cls.restaurant.add_dish(cls.chocolate_cake)

        # Create patrons
        cls.miranda = patron.Patron("Miranda", False)
        cls.derek = patron.Patron("Derek", True)

        # Add patrons to the restaurant
        cls.restaurant.add_patron(cls.miranda)
        cls.restaurant.add_patron(cls.derek)

    @classmethod
    def tearDownClass(cls):
        # Called once at the end
        print('Class torn down')

    def setUp(self):
        # Called before every test
        print('Test case set up')

    def tearDown(self):
        # Called after every test
        print('Test case torn down')


    def test_bill(self):
        # Check that all customers have no bills
        bill = self.miranda.get_bill()
        self.assertEqual(bill, None)

        # Check that the restaurant has no bills
        bills = self.restaurant.get_bills()
        self.assertEqual(len(bills), 0)

        # Create a bill and add a dish
        self.restaurant.new_bill(self.miranda)
        self.restaurant.add_to_bill(self.miranda.get_bill(), self.lasagna)

        # Check that the customer has a bill and it is for the correct total and is unpaid
        bill = self.miranda.get_bill()
        self.assertEqual(bill.get_total(), 12.00)
        self.assertEqual(bill.get_is_paid(), False)

        # Check that there restaurant has the bill with the correct patron and total
        bills = self.restaurant.get_bills()
        self.assertEqual(len(bills), 1)
        self.assertEqual(bills[0].get_patron(), self.miranda)
        self.assertEqual(bills[0].get_total(), 12.00)

        # Check that the get_unpaid_bills returns the bill with the correct amount
        bills = self.restaurant.get_unpaid_bills()
        self.assertEqual(len(bills), 1)

        # Add a dish to the bill
        self.restaurant.add_to_bill(self.miranda.get_bill(), self.chocolate_cake)

        # Check that the bill amount is correct
        bill = self.miranda.get_bill()
        self.assertEqual(bill.get_total(), 25.00)

        # Pay the bill
        self.restaurant.pay_bill(self.miranda.get_bill(), "MasterCard")

        # Check that get_unpaid_bills returns none
        bills = self.restaurant.get_unpaid_bills()
        self.assertEqual(len(bills), 0)

        # Check that get_paid_bills returns the correct bill
        bills = self.restaurant.get_paid_bills()
        self.assertEqual(len(bills), 1)
        self.assertEqual(bills[0].get_total(), 25.00)
        self.assertEqual(bills[0].get_is_paid(), True)

        # Check that the payment type was added to the bill
        self.assertEqual(bills[0].get_payment_type(), "MasterCard")

        # Check that the customer no longer has a bill
        bill = self.miranda.get_bill()
        self.assertEqual(bill, None)


    def test_bill_two(self):
        # Test that the restaurant has 2 customers with no bills
        patrons = self.restaurant.get_patrons()
        self.assertEqual(len(patrons), 2)
        bill = self.miranda.get_bill()
        self.assertEqual(bill, None)
        bill = self.derek.get_bill()
        self.assertEqual(bill, None)

        # Check that derek is a preferred customer and miranda is not
        preferred = self.derek.get_preferred()
        self.assertEqual(preferred, True)
        preferred = self.miranda.get_preferred()
        self.assertEqual(preferred, False)

        # Create bills and add items to both bills
        self.restaurant.new_bill(self.miranda)
        self.restaurant.new_bill(self.derek)
        self.restaurant.add_to_bill(self.miranda.get_bill(), self.lasagna)
        self.restaurant.add_to_bill(self.miranda.get_bill(), self.chocolate_cake)
        self.restaurant.add_to_bill(self.miranda.get_bill(), self.chocolate_cake)
        self.restaurant.add_to_bill(self.derek.get_bill(), self.lasagna)
        self.restaurant.add_to_bill(self.derek.get_bill(), self.lasagna)
        self.restaurant.add_to_bill(self.derek.get_bill(), self.lasagna)

        # Check that the totals of both bills are correct
        bill = self.miranda.get_bill()
        self.assertEqual(bill.get_total(), 38.00)
        bill = self.derek.get_bill()
        self.assertEqual(bill.get_total(), 36.00)

        # Check that both bills are unpaid
        bill = self.miranda.get_bill()
        self.assertEqual(bill.get_is_paid(), False)
        bill = self.derek.get_bill()
        self.assertEqual(bill.get_is_paid(), False)

        # Pay derek's bill
        self.restaurant.pay_bill(self.derek.get_bill(), "Cash")

        # Check that the get_unpaid_bills only returns miranda's bill
        bills = self.restaurant.get_unpaid_bills()
        self.assertEqual(len(bills), 1)
        self.assertEqual(bills[0].get_patron(), self.miranda)

        # Check that the get_paid_bills returns only derek's bill and miranda's old bill
        bills = self.restaurant.get_paid_bills()
        self.assertEqual(len(bills), 2)
        self.assertEqual(bills[0].get_patron(), self.miranda)
        self.assertEqual(bills[1].get_patron(), self.derek)

        # Pay miranda's bill
        self.restaurant.pay_bill(self.miranda.get_bill(), "Debit")

        # Check that both bills payment types are correct and marked as paid
        bills = self.restaurant.get_bills()
        self.assertEqual(bills[1].get_payment_type(), "Debit")
        self.assertEqual(bills[2].get_payment_type(), "Cash")
        self.assertEqual(bills[1].get_is_paid(), True)
        self.assertEqual(bills[2].get_is_paid(), True)



if __name__ == "__main__":
    unittest.main()
