"""
QUI: Mathis Binnemans
QUAND: 19/03/25
QUOI: Fichier classe "Coffre"
"""

##################################
### Constructeur / Destructeur ###
##################################
class Coffre():
    def __init__(self, para_contenuCoffre:str = "Bombe", para_symbole:str = "X", para_positionX:int = 0, para_positionY:int = 0):

        self.__contenuCoffre = para_contenuCoffre
        self.__symbole = para_symbole
        self.__positionX = para_positionX
        self.__positionY = para_positionY

    #####################
    ###    Getters    ###
    #####################

    ### Contenu du coffre
    @property
    def contenuCoffre(self) -> str:
        return self.__contenuCoffre

    ### Id du coffre
    @property
    def symbole(self) -> str:
        return self.__symbole

    ### Position X du coffre
    @property
    def positionX(self) -> int:
        return self.__positionX

    ### Position Y du coffre
    @property
    def positionY(self) -> int:
        return self.__positionY
        

    #####################
    ###    Setters    ###
    #####################

    ### Contenu du coffre
    @contenuCoffre.setter
    def contenuCoffre(self, para_contenuCoffre:str):    
        self.__contenuCoffre = para_contenuCoffre

    ################################
    ###         Méthodes         ###
    ################################

    """
    QUI: Sacha Fierin
    QUAND: 19/03/25
    QUOI: Méthode devoilerContenu()
    Permet d'afficher/dévoiler le contenu du coffre
    """
    def devoilerContenu(self):
        return f"Le coffre contient l'objet {self.contenuCoffre} !"