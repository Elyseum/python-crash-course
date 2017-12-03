""" Inheriting a class from a different file """

from car import Car

class ElectricCar(Car):
    """ Electric car """

    def __init__(self, make, model, year):
        """ Init parent """
        Car.__init__(self, make, model, year)

MY_TESLA = ElectricCar('tesla', 'model s', 2016)
print(MY_TESLA.get_descriptive_name())
