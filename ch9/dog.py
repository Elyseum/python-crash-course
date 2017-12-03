""" Defining with classes """

class Dog():
    """ Modelling a dog """

    def __init__(self, name, age):
        """ Init name and age """
        self.name = name
        self.age = age

    def sit(self):
        """ Respond to sit command """
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """ Respond to roll over command """
        print(self.name.title() + " rolled over!")

MY_DOG = Dog('willie', 6)
print("My dog's name is " + MY_DOG.name.title() + ".")
print("My dog is " + str(MY_DOG.age) + " years old.")

MY_DOG.sit()
MY_DOG.roll_over()

YOUR_DOG = Dog('lucy', 3)
print("Your dog's name is " + YOUR_DOG.name.title() + ".")
print("Your dog is " + str(YOUR_DOG.age) + " years old.")
