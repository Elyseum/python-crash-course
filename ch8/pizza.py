""" Arbitrary numer of arguments """

# *toppings is tuple of arbitrary length
def make_pizza(*toppings):
    """ Print list of requested toppings """
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza_2(*toppings):
    """ Summarize pizza we're about to make """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza_2('pepperoni')
make_pizza_2('mushrooms', 'green peppers', 'extra cheese')

def make_pizza_3(size, *toppings):
    """ Summarize pizza we're about to make """
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza_3(16, 'pepperoni')
make_pizza_3(12, 'mushrooms', 'green peppers', 'extra cheese')
