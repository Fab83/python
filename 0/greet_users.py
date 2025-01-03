def greet_users(names):
	"""Imprimer bienvenue a chaque utilisateur"""
	for name in names:
		msg=f"Hello, {name.title()} !"
		print(msg)
		
usernames=['pierre', 'paul','jacques', 'martine']
greet_users(usernames)