nums = list(range(1,  102))
for num in nums:
    if num % 5 == 0 and num % 3 == 0:
        print(num, '- fizz buzz')
    elif num % 5 == 0:
        print(num, '- buzz')
    elif num % 3 == 0:
        print(num, '- fizz')
    else:
        if num % 2 != 0:
            print(num, '- odd')
        if num % 2 == 0:
            print(num, '- even')
