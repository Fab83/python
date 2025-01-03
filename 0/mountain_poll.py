responses={}
# flag active
polling_active=True

while polling_active:
	name=input('Votre nom : ')
	response=input('Quelle montagne voulez-vous gravir ? ')
	
	# enregistrer réponses
	responses[name]=response

	repeat=input("Une autre personne va répondre (o/n) ? ")
	if repeat=="n":
		polling_active=False
		
# voir résultats
print("\n----Résultats----")
for name, response in responses.items():
	print(f"{name.title()} aimerait gravir {response.title()}")