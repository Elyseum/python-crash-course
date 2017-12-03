"""
    Return values
"""

def get_formatted_name(first_name, last_name):
    """ Returns a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

MUSICIAN = get_formatted_name('jimi', 'hendrix')
print(MUSICIAN)

def get_formatted_name_2(first_name, last_name, middle_name=''):
    """ Optional middle name """
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

MUSICIAN = get_formatted_name_2('jimi', 'hendrix')
print(MUSICIAN)

MUSICIAN = get_formatted_name_2('john', 'hooker', 'lee')
print(MUSICIAN)

MUSICIAN = get_formatted_name_2(first_name='john', middle_name='lee', last_name='hooker')
print(MUSICIAN)
