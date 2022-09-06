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
        print(f"Popularity: {self.popularity}")
        print('-----------')


filename = 'database.txt'

try:
    with open(filename) as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"File {filename} not found")
    exit()

for line in lines:
    pieces = line.split(",")
    item = Book(pieces[0].strip(), pieces[1].strip(), pieces[2].strip(), pieces[3].strip(), pieces[4].strip(), pieces[5].strip())
    item.print_book()
