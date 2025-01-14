from user import User

from admin import Admin, Privileges

new_admin = Admin("bob", "leponge", 18, "fréjus")

new_admin_p = ["can edit"]
new_admin.privileges.privileges = new_admin_p
new_admin.privileges.show_privileges()
