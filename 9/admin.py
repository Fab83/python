from user import User


class Admin(User):
    def __init__(self, first_name, last_name, age, town):
        super().__init__(first_name, last_name, age, town)
        self.privileges = Privileges()  # ajout de la class Privileges


class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("L'utilisateur n'a aucun droit.")
