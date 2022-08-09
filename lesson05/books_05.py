""" To write table with books:
    - title (capitalize first letters)
    - author (upper case)
    - price (rounded)
    Update01:
        - add category
        - add currency for price (use constant)
        - remove code duplicates (use list)
    Update02:
        - use range for index in cycle
        - remove space in constant CURR
        - add index size to constants
        - slice lists to the index size 
        - remove code duplicates (if exists)   
    Update03:
        - increase final prices for python books by 30%
        - reduce final prices for java books by 10%
        - control lists size
        - show the most popular book 
        - remove code duplicates (if exists)      
    Update04:        
        + increase final prices for most popular book by 100%
        + sell the most popular book 
        + add more books
        + add constant TAX_RATE
        + calculate taxes 
        - remove code duplicates (if exists) 
    Update05:       
        + remove unnecessary variables and constants
        + describe functions by comments
        + sell books, not popularity 
        + add a new 3 books to the storage
        - create a new sell cycle (2 sell cycles should be in the result)
    Update06:
        - get most popular book  ( 1 )
        - create a new sell cycle (2 sell cycles should be in the result) ( 32 )
        - business value volume (events structure) ( 2 )
        - ask user about sold books (user must input id) ( 32 )
        - create function to search book by id ( 8 )
        - remove INDEX_SIZE constant ( 1 )
        - create formula for popularity ( 8 )
        - remove formula for price ( 4 )
        - books list should be an argument in print_books ( 32 )
        - books list should be an argument in get_most_popular ( 32 )
"""

CURR = "$"
INDEX_SIZE = 3
INDEX_POPULARITY = 10 # A unit of popularity is equal to 10 books sold

books = [
    {
        'id': '01',
        'author': 'eric matthes',
        'title': 'python crash course',
        'price': 10 / 3,
        'category': 'python',
        'popularity': 4,
    },
    {
        'id': '02',
        'author': 'zed shaw',
        'title': 'learn python the hard way',
        'price': 20 / 3,
        'category': 'python',
        'popularity': 8,
    },
    {
        'id': '03',
        'author': 'joshua bloch',
        'title': 'effective java',
        'price': 9 / 3,
        'category': 'java',
        'popularity': 2,
    },
]


def increase_price(book):
    """ Prices increases up to 100% """
    book['price'] = book['price'] * 2


def print_books():
    for book in books:
        print(
            f"{book['id']}. '{book['title'].title()}', '{book['author'].upper()}', {round(book['price'], 2)} {CURR},  - {book['category']}")

    print('-------------------')


def print_book(book):
    print(
        f" The most popular book is '{book['title'].title()}' {book['author'].upper()}")


def sell(book):
    return book['price']


def get_most_popular():
    popularity = 0

    for book in books:
        if book['popularity'] > popularity:
            # max_popularity_index =
            popularity = book['popularity']

    # TODO: get most popular book
    return books[0]


for index in range(0, INDEX_SIZE):
    if books[index]['category'] == 'python':
        books[index]['price'] = books[index]['price'] * 1.3
    elif books[index]['category'] == 'java':
        books[index]['price'] = books[index]['price'] * 0.9

print_books()

# books[popularity.index(k)]
book = get_most_popular()
print_book(book)

increase_price(book)

value = sell(book)

TAX_RATE = 0.05

tax = value * 0.05
clean_value = value - tax

books.append({
    'id': '04',
    'author': 'herbert schildt',
    'category': 'java',
    'title': 'java: the complete reference',
    'price': 17 / 5,
    'popularity': 0,
})

books.append({
    'id': '05',
    'author': 'barbara doylet',
    'category': 'c#',
    'title': 'c# programming: from problem analysis to program designe',
    'price': 14 / 9,
    'popularity': 32,
})

books.append({
    'id': '06',
    'author': 'david flanagan',
    'category': 'javascript',
    'title': "javascript: the definitive guide: master the world's most-used programming language",
    'price': 22 / 7,
    'popularity': 4,
})

books.append({
    'id': '07',
    'author': 'michael lombard',
    'category': 'python',
    'title': 'python: learn python programming in one week with step-by-step',
    'price': 17 / 9,
    'popularity': 8,
})

print_books()

events = [
    {
        'book_id': '07',
        'price': 10.5
    },
    {
        'book_id': '05',
        'price': 8.5
    },
]
largest_popularity = -1
for book in books:
    if book['popularity'] <= largest_popularity:
        continue
    largest_popularity = book['popularity']
print('Largest popularity is', largest_popularity)

for book in books:
    val = book['price'] * book ['popularity'] * INDEX_POPULARITY
    print (book['id'], round(val), CURR)

for index in range(0, len(books)):
    if books[index]['category'] == 'python':
        books[index]['price'] = books[index]['price'] * 1.3
    elif books[index]['category'] == 'java':
        books[index]['price'] = books[index]['price'] * 0.9
print_books()
