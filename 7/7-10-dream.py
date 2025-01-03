vacations={}

active=True
while active:
	vacations['name']=input("Votre nom ? ")
	vacations['destination']=input("Où voulez-vous partir en vacances ? ")
	prompt=input('Un autre souhait ? (o/n) ')
	if prompt == 'n':
		active=False
		
print(vacations)