# Greg Elgin
# Last Updated: 3/27/20
# Simulates a day in the restaurant

import patron
import dish


# noinspection DuplicatedCode
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
        print()

        # Create a bill for magda and a bill for miranda
        self.restaurant.new_bill(magda)
        self.restaurant.new_bill(miranda)

        # Add dishes to the bills
        self.restaurant.add_to_bill(magda.get_bill(), cocktail)
        self.restaurant.add_to_bill(miranda.get_bill(), salad)
        self.restaurant.add_to_bill(miranda.get_bill(), lasagna)
        self.restaurant.add_to_bill(magda.get_bill(), cocktail)

        # Display all bills
        print()
        print("Bills:")
        for b in self.restaurant.get_bills():
            b_info = "Patron: " + b.get_patron().get_name() + ", Dishes: "
            for d in b.get_dishes():
                b_info += d.get_name() + ", "
            b_info += "Total: $" + str(("%.2f" % b.get_total()))
            print(b_info)
        print()

        # Create a bill for derek
        self.restaurant.new_bill(derek)

        # Add more dishes to the bills
        self.restaurant.add_to_bill(magda.get_bill(), cocktail)
        self.restaurant.add_to_bill(magda.get_bill(), chicken_sandwich)
        self.restaurant.add_to_bill(magda.get_bill(), chocolate_cake)
        self.restaurant.add_to_bill(magda.get_bill(), cocktail)
        self.restaurant.add_to_bill(miranda.get_bill(), chocolate_cake)
        self.restaurant.add_to_bill(derek.get_bill(), soup)
        self.restaurant.add_to_bill(derek.get_bill(), chicken_sandwich)

        # Display all bills
        print()
        print("Bills:")
        for b in self.restaurant.get_bills():
            b_info = "Patron: " + b.get_patron().get_name() + ", Dishes: "
            for d in b.get_dishes():
                b_info += d.get_name() + ", "
            b_info += "Total: $" + str(("%.2f" % b.get_total()))
            print(b_info)
        print()

        # Pay magda's bill
        self.restaurant.pay_bill(magda.get_bill(), "Visa")
        print("Magda has just paid her bill")

        # Display all unpaid bills
        print()
        print("Unpaid Bills:")
        for b in self.restaurant.get_unpaid_bills():
            b_info = "Patron: " + b.get_patron().get_name() + ", Dishes: "
            for d in b.get_dishes():
                b_info += d.get_name() + ", "
            b_info += "Total: $" + str(("%.2f" % b.get_total()))
            print(b_info)

        # Display all paid bills
        print()
        print("Paid Bills: ")
        for b in self.restaurant.get_paid_bills():
            b_info = "Patron: " + b.get_patron().get_name() + ", Total: $" + str(("%.2f" % b.get_total())) + \
                     ", Payment Type: " + b.get_payment_type()
            print(b_info)
        print()

        # Display if Magda has any bills
        print("Bill now on Magda's account: ")
        print(magda.get_bill())
