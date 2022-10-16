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
        return '*** Fantastic! Well done!!! ***'
    elif u > c:
        return 'Your number is a little more'
    elif u < c:
        return 'Your number is a little less'


def main():
    hello_casino()
    computer = randint(0, 100)
    user = int(input())
    print(choice(computer, user))


if __name__ == '__main__':
    main()
