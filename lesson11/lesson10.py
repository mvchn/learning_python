from models import Book

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
    #TODO: remove '' in output
    print(f"{item.get_id()}. {item.get_name()}")
    #item.print_book()
