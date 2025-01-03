guests=['Paul', 'jean','aline', 'stéphane','nathalie','aude']
for guest in guests:
    print(f"Salut {guest.title()}, tu viens diner samedi ?")
print(f"----ZUT ! {guests[3].title()} ne pourra pas venir----")
guests[3]='bernard'
for guest in guests:
    print(f"Salut {guest.title()}, tu viens diner samedi ?")

print('Nous avons une salle plus grande, nous accueillerons plus de monde')

guests.insert(0, 'nadia')
guests.insert(4, 'antoine')
guests.append('simba')
for guest in guests:
    print(f"Je te rappelle, mon cher {guest.title()}, que je t'attends pour diner samedi !")
print(f"Nombre invités : {len(guests)}")