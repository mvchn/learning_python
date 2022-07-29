''' To write table with books:
    - title (capitalize first letters)
    - author (upper case)
    - price (rounded)
    Update01:
        - add category
        - add currency for price (use constant)
        - remove code duplicates (use list)
    Update02:
        - use range for index in cycle
        - remove space in constant CURR
        - add index size to constants
        - slice lists to the index size 
        - remove code duplicates (if exists)   
    Update03:
        - increase final prices for python books by 30%
        - reduce final prices for java books by 10%
        - control lists size
        - show the most popular book 
        - remove code duplicates (if exists)          '''

CURR = "$"
INDEX_SIZE = 3

categories = ['python', 'python', 'java', 'php']
titles = ['python crash course', 'learn python the hard way', 'effective java']
authors = ['eric matthes', 'zed shaw', 'joshua bloch']
prices = [10/3, 20/3, 9/3]
popularity = [4, 8, 2]

if categories[0] == 'python':
    prices[0] = prices[0] * 1.3
elif categories[0:] == 'java':
    prices[0:] = prices[0:] * 0.9
print(prices)

for index in range(0, INDEX_SIZE):
    if categories[index] == 'python':
        prices[index] = prices[index] * 1.3
    elif categories[index] == 'java':
        prices[index] = prices[index] * 0.9

for index in range(0, INDEX_SIZE):
    print(f"{index + 1}. '{titles[index].title()}', '{authors[index].upper()}', {round(prices[index], 2)} {CURR},  - {categories[index]}")



if 'python' in categories[index]:
    prices[index] = prices[index] * 1.3
elif categories == 'java':
    prices[0, INDEX_SIZE] = prices[0, INDEX_SIZE] * 0.9
print(prices)

k = max(popularity)
if k == popularity[0]:
    print (f" The most popular book is '{titles[0].title()}' {authors[0].upper()}")
elif k == popularity[1]:
    print (f" The most popular book is '{titles[1].title()}' {authors[1].upper()}")
elif k == popularity[2]:
    print (f" The most popular book is '{titles[2].title()}' {authors[2].upper()}'")
