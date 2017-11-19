"""
    Check if a value is in a list (or not)
"""

BANNED_USERS = ['andrew', 'carolina', 'david']
USER = 'david'

if USER in BANNED_USERS:
    print(USER.title() + ", you can not post a response!")

BANNED_USERS = ['andrew', 'carolina', 'david']
USER = 'marie'

if USER not in BANNED_USERS:
    print(USER.title() + ", you can post a response if you wish.")
