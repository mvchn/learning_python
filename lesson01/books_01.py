""" To write table with books:
    - title (capitalize first letters)
    - author (upper case)
    - price (rounded)

    Update01: 
        - add category
        - add currency for price (use constant) 
        - remove code duplicates (use list)  
"""

book_title_01 = "python crash course"
book_author_01 = "eric matthes"
book_price_01 = 10/3
book_category_01 = 'python'

book_title_02 = "learn python the hard way"
book_author_02 = "zed shaw"
book_price_02 = 20/3
book_category_02 = 'python'

book_title_03 = "effective java"
book_author_03 = "joshua bloch"
book_price_03 = 9/3
book_category_03 = 'java'

print(f"1. '{book_title_01.title()}', '{book_author_01.upper()}', {round(book_price_01, 2)}")
print(f"2. '{book_title_02.title()}', '{book_author_02.upper()}', {round(book_price_02, 2)}")
print(f"3. '{book_title_03.title()}', '{book_author_03.upper()}', {round(book_price_03, 2)}")