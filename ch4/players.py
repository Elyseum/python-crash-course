"""
    Parts of a list
"""

# C# LINQ skip and take
PLAYERS = ['charles', 'martina', 'michael', 'florence', 'eli']
print(PLAYERS[0:3])
print(PLAYERS[1:4])
print(PLAYERS[:4])
print(PLAYERS[2:])
print(PLAYERS[-3:])

print("Here are the first three players of my team:")
for player in PLAYERS[:3]:
    print(player.title())
