from random import randint

LOW_BORDER = 0
HIGH_BORDER = 50

computer_number = randint(LOW_BORDER, HIGH_BORDER)

answer = str(input("I'm thinking of a number from " + str(LOW_BORDER) + " to " + str(HIGH_BORDER) + ". Do you want to guess?\n"))

if 'yes' in answer or 'YES' in answer or 'Yes' in answer:
    print('OK!')
elif 'no' in answer or 'NO' in answer or 'No' in answer:
    print('OK. Bye!')
    exit()
else:
    print("I'm sorry, but I don't understand you!")
    exit()

user_number = input('Input your number: ')

try:
    user_number = int(user_number)
except ValueError:
    print('You should input a number!')
    exit()

if user_number == computer_number:
    print('Fantastic! Well done!!!')
    exit()
elif user_number > computer_number:
    print('Your number is a little more than my')
elif user_number < computer_number:
    print('Your number is a little less than mine')

