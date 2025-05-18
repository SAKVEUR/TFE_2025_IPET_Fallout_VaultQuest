"""
QUI: Mathis Binnemans
QUAND: 17/03/25
QUOI: Fichier classe "Arme"
"""

##################################
### Constructeur / Destructeur ###
##################################
class Arme():
    def __init__(self, para_nomArme:str = "Arme", para_pointsDegatsArme:int= 1):
       self.nomArme = para_nomArme
       self.pointsDegatsArme = para_pointsDegatsArme
               
    #####################
    ###    Getters    ###
    #####################

    ### Nom de l'arme
    @property
    def para_nomArme(self) -> str:
        return self.__nomArme

    ### Point de dégat de l'arme
    @property
    def para_pointsDegatsArme(self) -> int:
        return self.__pointsDegatsArme

