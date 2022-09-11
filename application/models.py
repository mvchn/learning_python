class Book:

    def __init__(self, id, author, title, price, category, popularity):
        self.id = id
        self.author = author
        self.title = title
        self.price = price
        self.category = category
        self.popularity = popularity

    def get_id(self):
        return self.id

    def get_name(self):
        return f"{self.title} {self.author.upper()}"

    def print_book(self):
        print(f"ID: {self.id}")
        print(f"Author: {self.author}")
        print(f"Title: {self.title}")
        print(f"Price: {self.price}")
        print(f"Category: {self.category}")
        print(f"Popularity: {self.popularity}")
        print('-----------')


class Shelf:
    def __init__(self, name):
        self.books = []
        self.name = name

    def add_book(self, book):
        self.books.append(book)
