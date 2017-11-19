"""
    Complexer if statements
"""

AGE = 19
if AGE >= 18:
    print("You are old enough to vote!")

AGE = 19
if AGE >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

print("\nELSE statement:")
AGE = 17
if AGE >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
