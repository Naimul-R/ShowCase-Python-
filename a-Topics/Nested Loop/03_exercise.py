"""
🏬 Task 8: Multi-Store Sales Analysis System
📝 Task Instructions:2

• Ask how many stores the company has
• For each store, ask how many products were sold
• For each product, ask the sale amount
• Calculate total sales for each store
• After all stores, print:
    .Total sales of each store
    .The store with the highest sales
"""
store = int(input("Enter the number of store compary have: "))

highest_sale = 0
best_store = 0

for i in range(1, store + 1):
    print(f"\nStores: {i}")

    product_sold = int(input("Enter the amount of product sold: "))
    total_sale = 0

    for j in range(1, product_sold + 1):
        sale_amount = float(input(f"Enter the sales amount for product {j}: "))
        total_sale += sale_amount

    print("Total sales for store", i, "=", total_sale)

    # Check highest sale
    if total_sale > highest_sale:
        highest_sale = total_sale
        best_store = i

print("\nBest performing store is", best_store)
print("Highest sales amount is = ", highest_sale)