"""
QUI: Mathis Binnemans
QUAND: 19/03/25
QUOI: Classe Heros
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
class Heros(Personnage):
    def __init__(self, para_nomHero:str = "nom", para_points_vie_hero:int = 1, para_hero_arme:Arme = None, para_hero_armure:Armure = None, para_positionX:int = 0, para_positionY:int = 0, para_nombreDeplacement:int = 0, para_iconePersonnage:str = "A"):
       super().__init__(para_nomHero, para_points_vie_hero, para_hero_arme, para_hero_armure, para_positionX, para_positionY, para_nombreDeplacement, para_iconePersonnage)  
