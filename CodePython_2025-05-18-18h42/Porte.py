"""
QUI: Thibaud Masset
QUAND: 19/03/25 8h45
QUOI: Classe Porte
"""

##################################
### Constructeur / Destructeur ###
##################################
class Porte():
    def __init__(self, para_idPorte: int, para_symbole: str = "%", para_positionX: int = 0, para_positionY: int = 0, para_idQuete: int = 0):

        self.__idPorte = para_idPorte
        self.__symbole = para_symbole
        self.__positionX = para_positionX
        self.__positionY = para_positionY
        self.__idQuete = para_idQuete

    #####################
    ###    Getters    ###
    #####################

    ### L'id de la porte
    @property
    def idPorte(self) -> int:
        return self.__idPorte

    ### L'état d'ouverture de la porte
    @property
    def symbole(self) -> str:
        return self.__symbole

    ### La position X de la porte
    @property
    def positionX(self) -> int:
        return self.__positionX 

    ### La position Y de la porte
    @property
    def positionY(self) -> int:
        return self.__positionY

    ### L'id de la quete
    @property
    def idQuete(self) -> int:
        return self.__idQuete   


    #####################
    ###    Setters    ###
    #####################

    ### L'état d'ouverture de la porte
    @symbole.setter
    def symbole(self, nouveau_symbole: str):
        if not isinstance(nouveau_symbole, str):
            raise TypeError("Veuillez encoder un caractère")
        self.__symbole = nouveau_symbole

    ################################
    ###         Méthodes         ###
    ################################

    """
    QUI: Sacha Fierin
    QUAND: 19/03/25
    QUOI: Méthode ouvrirPorte()
    Permet d'ouvrir la porte
    """
    def ouvrirPorte(self):
        self.symbole = " "  # Change le symbole en espace
        print(f"La porte {self.__idPorte} a été ouverte !")



    """
    QUI: Sacha Fierin
    QUAND: 19/03/25
    QUOI: Méthode __str__()
    Permet d'afficher le symbole de la porte
    """
    def __str__(self):
        return self.symbole
