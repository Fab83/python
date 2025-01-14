# from car import Car, ElectricCar
# from car import * -> pas recommandé
import car

my_mustang = car.Car('ford', 'mustang', 1967)
print(my_mustang.get_descriptive_name())

my_leaf = car.ElectricCar('nissan', 'leaf', 2023)
print(my_leaf.get_descriptive_name())
