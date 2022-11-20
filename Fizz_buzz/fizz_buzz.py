for i in range (1,102):
    if i % 5 == 0 and i % 3 == 0:
        print ('fizz_buzz')
    if i % 5 == 0:
        print('buzz')
    if i % 3 == 0:
        print ('fizz')
    else:
        if i % 2 == 0:
            print ('odd')
        if i % 2 != 0:
            print ('even')
