# Greg Elgin
# Last Updated: 3/27/20
# Bill to be used in the restaurant model
# ALL MODIFICATIONS OF A BILL GO THROUGH RESTAURANT


# Calculates the total price of the bill
def calculate_total(dishes):
    total = 0
    for d in dishes:
        total += d.get_price()
    return total


class Bill:
    # Construct a bill
    # When bill is constructed it is unpaid and has no payment type
    def __init__(self, p):
        self.patron = p
        self.dishes = list()
        self.is_paid = False
        self.payment_type = None
        self.total = calculate_total(self.dishes)

    # Getters return patron and dishes on the bill
    def get_patron(self):
        return self.patron

    def get_dishes(self):
        return self.dishes

    # Getters return if the bill is paid, payment type, and the total of the bill respectively
    def get_is_paid(self):
        return self.is_paid

    def get_payment_type(self):
        return self.payment_type

    def get_total(self):
        return self.total

    # Called from restaurant when a new dish is added to the bill
    # Calls to recalculate total and saves to total
    def set_total(self):
        self.total = calculate_total(self.dishes)
