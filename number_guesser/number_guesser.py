from random import randint


def hello_casino():
    answer = str(input('I thought of a number from 1 to 100. Do you want to guess?\n'))
    if 'yes' in answer or 'YES' in answer or 'Yes' in answer:
        print('OK. Input your number:')
    elif 'no' in answer or 'NO' in answer or 'No' in answer:
        print('OK. Bye!')
    else:
        print("I'm sorry, but I don't understand you!")


def choice(c, u):
    if u == c:
        return 'well_done'
    elif u > c:
        return 'little_more'
    elif u < c:
        return 'little_less'


def main():

    messages = {
        'well_done' : '*** Fantastic! Well done!!! ***',
        'little_more' : 'Your number is a little more',
        'little_less' : 'Your number is a little less'
    }

    hello_casino()
    computer = randint(0, 1)
    user = int(input())
    message = choice(computer, user)
    print(messages[message])


if __name__ == '__main__':
    main()
