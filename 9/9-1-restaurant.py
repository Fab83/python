class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(f"Le restaurant s'appelle {self.restaurant_name.title()} et ils y font de la cuisine {self.cuisine_type.title()}, et ont servi {self.number_served} couverts.")

    def open_restaurant(self):
        print("Le restaurant est ouvert.")

    def set_number_served(self, number):
        self.number_served+=number
    
    def increment_number_served(self, incremented=10):
        self.number_served+=incremented

my_restaurant = Restaurant("El Muchacho", "Mexicaine")
print(f"{my_restaurant.restaurant_name}")
print(f"{my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

second_restaurant=Restaurant("le shangai", "asiatique")
second_restaurant.number_served=20
second_restaurant.describe_restaurant()
second_restaurant.set_number_served(30)
second_restaurant.describe_restaurant()
second_restaurant.increment_number_served()
second_restaurant.describe_restaurant()
second_restaurant.increment_number_served(14)
second_restaurant.describe_restaurant()