class Borrower:
    def __init__(self):
        self.borrowed_books = {}

    def lend_book(self, isbn, borrower_name):
        if isbn in self.borrowed_books:
            self.borrowed_books[isbn].append(borrower_name)
        else:
            self.borrowed_books[isbn] = [borrower_name]

    def return_book(self, isbn, borrower_name):
        if isbn in self.borrowed_books:
            try:
                self.borrowed_books[isbn].remove(borrower_name)
                if not self.borrowed_books[isbn]:
                    del self.borrowed_books[isbn]
            except ValueError:
                print(f"{borrower_name} did not borrow book with ISBN {isbn}.")

    def view_lent_books(self):
        if not self.borrowed_books:
            print("No books are currently lent out.")
        for isbn, borrowers in self.borrowed_books.items():
            print(f"ISBN: {isbn}, Borrowed by: {', '.join(borrowers)}")
