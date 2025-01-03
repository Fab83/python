prompt="\nDonnez un ingrédient à votre pizza : "
prompt+="\nTapez 'quit' pour sortir ! "

# v1
# while True:
# 	topping=input(prompt)
# 	if topping == 'quit':
# 		break
# 	else:
# 		print(f"J'ai ajouté {topping} à votre pizza !")
		
# v2
active=True
while active:
	topping=input(prompt)
	if topping == 'quit':
		active = False
	else:
		print(f"J'ai ajouté {topping} à votre pizza !")