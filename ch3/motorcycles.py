"""
    Modifying a list
"""

MOTORCYCLES = ['honda', 'yamaha', 'suzuki']
print(MOTORCYCLES)

MOTORCYCLES[0] = 'ducati'
print(MOTORCYCLES)

MOTORCYCLES = ['honda', 'yamaha', 'suzuki']
print(MOTORCYCLES)
MOTORCYCLES.append('ducati')
print(MOTORCYCLES)

MOTORCYCLES = []
MOTORCYCLES.append('honday')
MOTORCYCLES.append('yamaha')
MOTORCYCLES.append('suzuki')
print(MOTORCYCLES)

MOTORCYCLES = ['honda', 'yamaha', 'suzuki']
MOTORCYCLES.insert(0, 'ducati')
print(MOTORCYCLES)

print("Delete:")
MOTORCYCLES = ['honda', 'yamaha', 'suzuki']
print(MOTORCYCLES)
del MOTORCYCLES[0]
print(MOTORCYCLES)

print("Delete 2:")
HONDA = 'honda'
MOTORCYCLES = [HONDA, 'yamaha', 'suzuki']
print(HONDA)
print(MOTORCYCLES)
del MOTORCYCLES[0]
print(HONDA) # still exists

print("Pop:")
MOTORCYCLES = ['honda', 'yamaha', 'suzuki']
POPPED_MOTORCYCLE = MOTORCYCLES.pop()
print(MOTORCYCLES)
print(POPPED_MOTORCYCLE)

MOTORCYCLES = ['honda', 'yamaha', 'suzuki']
LAST_OWNED = MOTORCYCLES.pop()
print("The last motorcycle I owned was a " + LAST_OWNED.title() + ".")

MOTORCYCLES = ['honda', 'yamaha', 'suzuki']
FIRST_OWNED = MOTORCYCLES.pop(0)
print("The first motorcycle I owned was a " + FIRST_OWNED.title() + ".")

print("Remove by value:")
MOTORCYCLES = ['honda', 'yamaha', 'suzuki', 'ducati']
print(MOTORCYCLES)
# removes first occurence, value error if not present
MOTORCYCLES.remove('ducati')
print(MOTORCYCLES)
