"""
    Dinner guests exercise
"""

GUESTS = ['bill', 'linus', 'steve']

print("Invitations take 1:")
print("Hi " + GUESTS[0].title() + ", would you like to come to my dinner?")
print("Hi " + GUESTS[1].title() + ", would you like to come to my dinner?")
print("Hi " + GUESTS[2].title() + ", would you like to come to my dinner?")

print("Oops, turns out " + GUESTS[2].title() + " can't make it")

GUESTS[2] = 'Satya'
print("\nInvitations take 2:")
print("Hi " + GUESTS[0].title() + ", would you like to come to my dinner?")
print("Hi " + GUESTS[1].title() + ", would you like to come to my dinner?")
print("Hi " + GUESTS[2].title() + ", would you like to come to my dinner?")

GUESTS.insert(0, "new guest 1")
GUESTS.insert(2, "new guest 2")
GUESTS.append("new guest 3")
print("\nInvitations take 3:")
print("Hi " + GUESTS[0].title() + ", would you like to come to my dinner?")
print("Hi " + GUESTS[1].title() + ", would you like to come to my dinner?")
print("Hi " + GUESTS[2].title() + ", would you like to come to my dinner?")
print("Hi " + GUESTS[3].title() + ", would you like to come to my dinner?")
print("Hi " + GUESTS[4].title() + ", would you like to come to my dinner?")
print("Hi " + GUESTS[5].title() + ", would you like to come to my dinner?")

print("\nCancellations:")
print("Sorry " + GUESTS.pop().title() + ", I have to cancel your invitation")
print("Sorry " + GUESTS.pop().title() + ", I have to cancel your invitation")
print("Sorry " + GUESTS.pop().title() + ", I have to cancel your invitation")
print("Sorry " + GUESTS.pop().title() + ", I have to cancel your invitation")
print("Don't worry " + GUESTS[0].title() + ", you're still invited")
print("Don't worry " + GUESTS[1].title() + ", you're still invited")

del GUESTS[0]
del GUESTS[0] # Don't use 1 ^^
print("\nEmpty list:")
print(GUESTS)
