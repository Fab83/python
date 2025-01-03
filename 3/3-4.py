guests=['Paul', 'jean','aline', 'stéphane','nathalie','aude']
for guest in guests:
    print(f"Salut {guest.title()}, tu viens diner samedi ?")
print(f"----ZUT ! {guests[3].title()} ne pourra pas venir----")
guests.insert(3, 'bernard')
for guest in guests:
    print(f"Salut {guest.title()}, tu viens diner samedi ?")