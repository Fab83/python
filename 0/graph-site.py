from graphviz import Digraph

# Create a new directed graph
dot = Digraph(format='png')

# Define nodes and structure
dot.node('A', 'Habitat / Logement')

# First branch - Offre de Logement
dot.node('B1', 'Offre de Logement')
dot.edge('A', 'B1')

# Sub-branches under Offre de Logement
dot.node('C1', 'Location Sociale')
dot.node('C2', 'Accession à la Propriété')
dot.edge('B1', 'C1')
dot.edge('B1', 'C2')

# Location Sociale Details
dot.node('D1', 'Logements Disponibles')
dot.node('D2', 'Conditions d\'Éligibilité')
dot.node('D3', 'Demande de Logement Social')
dot.edge('C1', 'D1')
dot.edge('C1', 'D2')
dot.edge('C1', 'D3')

# Accession à la Propriété Details
dot.node('D4', 'Programmes Disponibles')
dot.node('D5', 'Critères d\'Accession')
dot.node('D6', 'Simulateur de Financement')
dot.edge('C2', 'D4')
dot.edge('C2', 'D5')
dot.edge('C2', 'D6')

# Conseil Personnalisé
dot.node('B2', 'Conseil Personnalisé')
dot.edge('A', 'B2')
dot.node('C3', 'Chatbot d\'Assistance')
dot.node('C4', 'Rendez-vous avec un Conseiller')
dot.node('C5', 'Guide pour Acteurs Immobiliers')
dot.edge('B2', 'C3')
dot.edge('B2', 'C4')
dot.edge('B2', 'C5')

# Rénovation Énergétique
dot.node('B3', 'Rénovation Énergétique')
dot.edge('A', 'B3')
dot.node('C6', 'Aides Financières')
dot.node('C7', 'Espace Conseil France Rénov\'')
dot.node('C8', 'Exemples de Projets Réalisés')
dot.edge('B3', 'C6')
dot.edge('B3', 'C7')
dot.edge('B3', 'C8')

# Aides et Financements
dot.node('B4', 'Aides et Financements')
dot.edge('A', 'B4')
dot.node('C9', 'Aides Locales')
dot.node('C10', 'Aides Nationales')
dot.node('C11', 'Subventions Européennes')
dot.node('C12', 'Simulateur d\'Aides')
dot.edge('B4', 'C9')
dot.edge('B4', 'C10')
dot.edge('B4', 'C11')
dot.edge('B4', 'C12')

# Développement des ENR
dot.node('B5', 'Développement des ENR')
dot.edge('A', 'B5')
dot.node('C13', 'Conseils et Accompagnement')
dot.node('C14', 'Projets et Installations en Cours')
dot.node('C15', 'Partenariats Locaux')
dot.node('C16', 'Aides à l\'Installation')
dot.edge('B5', 'C13')
dot.edge('B5', 'C14')
dot.edge('B5', 'C15')
dot.edge('B5', 'C16')

# Render the diagram to a file
# diagram_path = '/mnt/data/habitat_logement_sitemap'
diagram_path = 'c:/Users/FabriceVITEAU/Desktop/python'
dot.render(diagram_path)

diagram_path_with_extension = diagram_path + '.png'
diagram_path_with_extension
