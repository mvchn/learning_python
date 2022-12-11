def archivation(input):
    res = {}

    for index in input:
        if index not in res.keys():
            res[index] = 1
        else:
            res[index] += 1

    return res


result = archivation("AAAATTBBNOOOOS")  # A4T2B2NO4S

print(result)
