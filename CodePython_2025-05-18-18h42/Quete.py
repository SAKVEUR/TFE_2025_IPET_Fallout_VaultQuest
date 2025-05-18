"""
QUI: Mathis Binnemans
QUAND: 19/03/25
QUOI: Fichier classe "Quete"
"""

from Plateau import Plateau

##################################
### Constructeur / Destructeur ###
##################################
class Quete():
    def __init__(self, para_nomQuete: str, para_explicationQuete: str = "", para_messageFinQuete: str = "Vous avez terminé la quête!", para_numeroPlateau: int = 1):
        ### Définition des attributs
        self.__nomQuete = para_nomQuete
        self.__explicationQuete = para_explicationQuete
        self.__messageFinQuete = para_messageFinQuete
        self.__plateau = Plateau(para_numeroPlateau)
        self.configurerPlateau()

    #####################
    ###    Getters    ###
    #####################

    ### Nom de Quete
    @property
    def nomQuete(self) -> str:
        return self.__nomQuete

    ### Explication de quete
    @property
    def explicationQuete(self) -> str:
        return self.__explicationQuete

    ### Message de fin deQuete
    @property
    def messageFinQuete(self) -> str:
        return self.__messageFinQuete

    ### Plateau de la quete
    @property
    def plateau(self) -> Plateau:
        return self.__plateau

    ################################
    ###         Méthodes         ###
    ################################

    """
    QUI: Mathis Binnemans
    QUAND: 19/05/25
    QUOI: Méthode configurerPlateau()
    Configure le plateau en fonction du numéro de la quête
    """
    def configurerPlateau(self):
        if self.__plateau.identifiantPlan == 1:
            self.configurerPlateauQuete1()
        elif self.__plateau.identifiantPlan == 2:
            self.configurerPlateauQuete2()
        elif self.__plateau.identifiantPlan == 3:
            self.configurerPlateauQuete3()

    """
    QUI: Mathis Binnemans
    QUAND: 19/05/25
    QUOI: Méthode __configurerPlateauQuete1()
    Configure le plateau de la quête 1
    """
    def configurerPlateauQuete1(self):
        ### Murs Horizontaux
        for j in range(3, 7):
            self.__plateau.plateau[5][j] = "M" 
        self.__plateau.plateau[5][1] = "M"

        ### Murs Verticaux
        for i in range(1, 5):
            self.__plateau.plateau[i][6] = "M"

        ### Murs Verticaux Piece 2
        for k in range(6, 8):
            self.__plateau.plateau[k][5] = "M"

        ### Murs Horizontaux Piece 3
        for l in range(1, 4):
            self.__plateau.plateau[8][l] = "M"
        for m in range(5, 8):
            self.__plateau.plateau[8][m] = "M"
        for o in range(1, 8):
            self.__plateau.plateau[12][o] = "M"

        ### Murs Verticaux Piece 3
        for n in range(10, 12):
            self.__plateau.plateau[n][7] = "M"

        ### Murs Horizontaux Piece 4
        for p in range(10, 15):
            self.__plateau.plateau[3][p] = "M" 
        for s in range(10, 15):
            self.__plateau.plateau[9][s] = "M"

        ### Murs Verticaux Piece 4
        for q in range(4, 6):
            self.__plateau.plateau[q][10] = "M"
        for r in range(7, 9):
            self.__plateau.plateau[r][10] = "M"
        for t in range(4, 9):
            self.__plateau.plateau[t][14] = "M"



    """
    QUI: Mathis Binnemans
    QUAND: 19/05/25
    QUOI: Méthode configurerPlateauQuete2()
    Configure le plateau de la quête 2
    """
    def configurerPlateauQuete2(self):
        self.__plateau.plateau[1][5] = "X"



    """
    QUI: Mathis Binnemans
    QUAND: 19/05/25
    QUOI: Méthode configurerPlateauQuete3()
    Configure le plateau de la quête 3
    """
    def configurerPlateauQuete3(self):
        self.__plateau.plateau[8][5] = "%"



    """
    QUI: Mathis Binnemans
    QUAND: 19/03/25
    QUOI: Méthode afficherQueteChoisie()
    Afficher les informations de la quete choisie
    """
    def afficherQueteChoisie(self):
        print(f"Nom de la quête : {self.nomQuete}")
        print(f"Explication : {self.explicationQuete}")
        print(f"Plateau : {self.plateau.identifiantPlan}")

