# Greg Elgin
# Last Updated: 3/27/20
# Model restaurant for CS: 205 Individual Assignment, OOP and TDD
# ALL MODIFICATIONS OF A BILL GO THROUGH RESTAURANT

import bill


class Restaurant:
    # Construct a restaurant
    def __init__(self):
        self.dishes = list()
        self.patrons = set()
        self.bills = list()

    # Add dish and add patron add to the restaurant
    # Both have no limits
    def add_dish(self, dish):
        self.dishes.append(dish)

    def add_patron(self, patron):
        self.patrons.add(patron)

    # Getters return the dishes and the patrons of the restaurant respectively
    def get_dishes(self):
        return self.dishes

    def get_patrons(self):
        return self.patrons

    # Getters return all bills or just unpaid bills or just paid bills respectively
    def get_bills(self):
        return self.bills

    def get_unpaid_bills(self):
        unpaid = list()
        for b in self.bills:
            if not b.get_is_paid():
                if not b.get_total() == 0:
                    unpaid.append(b)
        return unpaid

    def get_paid_bills(self):
        paid = list()
        for b in self.bills:
            if b.get_is_paid():
                paid.append(b)
        return paid

    # Creates a bill for the customer specified
    def new_bill(self, p):
        self.bills.append(bill.Bill(p))
        p.set_bill(self.bills[-1])

    # Adds a dish to the bill and recalculates the bill total
    @staticmethod
    def add_to_bill(b, d):
        print(b.get_patron().get_name() + " has ordered a " + d.get_name())
        b.get_dishes().append(d)
        b.set_total()

    # Sets the bill to paid, adds a payment type
    @staticmethod
    def pay_bill(b, payment_method):
        b.is_paid = True
        b.payment_type = payment_method
        b.get_patron().bill = None

