class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"Title: {book.title}, Author: {book.author}")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"You have checked out '{book.title}'.")
                    return True
                else:
                    print(f"'{book.title}' is already checked out.")
                    return False
        print(f"Sorry, '{title}' does not exist in the library.")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"You have returned '{book.title}'.")
                    return True
                else:
                    print(f"'{book.title}' was not checked out.")
                    return False
        print(f"Sorry, '{title}' does not exist in the library.")
        return False
