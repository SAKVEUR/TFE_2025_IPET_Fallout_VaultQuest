"""
QUI: Mathis Binnemans
QUAND: 17/03/25
QUOI: Fichier classe "Armure"
"""

##################################
### Constructeur / Destructeur ###
##################################
class Armure():
    def __init__(self, para_nomArmure:str = "Armure", para_pointsProtectionArmure:int = 1):
       self.nomArmure = para_nomArmure
       self.pointsProtectionArmure = para_pointsProtectionArmure

    #####################
    ###    Getters    ###
    #####################
   
    ### Nom de l'armure
    @property
    def para_nomArmure(self) -> str:
        return self.__nomArmure

    ### Point de protection de l'armure
    @property
    def para_pointsProtectionArmure(self) -> str:
        return self.__pointsProtectionArmure
