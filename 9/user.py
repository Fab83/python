class User:
    def __init__(self, first_name, last_name, age, town, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.town = town
        self.login_attempts = login_attempts

    def describe_user(self):
        print(
            f"Le nom d'utilisateur est {self.first_name.title()} {self.last_name.title()}, age : {self.age} ans et je viens de {self.town.title()} - Tentatives : {self.login_attempts}")

    def great_user(self):
        print(f"Salut {self.first_name.title()} {self.last_name}")

    def increment_login_attempts(self, increment=1):
        self.login_attempts += increment

    def reset_login_attempts(self):
        self.login_attempts = 0
