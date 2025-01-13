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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Vous ne pouvez pas enlever des kilomètres")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
