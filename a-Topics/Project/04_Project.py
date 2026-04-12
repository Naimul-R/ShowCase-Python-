class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        self.borrower = None

    def __str__(self):
        status = f"Borrowed by {self.borrower}" if not self.available else "Available"
        return f"{self.title} by {self.author} | {status}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    # ---------- core operations ----------

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added {book.title}.")

    def borrow(self, title, borrower_name):
        book = self._find_book(title)
        if not book:
            print(f"Not found {title}!")
            return 
        if not book.available:
            print(f'"{title}" is already borrowed by {book.borrower}.')
            return 
        book.available = False
        book.borrower = borrower_name
        print(f'"{title}" borrowed by {borrower_name}.')

    def return_book(self, title):
        book = self._find_book(title)
        if not book:
            print(f' Not Found "{title}"')
            return 
        if book.available:
            print(f'"{title}" was not borrowed')
            return 
        book.available = True
        book.borrower = None
        print(f'"{title}" return successfully.')
