""" Exceptions when reading files """

FILENAME = 'ch10/alice_does_not_exist.txt'
try:
    with open(FILENAME) as f_obj:
        CONTENTS = f_obj.read()
except FileNotFoundError:
    print("Sorry, can't find '" + FILENAME + "'.")

FILENAME = 'ch10/alice.txt'
try:
    with open(FILENAME) as f_obj:
        CONTENTS = f_obj.read()
except FileNotFoundError:
    print("Sorry, can't find '" + FILENAME + "'.")
else:
    WORDS = CONTENTS.split()
    NUM_WORDS = len(WORDS)
    print("The file '" + FILENAME + "' has " + str(NUM_WORDS) + " words.")
