"""
    Exercises on working with lists of numbers
"""

print("Counting 1 to 20:")
for number in range(1, 21):
    print(number)

# Takes some time
# print("Counting 1 to 1.000.000")
# for number in range(1, 1000001):
#     print(number)

print("Sum of numbers from 1 to 1.000.000: " + str(sum(range(1, 1000001))))

print("Odd numbers:")
for number in range(1, 21, 2):
    print(number)

print("Threes:")
for number in range(3, 31, 3):
    print(number)

print("Cubes:")
for number in [x**3 for x in range(1, 11)]:
    print(number)
