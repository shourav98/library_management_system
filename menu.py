from library import Library

def display_menu():
    print("Library Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Books")
    print("4. Search Books by Author")
    print("5. Remove Book")
    print("6. Lend Book")
    print("7. View Lent Books")
    print("8. Return Book")
    print("9. Exit")

def handle_option(library):
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter title: ")
            authors = input("Enter authors (comma separated): ").split(',')
            isbn = input("Enter ISBN: ")
            publishing_year = input("Enter publishing year: ")
            price = input("Enter price: ")
            quantity = input("Enter quantity: ")
            library.add_book(title, authors, isbn, publishing_year, price, quantity)
        elif choice == '2':
            library.view_books()
        elif choice == '3':
            term = input("Enter search term (title or ISBN): ")
            library.search_books(term)
        elif choice == '4':
            author_name = input("Enter author name: ")
            library.search_by_author(author_name)
        elif choice == '5':
            term = input("Enter title or ISBN to remove: ")
            library.remove_book(term)
        elif choice == '6':
            isbn = input("Enter ISBN: ")
            borrower_name = input("Enter borrower name: ")
            library.lend_book(isbn, borrower_name)
        elif choice == '7':
            library.view_lent_books()
        elif choice == '8':
            isbn = input("Enter ISBN: ")
            borrower_name = input("Enter borrower name: ")
            library.return_book(isbn, borrower_name)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")
