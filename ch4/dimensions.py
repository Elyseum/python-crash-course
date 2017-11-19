"""
    Lists that can't be changed: tuples
"""

DIMENSIONS = (200, 50)
print(DIMENSIONS[0])
print(DIMENSIONS[1])

# Next statement doesn't work.
# It will give a typeError because tuples don't support item assignment

# DIMENSIONS[0] = 250

for dimension in DIMENSIONS:
    print(dimension)
