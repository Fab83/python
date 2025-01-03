guests=['Paul', 'jean','aline', 'stéphane','nathalie','aude']

guests.insert(0, 'nadia')
guests.insert(4, 'antoine')
guests.append('simba')
min_guests=guests.lowercase()
print(sorted(min_guests))

print("Désolé, mais la table a brulé. Ce sera intime!")

while len(guests) > 2:
    print(f"Désolé {guests[-1].title()}, nous devons reporter")
    guests.pop()
print(f"Les invités restants sont {guests}")
del guests[:]
print(guests)