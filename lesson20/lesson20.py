import random
start = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

print(start)

print (start[10])
random.shuffle(start)
print (start[12])
random_item = random.choice(start)
start.remove(random_item)
random_item_2 = random.choice(start)
start.remove(random_item_2)
start.sort
print(start)


