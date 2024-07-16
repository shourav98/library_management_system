import json
from book import Book

def save_data(books, borrowed_books):
    data = {
        'books': [book.__dict__ for book in books],
        'borrowed_books': borrowed_books
    }
    try:
        with open('library_data.json', 'w') as file:
            json.dump(data, file)
    except IOError as e:
        print(f"Error saving data to file: {e}")

def load_data():
    try:
        with open('library_data.json', 'r') as file:
            data = json.load(file)
            books = [Book(**book) for book in data['books']]
            borrowed_books = data['borrowed_books']
            return books, borrowed_books
    except FileNotFoundError:
        return [], {}
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading data from file: {e}")
        return [], {}
