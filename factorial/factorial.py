n = int(input("Input the number:"))
factorial = 1
for i in range(2, n + 1):
    factorial = factorial * i
print("The factorial of ", n, " is: ", factorial)
