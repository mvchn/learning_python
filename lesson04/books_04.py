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
        - remove code duplicates (if exists)      
    Update04:        
        + increase final prices for most popular book by 100%
        + sell the most popular book 
        + add more books
        + add constant TAX_RATE
        - calculate taxes 
        - remove code duplicates (if exists) 
'''

CURR = "$"
INDEX_SIZE = 3

categories = ['python', 'python', 'java', 'php']
titles = ['python crash course', 'learn python the hard way', 'effective java']
authors = ['eric matthes', 'zed shaw', 'joshua bloch']
prices = [10/3, 20/3, 9/3]
popularity = [4, 8, 2]

def increase_price(key):
    prices[key] = prices[key] * 2;

def print_books(max_key):
    for index in range(0, max_key):
        print(f"{index + 1}. '{titles[index].title()}', '{authors[index].upper()}', {round(prices[index], 2)} {CURR},  - {categories[index]}")

    print('-------------------')

def sell(key):
    return prices[key]

for index in range(0, INDEX_SIZE):
    if categories[index] == 'python':
        prices[index] = prices[index] * 1.3
    elif categories[index] == 'java':
        prices[index] = prices[index] * 0.9

print_books(INDEX_SIZE)

k = max(popularity)
print (f" The most popular book is '{titles[popularity.index(k)].title()}' {authors[popularity.index(k)].upper()}")


increase_price(popularity.index(k))

value = sell(popularity.index(k))

TAX_RATE = 0.05

tax = value * 0.05
clean_value = value - tax


print(clean_value)

categories.insert(3, 'java')
titles.append('java: the complete reference')
authors.append('herbert schildt')
prices.append(17/5)
popularity.append(11)

print_books(INDEX_SIZE+1)

books_sold = [40, 80, 20, 110]

for index in range(0, INDEX_SIZE):
    taxes = prices[index] * books_sold[index] * TAX_RATE

#print (taxes)
