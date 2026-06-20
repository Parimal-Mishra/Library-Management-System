# Library Management System

A simple Python CLI application for managing books, users, and borrowing operations using object-oriented programming.

## What this project does

This project lets you add and list library books, search books by prefix, add users, borrow and return books, and view current borrower activity from a command-line menu. It stores data in memory while the program runs and demonstrates how classes can collaborate to manage application state and user interaction.

## How it works

- `main.py` starts the application by creating and running an `OperationsManager` instance.
- `OperationsManager.py` displays the menu, validates user choices, and routes commands to the admin logic.
- `Admin.py` manages the in-memory book and user collections and handles borrowing and returning books.
- `Book.py` defines the book object with `id`, `name`, and `quantity`.
- `User.py` defines the user object with `id`, `name`, and a list of borrowed books.
- `utility.py` validates numeric menu input.

## OOP Concepts Used

- Encapsulation: `Book`, `User`, `Admin`, and `OperationsManager` each encapsulate their specific data and behavior.
- Abstraction: `OperationsManager` provides a simple menu interface while `Admin` handles the business logic.
- Inheritance: Not used explicitly in this project; the design relies on composition between classes.
- Polymorphism: Implemented via object string representations (`__str__`) for readable display.
- Classes and objects: `Book`, `User`, `Admin`, and `OperationsManager` are classes, and each book or user record is an object instance.

## Features

- Add a new book with a unique numeric ID.
- List all books with available quantities.
- Search books by name prefix.
- Add new users.
- Borrow books and decrement available quantity.
- Return books and restore available quantity.
- Print users who currently have borrowed books.
- List all users in the system.

## Project files

- `main.py`: Application entry point.
- `OperationsManager.py`: Menu logic and user interaction.
- `Admin.py`: Library business logic and data management.
- `Book.py`: Book data model.
- `User.py`: User data model and borrowing state.
- `utility.py`: Input validation helper.

## Usage

Run the application with:

```bash
python main.py
```

Then use the numbered menu to add books, users, borrow and return books, and view current records.

## Notes

- Data is stored only in memory while the program runs.
- There is no file or database persistence.
- Book search uses prefix matching on book names.
- Input validation is handled with `input_is_valid()` for numeric menu choices.


