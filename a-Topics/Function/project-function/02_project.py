# Create function for add items
def add_items():
    items = []
    total_item = int(input("How many items? : "))

    for i in range(1, total_item + 1):
        name = input(f"Enter item {i} name : ")
        price = int(input(f"Enter item {i} price : "))
        items.append({"name": name, "price": price})

    return items

# Create function to show shopping cart with items 
def show_cart(items):
    print("\n--- Your Shopping Cart ---")

    for i, item in enumerate(items, 1):
        print(f" {i}. {item['name']:<15} - price: {item['price']}")

    print("--------------------------")

# Create function to get total item 
def get_total(items):
    total = 0 
    
    for item in items:
        total += item['price']
    return total

# Create a function for discount apply 
def apply_discount(total):
    if total > 1000:
        discount = total * 10 / 100
        label = "10%"
    elif total > 500:
        discount = total * 5 / 100
        label = "5%"
    else: 
        discount = 0
        label = "No"

    final = total - discount
    return final, discount, label

# create a function for Most expensive item function
def most_expensive(items):
    expensive = items[0]
    
    for item in items:
        if item['price'] > expensive['price']:
            expensive = item 
    return expensive

# ---------- MAIN REPORT FUNCTION ----------
def full_cart_report():
    print("\n============================================")
    print("        🛒  SHOPPING CART SYSTEM  🛒       ")
    print("============================================")

    # Step 1 — collect items
    items = add_items()

    # Step 2 — show cart
    show_cart(items)

    # Step 3 — calculate total
    total = get_total(items)

    # Step 4 — apply discount
    final, discount, label = apply_discount(total)

    # Step 5 — most expensive item
    expensive = most_expensive(items)

    # Step 6 — print final report
    print(f"\n  Total Bill    : {total}")
    print(f"  Discount      : {label} → -{discount}")
    print(f"  Final Bill    : {final}")
    print(f"\n  💸 Most Expensive : {expensive['name']} - Price: {expensive['price']}")
    print("\n============================================")


# --- Run the program ---
full_cart_report()