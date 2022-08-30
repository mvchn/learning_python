
def popularity_formula(c):
    return c * 2 * 2


def print_books(books, currency):
    print("Storage state:")

    for book in books:
        print(
            f"{book['id']}. '{book['title'].title()}', '{book['author'].upper()}', {round(book['price'], 2)} {currency},  - {book['category']}, /{popularity_formula(book['popularity'])}/")

    print('-------------------')
