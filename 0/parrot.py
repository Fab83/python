prompt = ("\nDis-moi quelque chose, et je le répéterai !")
prompt += ("\nEnter 'quit' pour finir le programme : ")

active=True

while active:
	message=input(prompt)
	
	if message == 'quit':
		active=False
	else:
		print(message)