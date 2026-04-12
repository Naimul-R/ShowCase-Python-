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

    # ---------- search & info ----------

    def search_by_author(self, author):
        results = [b for b in self.books if b.author.lower() == author.lower()]
        if not results:
            print(f'No book found by Author "{author}"')
            return 
        print(f'Book by "{author}"')
        for b in results:
            print(f'    {b}')

    def count_available(self):
        return sum(1 for b in self.books if b.available)
    
    def show_all(self):
        print(f'\n  {self.name} — All Books ({len(self.books)} total):')
        print('  ' + '-' * 40)
        for b in self.books:
            print(f'    {b}')
        print(f'  Available: {self.count_available()} / {len(self.books)}')

    # ---------- private helper ----------

    def _find_book(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                return b 
        return None
    
lib = Library("Bangladesh International Library.")

# Add books
print("\n[ Adding Books ]")
lib.add_book(Book("The Alchemist",         "Paulo Coelho"))
lib.add_book(Book("Atomic Habits",         "James Clear"))
lib.add_book(Book("Clean Code",            "Robert Martin"))
lib.add_book(Book("Thinking Fast and Slow","Daniel Kahneman"))

# --- show all books ---
lib.show_all()

# --- borrow books ---
print("\n[ Borrowing Books ]")
lib.borrow("Atomic Habits",  "Rahim")
lib.borrow("Clean Code",     "Karim")

# --- return a book ---
print("\n[ Returning Books ]")
lib.return_book("Clean Code")
lib.return_book("Clean Code") # already returned

# --- search by author ---
print("\n[ Search by Author ]")
lib.search_by_author("Paulo Coelho")
lib.search_by_author("J.K. Rowling")    # not found — should fail

# --- final status ---
lib.show_all()