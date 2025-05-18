"""
QUI: Mathis Binnemans et Sacha Fierin
QUAND: 26/03/25
QUOI: Classe MaitreDuJeu
"""

####################
###    Import    ###
####################
from Joueur import Joueur
from Monstre import Monstre

##################################
### Constructeur / Destructeur ###
##################################
class MaitreDuJeu(Joueur):
    def __init__(self, para_nomJoueur:str, para_ordreJoueur: int = 1, para_monstres: list = []):
        if monstres is None:
            monstres = []
        super().__init__(para_nomJoueur, para_ordreJoueur, est_maitre_du_jeu=True)
        self.__monstres = para_monstres
        self.__tourMonstre = 0

    #####################
    ###    Getters    ###
    #####################

    ### GET Ordre de passage des monstres
    @property
    def positionTour(self) -> int:
        return self.positionTour