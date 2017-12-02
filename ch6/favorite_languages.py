""" 
    Dictionary with lists
"""

FAVORITE_LANGUAGES = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in FAVORITE_LANGUAGES.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

for name, languages in FAVORITE_LANGUAGES.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
    else:
        print("\n" + name.title() + "'s favorite language is:")
    for language in languages:
        print("\t" + language.title())
