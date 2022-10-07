from random import randint

LN = 50  # LN - largest number of range
n = randint(0, LN)

# TODO: computer can generate 0 also
answer = str(input("I thought of a number from 0 to " + str(LN) + ". Do you want to guess?\n"))
if 'yes' in answer or 'YES' in answer or 'Yes' in answer:
    print('OK. Input your number:')
elif 'no' in answer or 'NO' in answer or 'No' in answer:
    print('OK. Bye!')
    exit()
else:
    print("I'm sorry, but I don't understand you!")
    exit()

# TODO: program fails on non-numerical input
a = int(input())

try:
    if a == n:
        print('Fantastic! Well done!!!')
        exit()
    elif a > n:
        print('Your number is a little more than my')
    elif a < n:
        print('My number is a little more than yours')
except ValueError:
    print('\nThis is not a number. Try again...')
    exit()

print(n)
