""" Inheriting a class """

class Car():
    """ Simple car """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Formatting a descriptive name """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """ print mileage """
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """ Set odometer to given mileage, don't allow roll back! """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ Add given amount to odometer """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

class ElectricCar(Car):
    """ Electric car """

    def __init__(self, make, model, year):
        """ Init parent """
        # Next line gives a 'useless super call'
        # super().__init__(make, model, year)

        # Makes much more sense. Explicitly call Car.__init__ with self etc
        Car.__init__(self, make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """ Battery info """
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

MY_TESLA = ElectricCar('tesla', 'model s', 2016)
print(MY_TESLA.get_descriptive_name())
MY_TESLA.describe_battery()
