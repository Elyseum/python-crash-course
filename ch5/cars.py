"""
    IF statement: conditional operations
"""

CARS = ['audi', 'bmw', 'subaru', 'toyota']

for car in CARS:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
