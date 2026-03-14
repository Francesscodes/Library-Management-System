class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


class Library:
    def __init__(self):
        self.books = []

    # Fix: all methods are now properly indented INSIDE the Library class

    def add_book(self, title, author, genre):
        book = Book(title, author, genre)
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def search_books_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        self.display_books(found_books)

    def search_books_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        self.display_books(found_books)

    def search_books_by_genre(self, genre):
        found_books = [book for book in self.books if book.genre.lower() == genre.lower()]
        self.display_books(found_books)

    def display_books(self, books):
        if books:
            print("\nBooks found:")
            for book in books:
                print(f"  Title: {book.title}, Author: {book.author}, Genre: {book.genre}")
        else:
            print("No books found.")


# Create a library
library = Library()

# Add sample books
library.add_book("1984", "George Orwell", "Dystopian Fiction")
library.add_book("To Kill a Mockingbird", "Harper Lee", "Fiction")
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Classic Literature")
library.add_book("Surprisely", "Francess Ekezie", "Business")

# Main menu
while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Search Books by Title")
    print("3. Search Books by Author")
    print("4. Search Books by Genre")
    print("5. Display All Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        library.add_book(title, author, genre)
    elif choice == "2":
        title = input("Enter book title to search: ")
        library.search_books_by_title(title)
    elif choice == "3":
        author = input("Enter book author to search: ")
        library.search_books_by_author(author)
    elif choice == "4":
        genre = input("Enter book genre to search: ")
        library.search_books_by_genre(genre)
    elif choice == "5":
        library.display_books(library.books)
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")