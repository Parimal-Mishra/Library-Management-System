from Book import Book
from User import User


class Admin:
    def __init__(self):
        self.books = {}  # book_id -> Book
        self.users = {}  # user_id -> User

    def add_book(self, book_id, book_name, book_quantity):
        if book_id in self.books:
            print("This book ID already exists.")
            return

        new_book = Book(book_id, book_name, book_quantity)
        self.books[book_id] = new_book
        print("Book added successfully.")

    def print_all_books(self):
        if not self.books:
            return "There are no books in the library."

        lines = [f"{book.id}: {book.name} ({book.quantity} available)" for book in self.books.values()]
        return "\n".join(lines)

    def search_for_book(self, query):
        query_text = query.strip().lower()
        return [book for book in self.books.values() if book.name.lower().startswith(query_text)]

    def add_user(self, user_id, user_name):
        if user_id in self.users:
            print("This user ID already exists.")
            return

        new_user = User(user_id, user_name)
        self.users[user_id] = new_user
        print("User created successfully.")

    def find_user_by_name(self, user_name):
        normalized = user_name.strip().lower()
        for user in self.users.values():
            if user.name.lower() == normalized:
                return user
        return None

    def borrow_book(self, user_name, book_name):
        user = self.find_user_by_name(user_name)
        if not user:
            print("There is no user with this name.")
            return

        found_books = self.search_for_book(book_name)
        if not found_books:
            print("No book found with that name.")
            return

        book = found_books[0]
        if book.quantity <= 0:
            print("Insufficient quantity!")
            return

        book.quantity -= 1
        user.borrow_book(book.name)
        print(f"The user {user.name} borrowed {book.name}.")

    def return_book(self, user_name, book_name):
        user = self.find_user_by_name(user_name)
        if not user:
            print("There is no user with this name.")
            return

        found_books = self.search_for_book(book_name)
        if not found_books:
            print("There is no book with that name.")
            return

        book = found_books[0]
        if not user.return_book(book.name):
            print(f"{user.name} did not borrow {book.name}.")
            return

        book.quantity += 1
        print(f"The user {user.name} returned {book.name}.")

    def print_users_borrowed(self):
        borrowed_users = [user for user in self.users.values() if user.borrowed_books]
        if not borrowed_users:
            print("There are no users who have borrowed books.")
            return

        for user in borrowed_users:
            borrowed_list = ", ".join(user.borrowed_books)
            print(f"The user {user.name} borrowed: {borrowed_list}")

    def print_all_users(self):
        if not self.users:
            print("There are no users in the system.")
            return

        for user in self.users.values():
            print(f"{user.id}: {user.name}")
