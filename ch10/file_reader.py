""" Read from a file"""

with open('ch10/pi_digits.txt') as file_object:
    FILE_CONTENT = file_object.read() # reads the entire content
    print(FILE_CONTENT)
print("Done")

FILENAME = 'ch10/pi_digits.txt'
with open(FILENAME) as file_object:
    for line in file_object:
        print(line)
print("Done")

FILENAME = 'ch10/pi_digits.txt'
with open(FILENAME) as file_object:
    for line in file_object:
        print(line.rstrip())
print("Done")

FILENAME = 'ch10/pi_digits.txt'
with open(FILENAME) as file_object:
    LINES = file_object.readlines()

for line in LINES:
    print(line.rstrip())
print("Done")
