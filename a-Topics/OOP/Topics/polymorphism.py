# Polymorphism means one thing, many forms. The same method name behaves differently depending on which class is calling it.

class CreditCard:
    def pay(self, amount):
        print(f"paid ${amount} via credit card.")

class PayPal:
    # using same function/parameter name called polymorphism 
    def pay(self, amount):
        print(f"Paid ${amount} via PayPal.")

class Crypto:
    def pay(self, amount):
        print(f"Paid ${amount} via Bitcoin.")

payment = CreditCard()
payment.pay(100)

payment = PayPal()
payment.pay(200)

payment = Crypto()
payment.pay(500)

print("===== Another Example =====")
class library:
    def BookName(self):
        print(f"Think and Grow RIch.")
    
class BookSelf(library):
    def BookName(self):
        super().BookName()
        print('Mindset.')

obj = BookSelf()
obj.BookName()