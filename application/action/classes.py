class MarketEvent:

    def __init__(self, book_id, date, price, currency):
        self.book_id = book_id
        self.date = date
        self.price = price
        self.currency = currency

    def print_event(self):
        print(f"ID: {self.book_id}")
        print(f"Date: {self.date}")
        print(f"Price: {self.price}{self.currency}")
