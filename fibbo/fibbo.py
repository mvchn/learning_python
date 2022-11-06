num = int(input("Enter range border:"))
f1 = 0
f2 = 1
for i in range(1, num):
    if f2 <= num:
        f1, f2 = f2, f1 + f2
    else:
        break
    print (f2)
