""" Read from a file as json """

import json

FILENAME = 'ch10/numbers.json'

with open(FILENAME) as f_obj:
    NUMBERS = json.load(f_obj)

print(NUMBERS)
