# Greg Elgin
# Last Updated: 3/23/20
# Creates a restaurant object and simulates a day in the restaurant
# Unit testing used to verify all methods work as they should

import restaurant
import simulate


def main():
    my_restaurant = restaurant.Restaurant()

    my_simulation = simulate.Simulate(my_restaurant)
    my_simulation.run()


main()
