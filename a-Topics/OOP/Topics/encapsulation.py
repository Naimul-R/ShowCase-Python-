# Definition: Encapsulation is the practice of bundling data (attributes) and methods (functions) together inside a class, while restricting direct access to some of the object's components. It hides internal details and exposes only what's necessary.

class Password_manager:
    def __init__(self):
        self.__password = {} # Encampsulate (privet)
        self.__master = "secret123" # also privet

    def save(self, site, password, master):
        if master == self.__master:
            self.password[site] = password
            print(f"Save password for {site}")
        else:
            print("Wrong master password!")