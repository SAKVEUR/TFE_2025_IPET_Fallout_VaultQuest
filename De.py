"""
QUI: Thibaud Masset
QUAND: 21/03/25 8h45
QUOI: Classe DesCombat
"""

####################
###    Import    ###
####################
from random import *

##################################
### Constructeur / Destructeur ###
##################################
class De():
    
    def __init__(self, para_nombreFace:int=6):
       self.nombreFace = para_nombreFace

    #####################
    ###    Getters    ###
    #####################

    ### Nombre de face neutres
    @property
    def para_nombreFace(self) -> int:
        return self.__nombreFace
