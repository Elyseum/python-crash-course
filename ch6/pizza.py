"""
    Nesting a list in a dictionary
"""

PIZZA = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + PIZZA['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in PIZZA['toppings']:
    print("\t" + topping)
