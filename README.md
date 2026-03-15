Library Management System CLI 

A clean and efficient Command Line Interface (CLI) application built in Python to manage a personal book collection. This system uses Object-Oriented Programming (OOP) to allow users to catalog books and perform targeted searches by title, author, or genre.

 Key Features
Book Cataloging: Add new books with specific details including Title, Author, and Genre.

Multi-Criteria Search:

Search by Title.

Search by Author.

Search by Genre.

Case-Insensitive Retrieval: Find books regardless of whether you type in uppercase or lowercase.

Inventory Display: View a complete list of all books currently held in the library system.

Interactive Menu: A user-friendly, numbered menu system for easy navigation.

Technical Overview
The application is structured into two primary classes to ensure code clarity and reusability:
Class            Purpose
Book            Acts as a data container for individual book attributes (Title, Author, Genre).
Library         Contains the core logic for adding books, filtering the collection, and displaying results.

How to Use
Launch the System: Run the script using Python:

Bash
python main.py
Add a Book: Select option 1 and enter the requested details.

Find a Book: Use options 2, 3, or 4 to search your collection by your preferred criteria.

View All: Select option 5 to print the entire library inventory to the console.

Exit: Select option 6 to close the application.

 Sample Data
The system comes pre-loaded with a few classics to get you started, including:

1984 by George Orwell

To Kill a Mockingbird by Harper Lee

Surprisely by Francess Ekezie
