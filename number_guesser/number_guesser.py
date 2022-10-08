from random import randint
n = randint(0, 100)
answer = str(input('I thought of a number from 1 to 100. Do you want to guess?\n'))
if 'yes' in answer or 'YES' in answer or 'Yes' in answer:
    print('OK. Input your number:')
elif 'no' in answer or 'NO' in answer or 'No' in answer:
    print ('OK. Bye!')#stop
else:
    print ("I'm sorry, but I don't understand you!")#stop

a = int(input())
if a == n:
    print ('Fantastic! Well done!!!')#stop
elif a > n:
    print ('Your number is a little more than my')
elif a < n:
    print('My number is a little more than yours')

print(n)