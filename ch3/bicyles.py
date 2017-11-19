"""
    Chapter 3: illustrations on how to use lists
"""

BICYLES = ['trek', 'cannondale', 'redline', 'specialized']
print("All:")
print(BICYLES)

print("\nFirst:")
print(BICYLES[0])
print(BICYLES[0].title())

print("\nLast:")
print(BICYLES[-1].title())

MESSAGE = "My first bicycle was a " + BICYLES[0].title() + "."
print(MESSAGE)
