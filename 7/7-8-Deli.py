sandwich_orders=['jambon', 'saucisson', 'américain', 'fromage', 'curry']
finished_sandwich=[]

for sandwich in sandwich_orders:
	print(f"J'ai préparé ton {sandwich.title()} avec amour ! ")
	finished_sandwich.append(sandwich)
	
print(f"J'ai fait {finished_sandwich}")