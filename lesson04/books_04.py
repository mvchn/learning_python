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
"""

CURR = "$"
INDEX_SIZE = 3

popularity = [4, 8, 2]

books = [
{
    'id': '01',
    'author': 'eric matthes',
    'title': 'python crash course',
    'price': 10/3,
    'category': 'python'
},
{
    'id': '02',
    'author': 'zed shaw',
    'title': 'learn python the hard way',
    'price': 20/3,
    'category': 'python'
},
{
    'id': '03',
    'author': 'joshua bloch',
    'title': 'effective java',
    'price': 9/3,
    'category': 'java'
},
]


def increase_price(key):
    books[key]['price'] = books[key]['price'] * 2;

def print_books(max_key):
    for book in books:
        print(f"{book['id']}. '{book['title'].title()}', '{book['author'].upper()}', {round(book['price'], 2)} {CURR},  - {book['category']}")

    print('-------------------')

def sell(key):
    return books[key]['price']

for index in range(0, INDEX_SIZE):
    if books[index]['category'] == 'python':
        books[index]['price'] = books[index]['price'] * 1.3
    elif books[index]['category'] == 'java':
        books[index]['price'] = books[index]['price'] * 0.9

print_books(INDEX_SIZE)

k = max(popularity)
print (f" The most popular book is '{books[popularity.index(k)]['title'].title()}' {books[popularity.index(k)]['author'].upper()}")


increase_price(popularity.index(k))

value = sell(popularity.index(k))

TAX_RATE = 0.05

tax = value * 0.05
clean_value = value - tax


books.append({
    'id' : '04',
    'category' : 'java',
    'title': 'java: the complete reference',
    'price': 17/5
    })

print(clean_value)




