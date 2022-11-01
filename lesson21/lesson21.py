def linear_search(a, n, x):
    res = -1
    i = 0

    for item in a[:n]:
        if item == x:
            res = i
        i += 1

    return res


books = ['python crash course', 'learn python the hard way', 'effective java', 'test', 'one', 'two']

find = 'one'
border = 30

result = linear_search(books, border, find)

print(result)
