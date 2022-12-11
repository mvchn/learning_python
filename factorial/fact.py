def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


i = 7
print("Factorial of", i, "is", factorial(i))

