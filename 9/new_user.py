from user_class import User, Admin, Privileges

new_admin = Admin("fabrice", "viteau", 54, "agay"

new_admin_privileges = ["can edit", "can delete"]
new_admin.privileges.privileges = new_admin_privileges
new_admin.describe_user()
new_admin.privileges.show_privileges()
