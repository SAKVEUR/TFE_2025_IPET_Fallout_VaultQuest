"""
QUI: Mathis Binemans
QUAND: 27/03/25
QUOI: TESTER de Quete
"""

from Quete import Quete
from Partie import Partie

try:

    # Création de l'objet Quete
    objet1 = Partie()

    # Afficher la quête sélectionnée
    objet1.demarrer()

except ValueError as erreur:
    print(f"Erreur : {erreur}")

objet1.jouerTourHeros()
