"""

"""

from func.functions import print_books
from action.classes import MarketEvent
from const.constants import CURR

books = [
    {
        'id': 1,
        'author': 'eric matthes',
        'title': 'python crash course',
        'price': 10 / 3,
        'category': 'python',
        'popularity': 2,
    },
    {
        'id': 2,
        'author': 'zed shaw',
        'title': 'learn python the hard way',
        'price': 20 / 3,
        'category': 'python',
        'popularity': 3,
    },
    {
        'id': 3,
        'author': 'joshua bloch',
        'title': 'effective java',
        'price': 9 / 3,
        'category': 'java',
        'popularity': 1,
    },
]

print_books(books, CURR)

print("* sell - start sell cycle")
print("* rev - see revenue")
print("* up - update popularity\n")

# class instance sample

id = input('Enter id: ')

event = MarketEvent(id, '30.08.2022', 10, CURR)

event.print_event()
