def get_formatted_name(first_name, last_name):
	"""retourne nom complet, formatté"""
	full_name=f"{first_name} {last_name}"
	return full_name.title()

while True:
	print("\nVotre nom : ")
	print("\n(Entrez 'q' pour quitter)")
	f_name=input("Prénom : ")
	if f_name=='q':
		break
	l_name=input("Nom : ")
	if l_name=='q':
		break
	
	formatted_name=get_formatted_name(f_name, l_name)
	print(f"\nSalut, {formatted_name}")