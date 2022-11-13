def fibbo(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibbo(i-1) + fibbo(i-2)


num = int(input("Enter range border:"))
print('---------')
print(fibbo(num))
print('---------')
f1 = 0
f2 = 1
for i in range(1, num):
    if f2 <= num:
        f1, f2 = f2, f1 + f2
    else:
        break
    print(f2)
