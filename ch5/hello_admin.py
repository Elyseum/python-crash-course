"""
    Try it yourself
"""

USERNAMES = ['eric', 'bob', 'marc', 'admin', 'mike', 'dave']
USER = 'admin'

for user in USERNAMES:
    if user == 'admin':
        print("Hello " + user + ", would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again")

USERNAMES = []
if not USERNAMES:
    print("We need to find some users!")

CURRENT_USERS = ['eric', 'bob', 'marc', 'John', 'mike', 'dave']
NEW_USERS = ['marc', 'dave', 'JOHN', 'joey']
CURRENT_USERS_LOWER = [x.lower() for x in CURRENT_USERS]
for new_user in NEW_USERS:
    if new_user.lower() in CURRENT_USERS_LOWER:
        print("Username " + new_user.title() + " has already been taken!")
    else:
        print("Username " + new_user.title() + " is still available.")

for number in range(1, 10):
    if number == 1:
        suffix = "st"
    elif number == 2:
        suffix = "nd"
    elif number == 3:
        suffix = "rd"
    elif number > 3:
        suffix = "th"

    print(str(number) + suffix)
