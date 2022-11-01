f1 = 0
f2 = 1
for i in range(1, 1000):
    if f2 <= 1000:
        f1, f2 = f2, f1 + f2
    else:
        break
    print (f2)
