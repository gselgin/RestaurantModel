# Greg Elgin
# Last Updated: 3/23/20
# Model restaurant for CS: 205 Individual Assignment, OOP and TDD

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

    # Creates a bill for the customer specified
    def new_bill(self, p):
        self.bills.append(bill.Bill(p))

    # Adds a dish to the bill
