"""
    This is about organizing (= sorting) the list
"""

CARS = ['bmw', 'audi', 'toyota', 'subaru']
CARS.sort() # in-place sorting
print(CARS)

CARS = ['bmw', 'audi', 'toyota', 'subaru']
CARS.sort(reverse=True)
print(CARS)

CARS = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(CARS)
print("Here is sorted list:")
print(sorted(CARS)) # new list: sorted version of the original one
print("Here is the original list again:")
print(CARS)

# Sorting works good because ALL values are lower-case

print("Reversing")
CARS = ['bmw', 'audi', 'toyota', 'subaru']
print(CARS)
CARS.reverse() # in-place reversing the list
print(CARS)

CARS = ['bmw', 'audi', 'toyota', 'subaru']
print("Number of cars: " + str(len(CARS)))
