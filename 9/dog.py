class Dog:
    """Modele simple de chien"""

    def __init__(self, name, age):
        # fonction d'une class est une methode
        # __init__() method est lancée automatiquement à chaque instanciation
        """initialise attributs de nom et d'age"""
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} s'assoit maintenant")

    def roll_over(self):
        print(f"{self.name} fait la roulade")


my_dog = Dog('Simba', 3)
print(f"Mon chien s'appelle {my_dog.name} ")
print(f"Il a {my_dog.age} ans !")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Laika', 5)
print(f"\nTon chien s'appelle {your_dog.name} ")
print(f"Il a {your_dog.age} ans !")

your_dog.sit()
your_dog.roll_over()
