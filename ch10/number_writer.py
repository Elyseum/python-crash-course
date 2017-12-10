""" Writing to file """

import json

NUMBERS = [2, 3, 5, 7, 11, 13]

FILENAME = 'ch10/numbers.json'
with open(FILENAME, 'w') as f_obj:
    json.dump(NUMBERS, f_obj)
