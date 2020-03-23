# Greg Elgin
# Last Updated: 3/23/20
# Simulates a day in the restaurant

import patron
import dish


class Simulate:
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def run(self):
        # Create patrons
        magda = patron.Patron("Magda", True)
        miranda = patron.Patron("Miranda", False)
        derek = patron.Patron("Derek", False)

        # Add patrons to the restaurant
        self.restaurant.add_patron(magda)
        self.restaurant.add_patron(miranda)
        self.restaurant.add_patron(derek)

        # Create dishes
        cocktail = dish.Dish("cocktail", "Drink", 7.00)
        salad = dish.Dish("Salad", "Appetizer", 8.00)
        soup = dish.Dish("Soup", "Appetizer", 6.00)
        chicken_sandwich = dish.Dish("Chicken Sandwich", "Entree", 10.00)
        lasagna = dish.Dish("Lasagna", "Entree", 12.00)
        chocolate_cake = dish.Dish("Chocolate Cake", "Desert", 13.00)

        # Add dishes to the restaurant
        self.restaurant.add_dish(cocktail)
        self.restaurant.add_dish(salad)
        self.restaurant.add_dish(soup)
        self.restaurant.add_dish(chicken_sandwich)
        self.restaurant.add_dish(lasagna)
        self.restaurant.add_dish(chocolate_cake)

        # Print the dishes served at the restaurant
        print("Dishes:")
        for d in self.restaurant.get_dishes():
            dish_info = d.get_course() + " --- " + d.get_name() + " --- " + str(d.get_price())
            print(dish_info)

        # Print the patrons at the restaurant
        print()
        print("Patrons:")
        for p in self.restaurant.get_patrons():
            patron_info = p.get_name()
            if p.get_preferred():
                patron_info += " -- Preferred Customer -- "
            if p.get_bill():
                patron_info += p.get_bill.get_total()
            print(patron_info)

        # Create a bill for magda

        # Add dishes to the bill
