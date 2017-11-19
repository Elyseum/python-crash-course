"""
    The if-elif-else chain
"""

AGE = 12
if AGE < 4:
    print("Your admission cost is $0.")
elif AGE < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

AGE = 12
if AGE < 4:
    PRICE = 0
elif AGE < 18:
    PRICE = 5
else:
    PRICE = 10
print("Your admission cost is $" + str(PRICE) + ".")

AGE = 12
if AGE < 4:
    PRICE = 0
elif AGE < 18:
    PRICE = 5
elif AGE < 65:
    PRICE = 10
else:
    PRICE = 5
print("Your admission cost is $" + str(PRICE) + ".")

# elif can be final block as well
AGE = 12
if AGE < 4:
    PRICE = 0
elif AGE < 18:
    PRICE = 5
elif AGE < 65:
    PRICE = 10
elif AGE >= 65:
    PRICE = 5
print("Your admission cost is $" + str(PRICE) + ".")
