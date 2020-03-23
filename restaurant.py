# Greg Elgin
# Last Updated: 3/23/20
# Model restaurant for CS: 205 Individual Assignment, OOP and TDD


class Restaurant:
    # Construct a restaurant
    def __init__(self):
        self.dishes = set()
        self.patrons = set()
        self.bills = list()

    # Add dish and add patron add to the restaurant
    # Both have no limits
    def add_dish(self, dish):
        self.dishes.add(dish)

    def add_patron(self, patron):
        self.patrons.add(patron)

    # Getters return the dishes and patrons of the restaurant
    def get_dishes(self):
        return self.dishes

    def get_patrons(self):
        return self.patrons

    def process_bill(self):

    def is_bill_paid(self, bill):
        if
    def