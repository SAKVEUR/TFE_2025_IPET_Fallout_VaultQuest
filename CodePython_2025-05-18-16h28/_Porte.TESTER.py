"""
QUI: Sacha Fierin
QUAND: 14/05/25
QUOI: Test de la classe Porte
"""

from Partie import Partie
from Personnage import Personnage
from Porte import Porte
from Plateau import Plateau


# Créer une partie
partie = Partie()
    
# Créer un plateau de test
plateau = Plateau(1, 5, 5)
    
# Créer une porte de test
porte1 = Porte(1, "%", 2, 2)
porte2 = Porte(2, "%", 2, 3)
    
# Créer un personnage de test
personnage = Personnage("Test", 100, None, None, 2, 1, 0, "A")  # Position adjacente à la porte
    
# Placer la porte sur le plateau
plateau.plateau[2][2] = porte1.symbole
plateau.plateau[2][3] = porte2.symbole
plateau.plateau[2][1] = personnage.iconePersonnage
    
# Afficher le plateau initial
print("\nPlateau initial :")
plateau.afficher_plateau()
    
# Tester l'ouverture de la porte
print("\nTest d'ouverture de la porte :")
porte1.ouvrirPorte()
plateau.plateau[2][2] = porte1.symbole  # Mettre à jour le symbole sur le plateau
    
# Afficher le plateau après ouverture
print("\nPlateau après ouverture :")
plateau.afficher_plateau()

