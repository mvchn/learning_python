def archivation(input):
    res = ''
    # TODO: add loop
    # TODO: use structure for input
    for index in input:
        if input[index] == 'A':
            res += 'A'

    # if input[0] == 'A':
    #     if input[1] == 'A':
    #         if input[2] == 'A':
    #             if input[3] == 'A':
    #                 res += 'A4'
    # if input[4] == 'T':
    #     if input[5] == 'T':
    #         res += 'T2'

    return res


result = archivation("AAAATTBBNOOOOS")  # A4T2B2NO4S

print(result)
