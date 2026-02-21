"""
🏬 Exercise 09 — Warehouse Stock Management
Requirements

1- Ask how many categories.
2- For each category:
    -Ask how many products.
    -Enter stock quantity for each product.
    -Calculate total stock for that category.

3- After all categories:
    -Print total warehouse stock.
    -Print which category has the highest stock.
    -Print that stock amount.
    -If any category total stock < 50 → print "Low stock warning".
"""
category = int(input("Enter the number of categories: "))

total_warehouse_stock = 0
highest_stock = 0
highest_category = 0

for i in range(1, category + 1):
    print(f"\nCategory {i}: ")

    products = int(input("Enter the number of products: "))
    category_total = 0

    for j in range(1, products + 1):
        stock_quantity = int(input(f"Enter stock quantity for each product {j}: "))
        category_total += stock_quantity

    print("Total stock for category", i, "=", category_total)

    # Add to warehouse total
    total_warehouse_stock += category_total

    # check highest stock category 
    if category_total > highest_stock:
        highest_stock = category_total
        highest_category = i

    # Low stock warning 
    if category_total < 50:
        print("Low stock warning for category", i)

print("\nTotal warehouse stock = ",total_warehouse_stock)
print("Category with highest stock = ",highest_category)
print("Highest stock amount = ",highest_stock)