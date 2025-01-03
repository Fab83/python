def print_models(unprinted_models, completed_models):
    """
    Simule l'impression de chaque moedl, jusqu'au dernier
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model : {current_design.title()}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """montre tous les modèles imprimés"""
    print("\nLes modèles suivants ont été imprimés:")
    for completed_model in completed_models:
        print(completed_model.title())


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
