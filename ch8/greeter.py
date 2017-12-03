"""
    Writing and calling methods
"""

def greet_user():
    """ Prints hello to the user """
    print("Hello!")

greet_user()


def greet_user_byname(user_name):
    """ Display a simple greeting for given user name """
    print("Hello, " + user_name.title() + "!")

greet_user_byname('jesse')
greet_user_byname('sarah')
