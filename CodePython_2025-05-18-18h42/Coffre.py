"""
QUI: Mathis Binnemans
QUAND: 19/03/25
QUOI: Fichier classe "Coffre"
"""

##################################
### Constructeur / Destructeur ###
##################################
class Coffre():
    def __init__(self, para_idPorte: int, para_contenuCoffre:str = "Bombe", para_symbole:str = "X", para_positionX:int = 0, para_positionY:int = 0, para_idQuete:int = 0):

        self.__idPorte = para_idPorte
        self.__contenuCoffre = para_contenuCoffre
        self.__symbole = para_symbole
        self.__positionX = para_positionX
        self.__positionY = para_positionY
        self.__idQuete = para_idQuete
    #####################
    ###    Getters    ###
    #####################

    ### Id de la porte
    @property
    def idPorte(self) -> int:
        return self.__idPorte

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

    ### Id de la quete
    @property
    def idQuete(self) -> int:
        return self.__idQuete

    #####################
    ###    Setters    ###
    #####################  

    ### Symbole du coffre
    @symbole.setter
    def symbole(self, para_symbole:str):
        self.__symbole = para_symbole

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



    """
    QUI: Sacha Fierin
    QUAND: 19/03/25
    QUOI: Méthode __str__()
    Permet d'afficher le symbole du coffre
    """
    def __str__(self):
        return self.symbole
