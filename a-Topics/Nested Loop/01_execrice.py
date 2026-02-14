# Book Dictionary (Correct Structure)
books = {
    1: {"title": "Atomic Habits", "author": "James Clear"},
    2: {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson"},
    3: {"title": "Think and Grow Rich", "author": "Napoleon Hill"},
    4: {"title": "The 7 Habits of Highly Effective People", "author": "Stephen R. Covey"},
    5: {"title": "How to Win Friends and Influence People", "author": "Dale Carnegie"},
    6: {"title": "You Can Heal Your Life", "author": "Louise Hay"},
    7: {"title": "Man's Search for Meaning", "author": "Viktor E. Frankl"},
    8: {"title": "The Body Keeps the Score", "author": "Bessel van der Kolk"},
    9: {"title": "The Power of Your Subconscious Mind", "author": "Joseph Murphy"},
    10: {"title": "12 Rules for Life: An Antidote to Chaos", "author": "Jordan Peterson"}
}

# Show available books
print("Available Books:\n")
for key, value in books.items():
    print(f"{key}. {value['title']} - {value['author']}")

total_book_price = 0

# Ask how many different books user wants
book_count = int(input("\nHow many different books do you want to buy? "))

for i in range(book_count):
    print(f"\nBook Selection {i + 1}")
    
    num_book = int(input("Enter the book number: "))
    
    if num_book in books:
        price = int(input("Enter the price of this book: "))
        total_book_price += price   # ✅ Correct price addition
    else:
        print("Invalid book number!")

print("\nTotal price of books:", total_book_price)
