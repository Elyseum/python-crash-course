"""
    Chapter 2: print strings
"""

NAME = "ada lovelace"
print(NAME.title())
print(NAME.lower())
print(NAME.upper())

FIRST_NAME = "ada"
LAST_NAME = "lovelace"
FULL_NAME = FIRST_NAME + " " + LAST_NAME
print(FULL_NAME)
print("Hello, " + FULL_NAME.title() + "!")

MESSAGE = "Hello, " + FULL_NAME.title() + "!"
print(MESSAGE)

print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

FAVORITE_LANGUAGE = 'python '
print(FAVORITE_LANGUAGE)
print(FAVORITE_LANGUAGE.rstrip()) # does not modify
print(FAVORITE_LANGUAGE)
