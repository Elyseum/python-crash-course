""" writing to a file """

FILENAME = 'ch10/programming.txt'

with open(FILENAME, 'w') as file_object:
    file_object.write("I love programming.")

with open(FILENAME, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
