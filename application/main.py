"""

"""

from func.functions import print_books
from action.classes import MarketEvent
from const.constants import CURR
from models import Book
from models import Shelf



#print_books(books, CURR)

filename = 'database.txt'

try:
    with open(filename) as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"File {filename} not found")
    exit()

shelf = Shelf

for line in lines:

    pieces = line.split(",")
    item = Book(pieces[0].strip(), pieces[1].strip(), pieces[2].strip(), pieces[3].strip(), pieces[4].strip(), pieces[5].strip())
    # TODO: fix line
    #shelf.add_book(item)
    print(f"{item.get_id()}. {item.get_name()}")


id = input('Enter id: ')

item.print_book()

# event = MarketEvent(id, '30.08.2022', 10, CURR)
#
# event.print_event()
