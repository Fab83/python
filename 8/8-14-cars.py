def make_car(marque, modele, **options):
    car = {
        'Marque': marque.title(),
        'Modèle': modele.title()
    }
    for option, value in options.items():
        car[option] = value
    return car


car = make_car('Audi', 'Q3', couleur='bleu', sellerie='cuir')
print(car)
