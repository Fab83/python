class Car:
    """Une tentative simple pour représenter une voiture"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Renvoie une description formatée"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"Cette voiture a {self.odometer_reading} kms au compteur.")

    def update_odometer(self, mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Vous ne pouvez pas enlever des kilomètres")

    def increment_odometer(self, miles):
        self.odometer_reading+=miles

class ElectricCar(Car):
    """Utilise la classe Car mais avec des spécifications électriques"""

    def __init__(self, make, model, year):
        """initialise les attributs de la classe parent"""
        super().__init__(make, model, year)
        # super() : tells Python to call the __init__() method from Car
        self.battery_size=40
    
    def describe_battery(self):
        print(f"Cette voiture a une batterie de {self.battery_size}-kwh")

my_leaf=ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()