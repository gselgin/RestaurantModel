# Greg Elgin
# Last Updated: 3/23/20
# Bill to be used in the restaurant model

import patron
import dish


# # Calculates the total price of the bill
# def get_total(dishes):
#     total = 0
#     for d in dishes:
#         total += d.get_price()
#     return total


class Bill:
    # Construct a bill
    # When bill is constructed it is unpaid and has no payment type
    def _init_(self, p):
        self.patron = p
        self.dishes = list()
        self.is_paid = False
        self.payment_type = None
        #self.total = get_total(self.dishes)

    # Getters return patron and dishes on the bill
    def get_patron(self):
        return self.patron

    def get_dishes(self):
        return self.dishes

    # Setter sets the bill as paid and adds a payment type
    def set_paid(self, payment_type):
        self.is_paid = True
        self.payment_type = payment_type
