# Create function for add items
def add_items():
    items = []
    total_item = int(input("How many items? : "))

    for i in range(1, total_item + 1):
        name = input(f"Enter item {i} name : ")
        price = int(input(f"Enter item {i} price : "))
        items.append({"name": name, "price": price})

    return items