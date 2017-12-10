""" Working with exceptions """

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


try:
    ANSWER = 5/2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(ANSWER)
