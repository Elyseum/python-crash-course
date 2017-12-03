""" Importing standard lib """

from collections import OrderedDict

FAV_LANGS = OrderedDict()

FAV_LANGS['jen'] = 'python'
FAV_LANGS['sarah'] = 'c'
FAV_LANGS['edward'] = 'ruby'
FAV_LANGS['phil'] = 'python'

for name, language in FAV_LANGS.items():
    print(name.title() + "'s favorite language is " + language.title())
