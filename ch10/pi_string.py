""" Interpreting a read file """

FILENAME = 'ch10/pi_digits.txt'
with open(FILENAME) as file_object:
    LINES = file_object.readlines()

PI_STRING = ''
for line in LINES:
    PI_STRING += line.strip()
print(PI_STRING)
print(len(PI_STRING))

FILENAME = 'ch10/pi_million_digits.txt'
with open(FILENAME) as file_object:
    LINES = file_object.readlines()

PI_STRING = ''
for line in LINES:
    PI_STRING += line.strip()

print(PI_STRING[:52] + "...")
print(len(PI_STRING))

# Birthday

FILENAME = 'ch10/pi_million_digits.txt'
with open(FILENAME) as file_object:
    LINES = file_object.readlines()

PI_STRING = ''
for line in LINES:
    PI_STRING += line.strip()

BIRTHDAY = "030787"

if BIRTHDAY in PI_STRING:
    print("Your birthday appears in the first million digits of PI.")
else:
    print("Your birthday does not appear in the first million digits of PI :(.")

BIRTHDAY = "120372"

if BIRTHDAY in PI_STRING:
    print("Your birthday appears in the first million digits of PI.")
else:
    print("Your birthday does not appear in the first million digits of PI :(.")
