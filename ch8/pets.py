"""
    Different kind of arguments
"""

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Positional arguments
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog')

# Default values
def describe_pet_d(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet_d('willie')
describe_pet_d(pet_name='willie')

describe_pet_d('harry', 'hamster')
describe_pet_d(pet_name='harry', animal_type='hamster')
