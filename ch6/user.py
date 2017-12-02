"""
    Looping through dictionaries
"""

USER_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

# tuple destruction
for key, value in USER_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


FAVORITE_LANGUAGES = {
    'jen'   : 'python',
    'sarah' : 'c',
    'edward': 'ruby',
    'phil'  : 'python'
}

print()
for name, language in FAVORITE_LANGUAGES.items():
    print(name.title() + "'s favorite langauge is " + language.title() + ".")

print()
for name in FAVORITE_LANGUAGES.keys():
    print(name.title())

print() # No need to call keys (pylint suggestion)
for name in FAVORITE_LANGUAGES:
    print(name.title())

print()
FRIENDS = ['phil', 'sarah']
for name in FAVORITE_LANGUAGES:
    print(name.title())
    if name in FRIENDS:
        print("\tHi " + name.title() +
              ", I see your favorite language is " +
              FAVORITE_LANGUAGES[name].title())

print()
if 'erin' not in FAVORITE_LANGUAGES:
    print("Erin, please take your poll!")

print()
for name in sorted(FAVORITE_LANGUAGES):
    print(name.title() + ", thank you for taking the poll.")

print()
print("The following languages have been mentioned:")
for language in FAVORITE_LANGUAGES.values():
    print(language.title())

print()
print("The following languages have been mentioned:")
for language in sorted(FAVORITE_LANGUAGES.values()):
    print(language.title())

print()
print("The following languages have been mentioned:")
for language in set(FAVORITE_LANGUAGES.values()):
    print(language.title())
