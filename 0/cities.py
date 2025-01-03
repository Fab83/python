prompt="\nEntrez le nom d'une ville que vous avez visitée : "
prompt += "\nTapez 'quit' quand vous avez fini. \n"

while True:
	city=input(prompt)
	
	if city == 'quit':
		break
	else:
		print(f"J'aimerais bien aller à {city.title()}")