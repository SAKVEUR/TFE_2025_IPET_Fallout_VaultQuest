from Personnage import Personnage
from Arme import Arme
from Armure import Armure
from Plateau import Plateau

# Création des objets nécessaires
arme = Arme("Épée", 10)
armure = Armure("Bouclier", 5)

# Création des personnages
hero = Personnage("Héros", 100, arme, armure, 0, 0)
ennemi = Personnage("Ennemi", 80, arme, armure, 1, 0)

# Création du plateau
plateau = Plateau(3, 3)
plateau.plateau[0][0] = hero
plateau.plateau[0][1] = ennemi.nomPerso

# Test des méthodes
print("Test de trouverEnnemisAPortee:")
ennemis = hero.trouverEnnemisAPortee(plateau, 3)
print(ennemis)

print("\nTest de lancerDesCombat:")
degats = hero.lancerDesCombat()


print("\nTest de lancerDesDefense:")
protection = hero.lancerDesDefense()


print("\nTest de calculerDegatsFinaux:")
degats_finaux = hero.calculerDegatsFinaux(degats, protection)


print("\nTest de appliquerDegats:")
hero.appliquerDegats(degats_finaux)


print("\nTest de seDefendre:")
defense = hero.seDefendre()
