"""
    Chapter 4: for loops
"""

MAGICIANS = ['alice', 'david', 'carolina']
for magician in MAGICIANS:
    print(magician)

print("")
MAGICIANS = ['alice', 'david', 'carolina']
for magician in MAGICIANS:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")

print("")
MAGICIANS = ['alice', 'david', 'carolina']
for magician in MAGICIANS:
    print(magician.title() + ", that was a great trick!")
# Outside the loop you can still access the loop variable 
# to get a hold of the last value.
print("I can't wait to see your next trick, " + magician.title() + ".\n")
