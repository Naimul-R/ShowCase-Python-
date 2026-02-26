"""
🧾 Exercise 15 — Library Borrowing Management System
1️⃣ Show a menu repeatedly using a while loop:
"""
total_borrowed = 0
total_return = 0

max_book_borrowed = 0
top_member = ""

while True:
    print("\n---- Library Menu ----")
    print("1. Borrow Book")
    print("2. Return Book")
    print("3. View Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Borrowed Book
    if choice == "1":
        name = input("Enter Member Name: ")
        num_book = int(input("Enter the number of borrowed: "))

        total_borrowed += num_book

        for i in range(1, num_book + 1):
            book_title = input(f"Enter book title for book {i}: ")

        # Track member with most book
        if num_book > max_book_borrowed:
            max_book_borrowed = num_book
            top_member = name

        # Borrowing warning
        if num_book > 3:
            print(f"Borrowing limit warning for member {name}")

        print("Book borrowed successfully!")

    # Returned book
    elif choice == "2":
        return_book = int(input("Enter number of book you return: "))
        total_return += return_book
        print("Your returned book successful!")

    # === View Summary ===
    elif choice == "3":
        print("\n===== Book Summary =====")
        print("Total books borrowed = ", total_borrowed)
        print("Total books return = ", total_return)
        print("Book currently outsite = ", total_borrowed - total_return)

        if top_member:
            print("Member who borrowed most book = ", top_member)
            print("Maximum Book borrowed = ", max_book_borrowed)
        else:
            print("No borrowing record yet")

    # Exit
    elif choice == "4":
        print("Existing system...")
        break
    else:
        print("Invailed choice. Please enter the valid choice.")
