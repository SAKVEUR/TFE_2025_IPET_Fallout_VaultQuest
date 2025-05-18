"""
QUI: Sacha Fierin
QUAND: 07/05/25
QUOI: TESTER de Plateau
"""

from Personnage import Personnage
from Plateau import Plateau
from Arme import Arme
from Armure import Armure
from Partie import Partie
from Heros import Heros
from Monstre import Monstre

### Création des objets de base
arme1 = Arme("Épée test 1", 5)
armure1 = Armure("Armure test 1", 3)
heros1 = Heros("personnage test1", 10, arme1, armure1, 3, 2, 0,"A")
monstre1 = Monstre("personnage test2", 10, arme1, armure1, 5, 3, 0,"1")


### Créer un plateau (niveau 1, 5 lignes, 8 colonnes)
plateau = Plateau(4, 8, 12)
partie = Partie()
partie.plateauActuel = plateau

### Placer les personnages sur le plateau
plateau.plateau[heros1.positionY][heros1.positionX] = str(heros1)
plateau.plateau[monstre1.positionY][monstre1.positionX] = str(monstre1)

### Affichage état initial
plateau.afficher_plateau()

### Test des déplacements
continuer = True
while continuer:
    heros1.seDeplacer(plateau)
    plateau.afficher_plateau()
    continuer = heros1.nombreDeDeplacement > 0
