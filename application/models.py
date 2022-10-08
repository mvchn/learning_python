class Book:

    def __init__(self, book_id, author, title, price, category, popularity):
        self.book_id = book_id
        self.author = author
        self.title = title
        self.price = price
        self.category = category
        self.popularity = popularity

    def get_id(self):
        return self.book_id

    def get_name(self):
        return f"{self.title} {self.author.upper()}"

    def print_book(self):
        print(f"ID: {self.book_id}")
        print(f"Author: {self.author}")
        print(f"Title: {self.title}")
        print(f"Price: {self.price}")
        print(f"Category: {self.category}")
        print(f"Popularity: {self.popularity}")
        print('-----------')


class Shelf:
    def __init__(self, name):
        self.books = {}
        self.name = name

    def add_book(self, book):
        self.books[book.get_id()] = book

    def find(self, book_id):
        return self.books.get(book_id, None)
