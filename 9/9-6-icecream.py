# Page 211
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Le restaurant s'appelle {self.restaurant_name} et ils y font de la cuisine {self.cuisine_type}")

    def open_restaurant(self):
        print("Le restaurant est ouvert.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="ice creams"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


big_one = IceCreamStand("The Big One")
big_one.flavors = ['vanille', 'chocolat', 'fraise']
big_one.describe_restaurant()
big_one.show_flavors()
