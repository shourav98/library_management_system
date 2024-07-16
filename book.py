class Book:
    def __init__(self, title, authors, isbn, publishing_year, price, quantity):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.publishing_year = publishing_year
        try:
            self.price = float(price)
        except ValueError:
            raise ValueError("The book price should be a floating number.")
        try:
            self.quantity = int(quantity)
        except ValueError:
            raise ValueError("The book quantity should be an integer.")

    def __repr__(self):
        return f"Title: {self.title}, Authors: {', '.join(self.authors)}, ISBN: {self.isbn}, Year: {self.publishing_year}, Price: ${self.price:.2f}, Quantity: {self.quantity}"
