"""
QUI: Sacha Fierin
QUAND: 27/03/25
QUOI: TESTER de Partie
"""

from Plateau import Plateau
from Personnage import Personnage
from Partie import Partie
from Arme import Arme
from Armure import Armure
from Porte import Porte
from Heros import Heros
from Monstre import Monstre
from Coffre import Coffre
# Créer une partie et un plateau 5x5
partie = Partie()
plateau = Plateau(1, 5, 5)
partie.plateauActuel = plateau
partie.titreDuJeu()
partie.InitialiserMateriel()

# Créer une arme et une armure pour le personnage
arme_test = Arme("Épée de test", 5)
armure_test = Armure("Armure de test", 3)

# Créer un personnage au centre du plateau (2,2)
personnage = Heros("H", 10, arme_test, armure_test, 2, 2, 0, "A")

monstre = Monstre("M", 10, arme_test, armure_test, 1, 2, 5, "1")

porte1 = Porte(1, "%", 2, 3)

coffre = Coffre("Bombe", "X", 3, 2)

# Placer les éléments autour du personnage
plateau.plateau[1][2] = "M"  # Mur en haut
plateau.plateau[2][3] = porte1.symbole  # Porte à droite
plateau.plateau[2][1] = monstre.iconePersonnage  # Monstre à gauche
plateau.plateau[3][2] = coffre.symbole

# Placer le personnage au centre
plateau.plateau[2][2] = personnage.iconePersonnage

print("\n=== Test du plateau initial ===")
plateau.afficher_plateau()

print("\n=== Test de la vérification des cases adjacentes ===")
partie.verifierCasesAdjacente(personnage)

print("\n=== État du plateau après vérification des cases adjacentes ===")
plateau.afficher_plateau()
