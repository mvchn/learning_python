class Book:

    def __init__(self, id, author, title, price, category, popularity):
        self.id = id
        self.author = author
        self.title = title
        self.price = price
        self.category = category
        self.popularity = popularity

    def print_book(self):
        print(f"ID: {self.id}")
        print(f"Author: {self.author}")
        print(f"Title: {self.title}")
        print(f"Price: {self.price}")
        print(f"Category: {self.category}")
        print('-----------')


filename = 'database.txt'

try:
    with open(filename) as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"File {filename} not found")

for line in lines:
    # separate line with ,
    item = Book(line[0], line[1], line[2], line[3], line[4], line[5])
    item.print_book()

