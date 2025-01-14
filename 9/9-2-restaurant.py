class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Le restaurant s'appelle {self.restaurant_name} et ils y font de la cuisine {self.cuisine_type}")

    def open_restaurant(self):
        print("Le restaurant est ouvert.")


my_restaurant = Restaurant("El Muchacho", "Mexicaine")
my_second_restaurant = Restaurant("Les voiles", "Poisson")
my_third_restaurant = Restaurant("La bonne côte", "Viandes")

my_restaurant.describe_restaurant()
my_second_restaurant.describe_restaurant()
my_third_restaurant.describe_restaurant()
