prompt = "\nQuel est votre age : "
prompt += "\nTapez '0' pour sortir ! "

while True:
	age=int(input(prompt))
	if age == 0:
		break
	elif age < 3:
		print("C'est gratuit !")
	elif 3 <= age <= 12:
		print("Le ticket coûte $10")
	else:
		print("Le ticket coûte $15")