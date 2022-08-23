"""

Books

"""

from func.functions import print_books

CURR = "$"

books = [
    {
        'id': '01',
        'author': 'eric matthes',
        'title': 'python crash course',
        'price': 10 / 3,
        'category': 'python',
        'popularity': 2,
    },
    {
        'id': '02',
        'author': 'zed shaw',
        'title': 'learn python the hard way',
        'price': 20 / 3,
        'category': 'python',
        'popularity': 3,
    },
    {
        'id': '03',
        'author': 'joshua bloch',
        'title': 'effective java',
        'price': 9 / 3,
        'category': 'java',
        'popularity': 1,
    },
]

def increase_price(book):
    """ Prices increases up to 100% """
    book['price'] = book['price'] * 2


def sell(book):
    return book['price']


def get_most_popular():
    index_popularity = 0
    most_popular = books[index_popularity]
    for book in books:
        if book['popularity'] > index_popularity:
            index_popularity = book['popularity']
            most_popular = book

    return most_popular

# program start

for book in books:
    if book['category'] == 'python':
        book['price'] = book['price'] * 1.3
    elif book['category'] == 'java':
        book['price'] = book['price'] * 0.9

print_books(books)

# books[popularity.index(k)]
book = get_most_popular()
print(f" The book is '{book['title'].title()}' {book['author'].upper()}")

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

print_books(books)

book = get_most_popular()
print(f" The book is '{book['title'].title()}' {book['author'].upper()}")

market_events = [
    {
        'book_id': '07'
    },
    {
        'book_id': '05'
    },
    {
        'book_id': '03'
    },
    {
        'book_id': '03'
    },
]

INDEX_POPULARITY = 10  # A unit of popularity is equal to 10 books sold

for book in books:
    val = book['price'] * book['popularity'] * INDEX_POPULARITY
    print(book['id'], round(val), CURR)


