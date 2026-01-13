#Define the menu of Coffee
Menu = {
    "Espresso": 160,
    "Cappuccino": 250,
    "Latte": 280,
    "Americano": 155,
    "Mocha": 300,
    "Macchiato": 220,
    "Flat white": 280,
    "Cold Brew": 300,
    "Affogato": 350,
    "Caramel Latte": 280,
}

#Greet with the customer 
print("Welcome to our Coffee-Canvas")

print("Espresso: BDT160\nCappuccino: BDT250\nLatte: BDT260\nAmericano: BDT155\nMocha: BDT300\nMacchiato: BDT220\nFlat White: BDT280\nCold Brew: BDT300\nAffogato: BDT350\nCaramel Latte: BDt280 ")

order_total = 0

item_1 = input("Enter the name of item you want to order: ")
if item_1 in Menu:
    order_total += Menu[item_1]
    print(f"Your item {item_1} has been added to your order ")
else:
    print(f"Your Ordered {item_1} is not available yet")