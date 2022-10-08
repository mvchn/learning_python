from random import randint
SN = 0   # SN - smallest number of range
LN = 50  # LN - largest number of range
n = randint(SN, LN)

answer = str(input("I'm thinking of a number from " + str(SN) + " to " + str(LN) + ". Do you want to guess?\n"))
if 'yes' in answer or 'YES' in answer or 'Yes' in answer:
    print('OK!')
elif 'no' in answer or 'NO' in answer or 'No' in answer:
    print('OK. Bye!')
    exit()
else:
    print("I'm sorry, but I don't understand you!")
    exit()

a = int(input('Input your number:'))
if type(a) == int:
    if SN <= a <= LN:
        if a == n:
            print('Fantastic! Well done!!!')
            exit()
        elif a > n:
            print('Your number is a little more than mine')
        elif a < n:
            print('Your number is a little less than mine')
    else:
        print("\nPlease, input a number from " + str(SN) + " to " + str(LN))
        exit()
else:
    print('The variable is not a number')

print(n)
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
