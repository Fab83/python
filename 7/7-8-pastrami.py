sandwich_orders=['jambon', 'pastrami', 'saucisson', 'pastrami', 'américain', 'pastrami', 'fromage', 'curry']
finished_sandwich=[]

print("\nIl n'y a plus de pastrami, désolé")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:
	print(f"J'ai préparé ton {sandwich.title()} avec amour ! ")
	finished_sandwich.append(sandwich)
	
print(f"J'ai fait {finished_sandwich}")