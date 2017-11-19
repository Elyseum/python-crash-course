"""
    Special support for numbers when using for loop
"""

print("Range [1-5[:")
for value in range(1, 5): # Note that 5 is no included
    print(value)

print("Range [1-5]:")
for value in range(1, 6):
    print(value)

print("Numbers as a list:")
NUMBERS = list(range(1, 6))
print(NUMBERS)

print("Even numbers:")
EVEN_NUMBERS = list(range(2, 11, 2))
print(EVEN_NUMBERS)

print("Squares:")
SQUARES = []
for value in range(1, 11):
    square = value**2
    SQUARES.append(square)
print(SQUARES)

DIGITS = list(range(0, 10))
print("\nDigits: " + str(DIGITS))
print("Min: " + str(min(DIGITS)))
print("Max: " + str(max(DIGITS)))
print("Sum: " + str(sum(DIGITS)))

print("Squares as list comprehension:")
SQUARES = [value**2 for value in range(1, 11)]
print(SQUARES)
