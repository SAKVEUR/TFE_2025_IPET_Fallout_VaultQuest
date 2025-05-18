"""
QUI: Mathis Binnemans et Sacha Fierin
QUAND: 26/03/25
QUOI: Classe Monstre
"""

####################
###    Import    ###
####################
from Arme import Arme
from Armure import Armure
from Personnage import Personnage

##################################
### Constructeur / Destructeur ###
##################################
class Monstre(Personnage):
    def __init__(self, para_nomMonstre:str = "nom", para_points_vie_monstre:int = 1, para_monstre_arme:Arme = None, para_monstre_armure:Armure = None, para_positionX:int = 0, para_positionY:int = 0, para_nombreDeplacement:int = 5, para_iconePersonnage:str = "1"):
        super().__init__(para_nomMonstre, para_points_vie_monstre, para_monstre_arme, para_monstre_armure, para_positionX, para_positionY, para_nombreDeplacement, para_iconePersonnage)

