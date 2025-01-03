
motos=['honda', 'yamaha', 'suzuki']
print(motos)
motos[0]='ducati'
print(motos)
motos.append('ktm')
print(motos)
popped_motos=motos.pop()
print(popped_motos)
motos.append('aprilia')
last_owned=motos.pop()
print(f"Ma dernière moto est une {last_owned.title()}")