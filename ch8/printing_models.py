""" Passing lists to functions """

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each desing, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulation
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """ Print completed models """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

UNPRINTED_DESIGNS = ['iphone_case', 'robot pedant', 'dodecahedron']
COMPLETED_MODELS = []

print_models(UNPRINTED_DESIGNS, COMPLETED_MODELS)
show_completed_models(COMPLETED_MODELS)
print(UNPRINTED_DESIGNS)

UNPRINTED_DESIGNS = ['iphone_case', 'robot pedant', 'dodecahedron']
COMPLETED_MODELS = []

# Pass in a copy of unprinted designs so print_models doesn't alter original.
print()
print_models(UNPRINTED_DESIGNS[:], COMPLETED_MODELS)
show_completed_models(COMPLETED_MODELS)
print(UNPRINTED_DESIGNS)
