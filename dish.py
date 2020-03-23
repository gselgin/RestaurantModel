# Greg Elgin
# Last Updated: 3/23/20
# Dish to be used in the restaurant model


class Dish:
    # Construct a dish
    def __init__(self, name, course, price):
        self.name = name
        self.course = course
        self.price = price

    # Getters return the name of dish, course, and price of the dish respectively
    def get_name(self):
        return self.name

    def get_course(self):
        return self.course

    def get_price(self):
        return self.price
