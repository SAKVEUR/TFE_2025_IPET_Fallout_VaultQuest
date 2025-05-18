"""
QUI: Mathis Binnemans et Sacha Fierin
QUAND: 26/03/25
QUOI: Classe MaitreDuJeu
"""

####################
###    Import    ###
####################
from Joueur import Joueur
from Monstre import Monstre

##################################
### Constructeur / Destructeur ###
##################################
class MaitreDuJeu(Joueur):
    def __init__(self, para_nomJoueur:str, para_ordreJoueur: int = 1, para_monstres: list = []):
        if monstres is None:
            monstres = []
        super().__init__(para_nomJoueur, para_ordreJoueur, est_maitre_du_jeu=True)
        self.__monstres = para_monstres
        self.__tourMonstre = 0

    #####################
    ###    Getters    ###
    #####################

    ### GET Ordre de passage des monstres
    @property
    def positionTour(self) -> int:
        return self.positionTour

    ################################
    ###         Méthodes         ###
    ################################

    """
    QUI: Thibaud Masset
    QUAND: 27/03/25
    QUOI: Méthode avancerTour()
    Fait avancer le tour pou le prochain monstre
    """
    def avancerTour(self) -> None:
        if len(self.__monstres) > 0:
            self.__tourMonstre += 1
            print(f"Tour suivant, monstre {self.__monstres[self.positionTour].nomPerso} est maintenant au tour.")
        else:
            print("Aucun monstre à déplacer.")



    """
    QUI: Thibaud Masset
    QUAND: 27/03/25
    QUOI: Méthode attribuerMonstre()
    Attribue les monstres jouable au maitre du jeu
    """  
    def attribuerMonstres(self, monstres: list) -> None:
        self.__monstres = monstres



    """
    QUI: Thibaud Masset
    QUAND: 27/03/25
    QUOI: Méthode ajouterMonstre()
    Ajoute les monstres a une liste de monstre controlable par le maitre du jeu
    """
    def ajouterMonstre(self, monstre: Monstre) -> None:
        if monstre not in self.__monstres:
            self.__monstres.append(monstre)
            print(f"{monstre.nomPerso} a été ajouté aux monstres contrôlés.")
        else:
            print(f"{monstre.nomPerso} est déjà contrôlé par le Maitre du Jeu.")



    """
    QUI: Thibaud Masset
    QUAND: 27/03/25
    QUOI: Méthode retirerMonstre()
    Retire les monstre de la liste de monstre controlable par le maitre du jeu
    """
    def retirerMonstre(self, monstre: Monstre) -> None:
        if monstre in self.__monstres:
            self.__monstres.remove(monstre)
            print(f"{monstre.nomPerso} a été retiré des monstres contrôlés.")
        else:
            print(f"{monstre.nomPerso} n'est pas contrôlé par le Maitre du Jeu.")



    """
    QUI: Thibaud Masset
    QUAND: 27/03/25
    QUOI: Méthode deplacerMonstre()
    Permet de déplacer un monstre
    """
    def deplacerMonstre(self, monstre: Monstre, direction: str) -> None:
        if len(self.__monstres) > 0:
            monstre = self.__monstres[self.positionTour]  # Le monstre du tour actuel
            monstre.deplacer(direction)  # Appel à la méthode deplacer du monstre
            print(f"{monstre.nomPerso} se déplace vers {direction}.")
        else:
            print("Aucun monstre à déplacer.")