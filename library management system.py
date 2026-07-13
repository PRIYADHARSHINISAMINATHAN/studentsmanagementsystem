class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists!")
                return

        self.books.append(Book(book_id, title, author))
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n------ Library Books ------")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"ID: {book.book_id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Status: {status}")
            print("-" * 30)

    def search_book(self):
        title = input("Enter book title to search: ").lower()

        found = False
        for book in self.books:
            if title in book.title.lower():
                status = "Available" if book.available else "Borrowed"
                print("\nBook Found")
                print(f"ID: {book.book_id}")
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Status: {status}")
                found = True

        if not found:
            print("Book not found!")

    def borrow_book(self):
        book_id = input("Enter Book ID to borrow: ")

        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book borrowed successfully!")
                else:
                    print("Book is already borrowed.")
                return

        print("Book not found!")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book returned successfully!")
                else:
                    print("Book is already available.")
                return

        print("Book not found!")

    def delete_book(self):
        book_id = input("Enter Book ID to delete: ")

        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book deleted successfully!")
                return

        print("Book not found!")


library = Library()

while True:
    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.borrow_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.delete_book()

    elif choice == "7":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")