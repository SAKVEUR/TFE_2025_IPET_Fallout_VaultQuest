"""
QUI: Mathis Binnemans et Sacha Fierin
QUAND: 26/03/25
QUOI: Classe Plateau
"""

##################################
### Constructeur / Destructeur ###
##################################
class Plateau():
    def __init__(self,paraIdentifiantPlan:int, para_nombreLigne:int = 15, para_nombreColonnes:int = 20):

        self.__identifiantPlan:int = paraIdentifiantPlan
        self.__nombreDeLigne:int = para_nombreLigne
        self.__nombreDeColonnes:int = para_nombreColonnes
        self.plateau = self.creerCases()

    #####################
    ###    Getters    ###
    #####################

    ### Identifiant du plateau
    @property
    def identifiantPlan(self):
        return self.__identifiantPlan

    ### Nombre de ligne du plateau
    @property
    def nombreDeLigne(self):
        return self.__nombreDeLigne
    

    ### Nombre de colonne du plateau
    @property
    def nombreDeColonne(self):
        return self.__nombreDeColonnes
    
    #####################
    ###    Setters    ###
    #####################

    ### Identifiant du plateau
    @identifiantPlan.setter
    def identifiantPlateau(self, para_identifiantPlan):
        if not isinstance(para_identifiantPlan, int):
            raise TypeError("L'indentifiant n'est pas un entier")
        self.__identifiantPlan = para_identifiantPlan

    ### Nombre de ligne du plateau
    @nombreDeLigne.setter
    def nombreDeLigne(self, para_nombreDeLigne):
        if not isinstance(para_nombreDeLigne, int):
            raise TypeError("Le nombreDeLigne n'est pas un entier")
        self.__nombreDeLigne = para_nombreDeLigne

    ### Nombre de colonne du plateau
    @nombreDeColonne.setter
    def nombreDeColonne(self, para_nombreDeColonne):
        if not isinstance(para_nombreDeColonne, int):
            raise TypeError("Le nombreDeColonne n'est pas un entier")
        self.__nombreDeColonne = para_nombreDeColonne

    ################################
    ###         Méthodes         ###
    ################################

    """
    QUI: Sacha Fierin
    QUAND: 03/04/25
    QUOI: Méthode creerCases()
    Création du plan, des cases du plateau
    """
    def creerCases(self):
        self.plateau = []
        case = " "
        nombreDeLigne = self.__nombreDeLigne
        nombreDeColonne  = self.__nombreDeColonnes
        for compteur_ligne in range (nombreDeLigne):
            listeLigne = []
            for compteur_colonne in range (nombreDeColonne):
                listeLigne.append(case) 
            self.plateau.append(listeLigne)

        ### Création des murs du contour du plateau en Vertical
        for i in range (0, nombreDeLigne):
            self.plateau[i][0] = "M"
            self.plateau[i][nombreDeColonne - 1] = "M"
        ### Création des murs du contour du plateau en Horizontal
        for j in range (0, nombreDeColonne):
            self.plateau[0][j] = "M"
            self.plateau[nombreDeLigne - 1][j] = "M"
        return self.plateau



    """
    QUI: Sacha Fierin
    QUAND: 03/04/25
    QUOI: Méthode creerCases()
    Affiche le plateau
    """
    def afficher_plateau(self):
        print(" ")
        for ligne in self.plateau:
            for case in ligne:
                print(case, end=" ")
            print()

