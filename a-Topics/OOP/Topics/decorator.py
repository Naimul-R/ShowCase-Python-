# Decorator --> A decorator is a function that wraps another function to add extra behavior — without changing the original function's code.
def greet(fx):
    def mfx(*arg, **kwargs):
        print("Good Morning.")
        fx(*arg, **kwargs)
        print("Thank you for using this function.")
    return mfx
    
@greet
def hello():
    print("Hello World")

@greet
def add(a, b):
    print(a+b)

hello()
add(5, 7)
