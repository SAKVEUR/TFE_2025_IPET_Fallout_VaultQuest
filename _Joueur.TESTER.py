"""
QUI: Thibaud Masset & Sacha Fierin
QUAND: 09/05/25
QUOI: Test de création des joueurs, nommage et choix des héros
"""

from Partie import Partie

# Créer une partie
partie = Partie()

# Initialiser le matériel (inclut la création des héros)
partie.InitialiserMateriel()

# Créer les joueurs
print("\n=== Création des joueurs ===")
partie.creerJoueurs()

# Afficher les résultats
print("\n=== Résultats ===")
for i, joueur in enumerate(partie.joueurs, 1):
    print(f"\nJoueur {i}:")
    print(f"Nom: {joueur.nomJoueur}")
    print(f"Est maître du jeu: {joueur.est_maitreDuJeu}")
    if hasattr(joueur, 'personnage'):
        print(f"Héros choisi: {joueur.personnage.nomPerso}")
        print(f"Points de vie: {joueur.personnage.points_vie_Perso}")
        print(f"Arme: {joueur.personnage.persoArme.nomArme} (Dégâts: {joueur.personnage.persoArme.pointsDegatsArme})")
        print(f"Armure: {joueur.personnage.persoArmure.nomArmure} (Protection: {joueur.personnage.persoArmure.pointsProtectionArmure})")

print(f"\n {partie.joueurs}")

while True:
    partie.jouerTour()
    partie.afficher_plateau()
