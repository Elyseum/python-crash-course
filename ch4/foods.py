"""
    Copying a list
"""

MY_FOODS = ['pizza', 'falafel', 'carrot cake']
FRIEND_FOODS = MY_FOODS[:] # copy all

print("\nMy favorite foods are:")
print(MY_FOODS)
print("\nMy friend's favorite foods are:")
print(FRIEND_FOODS)

MY_FOODS = ['pizza', 'falafel', 'carrot cake']
FRIEND_FOODS = MY_FOODS[:] # copy all

MY_FOODS.append('cannoli')
FRIEND_FOODS.append('ice cream')

print("\nMy favorite foods are:")
print(MY_FOODS)
print("\nMy friend's favorite foods are:")
print(FRIEND_FOODS)
