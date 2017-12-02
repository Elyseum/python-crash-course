"""
    Dictionaries
"""

ALIEN_0 = {'color': 'green', 'points': 5}
print(ALIEN_0['color'])

POINTS = ALIEN_0['points']
print("You just earned " + str(POINTS) + " points!")

ALIEN_0['x_position'] = 0
ALIEN_0['y_position'] = 25
print(ALIEN_0)

ALIEN_0 = {}
ALIEN_0['color'] = 'green'
ALIEN_0['points'] = 5
print(ALIEN_0)

ALIEN_0 = {'color': 'green'}
print("The alien is " + ALIEN_0['color'] + ".")
ALIEN_0['color'] = 'yellow'
print("The alien is now " + ALIEN_0['color'] + ".")

ALIEN_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(ALIEN_0['x_position']))

# Move to the right based on speed
if ALIEN_0['speed'] == 'slow':
    X_INCREMENT = 1
elif ALIEN_0['speed'] == 'medium':
    X_INCREMENT = 2
else:
    X_INCREMENT = 3

ALIEN_0['x_position'] = ALIEN_0['x_position'] + X_INCREMENT
print("New x-position: " + str(ALIEN_0['x_position']))

ALIEN_0 = {'color': 'green', 'points': 5}
print(ALIEN_0)
del ALIEN_0['points']
print(ALIEN_0)
# Trying to delete again throws a KeyError
# del ALIEN_0['points']

FAVORITE_LANGUAGES = {
    'jen'   : 'python',
    'sarah' : 'c',
    'edward': 'ruby',
    'phil'  : 'python'
}
print("Sarah's favorite language is " +
      FAVORITE_LANGUAGES['sarah'].title() +
      ".")
