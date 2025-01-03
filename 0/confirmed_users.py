unconfirmed_users=['alice', 'bruno', 'aline']
confirmed_users=[]

# vérifie chaque user jusqu'à ce qu'il y en ait plus
# chauqe user vérifié est envoyé dans l'autre liste
while unconfirmed_users: #tourne tant que non vide
	current_user=unconfirmed_users.pop()
	
	print(f"Vérifie user: {current_user.title()}")
	confirmed_users.append(current_user)
	
print("\nLes utilisateurs suivants ont été vérifiés : ")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())