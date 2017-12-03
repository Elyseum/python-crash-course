""" Modifying class state """

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

MY_NEW_CAR = Car('audi', 'a4', 2016)
print(MY_NEW_CAR.get_descriptive_name())
MY_NEW_CAR.read_odometer()

MY_NEW_CAR.odometer_reading = 23
MY_NEW_CAR.read_odometer()

MY_NEW_CAR.update_odometer(46)
MY_NEW_CAR.read_odometer()

MY_NEW_CAR.update_odometer(23)

MY_USED_CAR = Car('subaru', 'outback', 2013)
print(MY_USED_CAR.get_descriptive_name())

MY_USED_CAR.update_odometer(23500)
MY_USED_CAR.read_odometer()

MY_USED_CAR.increment_odometer(100)
MY_USED_CAR.read_odometer()
