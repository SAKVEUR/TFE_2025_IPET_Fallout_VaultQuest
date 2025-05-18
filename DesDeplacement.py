"""
QUI: Thibaud Masset
QUAND: 19/03/25 8h45
QUOI: Classe DesDeplacement
"""

####################
###    Import    ###
####################
from random import *

##################################
### Constructeur / Destructeur ###
##################################
class DesDeplacement():
    
    def __init__(self, para_nombreFaceDesDeplacement:int=6):

       self.__nombreFaceDesDeplacement:int = 6

       self.nombreFaceDesDeplacement = para_nombreFaceDesDeplacement

    #####################
    ###    Getters    ###
    #####################
               
    ### Nombre de face de déplacement
    @property
    def para_nombreFaceDesDeplacement(self) -> int:
        return self.__nombreFaceDesDeplacement

    ################################
    ###         Méthodes         ###
    ################################

    """
    QUI: Thibaud Masset
    QUAND: 18/04/25
    QUOI: Méthode lancer()
    Lance le dé et retourne un nombre aléatoire entre 1 et le nombre de faces
    """
    def lancer(self) -> int:
        return randint(1, self.nombreFaceDesDeplacement)
