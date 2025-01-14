class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Le restaurant s'appelle {self.restaurant_name} et ils y font de la cuisine {self.cuisine_type}")

    def open_restaurant(self):
        print("Le restaurant est ouvert.")


my_restaurant = Restaurant("El Muchacho", "Mexicaine")
print(f"{my_restaurant.restaurant_name}")
print(f"{my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
