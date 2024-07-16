from book import Book
from borrower import Borrower
import storage

class Library:
    def __init__(self):
        self.books = []
        self.borrower = Borrower()
        self.load_data()

    def add_book(self, title, authors, isbn, publishing_year, price, quantity):
        try:
            new_book = Book(title, authors, isbn, publishing_year, price, quantity)
            self.books.append(new_book)
            self.save_data()
        except ValueError as e:
            print(f"Error adding book: {e}")

    def view_books(self):
        if not self.books:
            print("No books available in the library.")
        for book in self.books:
            print(book)

    def search_books(self, term):
        results = [book for book in self.books if term.lower() in book.title.lower() or term in book.isbn]
        if not results:
            print("No books found matching the search term.")
        for book in results:
            print(book)

    def search_by_author(self, author_name):
        results = [book for book in self.books if any(author_name.lower() in author.lower() for author in book.authors)]
        if not results:
            print("No books found matching the author's name.")
        for book in results:
            print(book)

    def remove_book(self, term):
        for book in self.books:
            if term.lower() in book.title.lower() or term in book.isbn:
                self.books.remove(book)
                self.save_data()
                print("Book removed successfully.")
                return
        print("Book not found to remove.")

    def lend_book(self, isbn, borrower_name):
        for book in self.books:
            if book.isbn == isbn:
                if book.quantity > 0:
                    book.quantity -= 1
                    self.borrower.lend_book(isbn, borrower_name)
                    self.save_data()
                    print("Book lent successfully.")
                    return
                else:
                    print("Not enough books available to lend.")
                    return
        print("Book not found.")

    def return_book(self, isbn, borrower_name):
        for book in self.books:
            if book.isbn == isbn:
                book.quantity += 1
                self.borrower.return_book(isbn, borrower_name)
                self.save_data()
                print("Book returned successfully.")
                return
        print("Book not found.")

    def view_lent_books(self):
        self.borrower.view_lent_books()

    def save_data(self):
        try:
            storage.save_data(self.books, self.borrower.borrowed_books)
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        try:
            self.books, self.borrower.borrowed_books = storage.load_data()
        except Exception as e:
            print(f"Error loading data: {e}")
            self.books, self.borrower.borrowed_books = [], {}
