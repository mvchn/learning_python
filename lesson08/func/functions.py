
CURR = "$"


def popularity_formula(c):
    return c * 2 * 2


def print_books(books):
    for book in books:
        print(
            f"{book['id']}. '{book['title'].title()}', '{book['author'].upper()}', {round(book['price'], 2)} {CURR},  - {book['category']}, /{popularity_formula(book['popularity'])}/")

    print('-------------------')
