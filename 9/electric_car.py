import car


class Battery:
    """Une tentative simple pour modéliser une batterie pour une voiture électrique"""

    def __init__(self, battery_size=65):
        """Initialise les attributs de la batterie"""
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Cette voiture a une batterie de {self.battery_size}-kwh")

    def get_range(self):
        """indique les kms à disponibles avec la charge"""
        if self.battery_size == 40:
            range = 65
        elif self.battery_size == 65:
            range = 255
        else:
            range = "unknown"
        print(f"Cette voiture peut parcourir {range} kms avec une charge pleine.")


class ElectricCar(car.Car):
    """Utilise la classe Car mais avec des spécifications électriques"""

    def __init__(self, make, model, year):
        """initialise les attributs de la classe parent"""
        super().__init__(make, model, year)
        # super() : tells Python to call the __init__() method from Car
        self.battery = Battery()

    def fill_gas_tank(self):
        print("Cette voiture n'a pas de réservoir d'essence")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
