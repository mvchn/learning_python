""" To write table with books:
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
"""

CURR = "$"
INDEX_SIZE = 3

categories = ['python', 'java', 'python', 'php']
titles = ['python crash course', 'learn python the hard way', 'effective java']
authors = ['eric matthes', 'zed shaw', 'joshua bloch']
prices = [10/3, 20/3, 9/3]

for index in range(0,INDEX_SIZE):
    CURR = "USD"
    print(f"{index + 1}. '{titles[index].title()}', '{authors[index].upper()}', {round(prices[index], 2)} {CURR},  - {categories[index]}")
    #print(index)

print(CURR)