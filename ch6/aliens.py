"""
    Nesting
"""

ALIEN_0 = {'color': 'green', 'points': 5}
ALIEN_1 = {'color': 'yellow', 'points': 10}
ALIEN_2 = {'color': 'red', 'points': 15}

ALIENS = [ALIEN_0, ALIEN_1, ALIEN_2]

for alien in ALIENS:
    print(alien)

print()
ALIENS = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    ALIENS.append(new_alien)

for alien in ALIENS[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(ALIENS)))


print()
ALIENS = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    ALIENS.append(new_alien)

for alien in ALIENS[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in ALIENS[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(ALIENS)))
