"""
QUI: Sacha Fierin
QUAND: 27/03/25
QUOI: TESTER de Quete
"""

from Partie import Partie

partie = Partie()
partie.titreDuJeu()
partie.demarrer()

print(partie.heros_qui_joue)
print(partie.monstres_qui_joue)

partie.jouerTour()

