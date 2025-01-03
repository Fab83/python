def make_pizza(size, *toppings):
    print(f"\nPizza {size} avec ces ingrédients : ")
    for topping in toppings:
        print(f"- {topping.title()}")


make_pizza('XL', 'champignons')
make_pizza('M', 'ail', 'aubergines', 'tomates')
