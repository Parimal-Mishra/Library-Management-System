class User:
    def __init__(self, id, name):
        self.id = int(id)
        self.name = str(name).strip()
        self.borrowed_books = []

    def borrow_book(self, book_name):
        self.borrowed_books.append(book_name)

    def return_book(self, book_name):
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            return True
        return False

    def __str__(self):
        return f"{self.id}: {self.name}"
