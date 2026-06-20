from Admin import Admin
from utility import input_is_valid


class OperationsManager:
    def __init__(self):
        self.admin = Admin()

    def print_menu(self):
        print("\nLibrary Menu:")
        options = [
            '1) Add Book',
            '2) Print Library Books',
            '3) Search Books by Prefix',
            '4) Add User',
            '5) Borrow Book',
            '6) Return Book',
            '7) Print Users Who Borrowed Books',
            '8) Print Users',
            '9) Exit'
        ]
        print('\n'.join(options))
        return self.get_choice(len(options))

    def get_choice(self, num_options):
        msg = f"Enter choice (1-{num_options}): "
        return input_is_valid(msg, 1, num_options)

    def add_book(self):
        book_id = input('Enter book ID: ').strip()
        book_name = input('Enter book name: ').strip()
        book_quantity = input('Enter book quantity: ').strip()
        self.admin.add_book(book_id, book_name, book_quantity)

    def print_books(self):
        print(self.admin.print_all_books())

    def search_books(self):
        query = input('Enter book name prefix: ')
        found_books = self.admin.search_for_book(query)
        if not found_books:
            print('No books found matching that prefix.')
            return
        for book in found_books:
            print(book)

    def add_user(self):
        user_id = input('Enter user ID: ').strip()
        user_name = input('Enter user name: ').strip()
        self.admin.add_user(user_id, user_name)

    def borrow_book(self):
        user_name = input('Enter user name: ')
        book_name = input('Enter book name: ')
        self.admin.borrow_book(user_name, book_name)

    def return_book(self):
        user_name = input('Enter user name: ')
        book_name = input('Enter book name: ')
        self.admin.return_book(user_name, book_name)

    def print_users_borrowed(self):
        self.admin.print_users_borrowed()

    def print_all_users(self):
        self.admin.print_all_users()

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.print_books()
            elif choice == 3:
                self.search_books()
            elif choice == 4:
                self.add_user()
            elif choice == 5:
                self.borrow_book()
            elif choice == 6:
                self.return_book()
            elif choice == 7:
                self.print_users_borrowed()
            elif choice == 8:
                self.print_all_users()
            elif choice == 9:
                print("Exiting program. Goodbye.")
                break
