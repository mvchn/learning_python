def linear_search(a, n, x):
    for i, item in enumerate(a[:n]):
        if item == x:
            return i
        i += 1

    return -1


books = ['python crash course', 'learn python the hard way', 'effective java', 'test', 'one', 'two']

find = 'one'
border = 30

result = linear_search(books, border, find)

print(result)
