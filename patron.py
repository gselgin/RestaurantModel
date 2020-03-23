# Greg Elgin
# Last Updated: 3/23/20
# Patron to be used in the restaurant model

import bill


class Patron:
    def __init__(self, name, preferred):
        self.name = name
        self.preferred = preferred
        self.bill = None

    # Getters return the name, preferred status, and bill of a patron respectively
    def get_name(self):
        return self.name

    def get_preferred(self):
        return self.preferred

    def get_bill(self):
        return self.bill

    # Assigns a bill to a patron
    def set_bill(self, b):
        self.bill = b
