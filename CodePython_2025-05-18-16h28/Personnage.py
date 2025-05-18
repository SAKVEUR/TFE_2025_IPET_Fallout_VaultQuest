"""
QUI: Thibaud Masset & Mathis Binnemans & Sacha Fierin
QUAND: 27/03/25
QUOI: Classe Personnage
"""

####################
###    Import    ###
####################
from DesDeplacement import DesDeplacement
from DesCombat import DesCombat
from DesDefense import DesDefense
from Arme import Arme
from Armure import Armure
from Coffre import Coffre
from Porte import Porte

##################################
### Constructeur / Destructeur ###
##################################
class Personnage():
    def __init__(self, para_nomPerso:str, para_points_vie_Perso:int, para_Perso_arme:Arme, para_Perso_armure:Armure, para_positionX: int = 0, para_positionY: int = 0, para_nombreDeplacement:int = 5, para_iconePersonnage:str = "*"):
        self.__nomPerso:str = para_nomPerso
        self.__points_vie_Perso:int = para_points_vie_Perso
        self.__heroArme:Arme = para_Perso_arme
        self.__heroArmure:Armure = para_Perso_armure
        self.__positionX:int = para_positionX
        self.__positionY:int = para_positionY
        self.__nombreDeDeplacement:int = para_nombreDeplacement
        self.__iconePersonnage:str = para_iconePersonnage
        self.__estEnCombat:bool = False
        self.__ennemiEnCombat:Personnage = None
       
        # Initialisation des dés
        self.__desCombat = DesCombat(6, 3)  # 6 faces, 3 faces d'attaque
        self.__desDefense = DesDefense(6, 2)  # 6 faces, 2 faces de défense

    #####################
    ###    Getters    ###
    #####################

    ### Nom personnage
    @property
    def nomPerso(self) -> str:
        return self.__nomPerso

    ### Point de vie du personnage
    @property
    def points_vie_Perso(self) -> None:
        return self.__points_vie_Perso

    ### Arme du personnage
    @property
    def persoArme(self) -> None:
        return self.__heroArme

    ### Armure du personnage
    @property
    def persoArmure(self) -> None:
        return self.__heroArmure

    ### Position en X
    @property
    def positionX(self) -> int:
        return self.__positionX

    ### Position en Y
    @property
    def positionY(self) -> int:
        return self.__positionY

    ### Nombre de deplacement du personnage
    @property
    def nombreDeDeplacement(self) -> int:
        return self.__nombreDeDeplacement

    ### Icône du personnage
    @property
    def iconePersonnage(self) -> str:
        return self.__iconePersonnage

    #####################
    ###    Setters    ###
    #####################

    ### Point de vie du personnage
    @points_vie_Perso.setter
    def points_vie_Perso(self, para_points_vie_Perso) -> None:
        if not isinstance(para_points_vie_Perso, int):
            raise TypeError("Pas un nombre entier !")
        if not para_points_vie_Perso >= 0:
            raise ValueError("Points de vie plus petit ou égale à 0 !")
        self.__points_vie_Perso = para_points_vie_Perso

    ### Arme du personnage
    @persoArme.setter
    def persoArme(self, para_persoArme) -> None:
        if not isinstance(para_persoArme, Arme):
            raise TypeError("L'arme n'est pas de type arme")
        self.__heroArme = para_persoArme

    ### Armure du personnage
    @persoArmure.setter
    def persoArmure(self, para_PersoArmure) -> None:
        if not isinstance(para_PersoArmure, Armure):
            raise TypeError("L'armure n'est pas de type armure")
        self.__heroArmure = para_PersoArmure

    ### Position en X
    @positionX.setter
    def positionX(self, para_positionX: int) -> None:
        if not isinstance(para_positionX, int):
            raise TypeError("La position en X n'est pas de type int")
        self.__positionX = para_positionX

    ### Position en Y
    @positionY.setter
    def positionY(self, para_positionY: int) -> None:
        if not isinstance(para_positionY, int):
            raise TypeError("La position en Y n'est pas de type int")
        self.__positionY = para_positionY

    ### Nombre de déplacement
    @nombreDeDeplacement.setter
    def nombreDeDeplacement(self, para_nombreDeplacement: int) -> None:
        if not isinstance(para_nombreDeplacement, int):
            raise TypeError("Le nombre de déplacement n'est pas de type int")
        if not para_nombreDeplacement >= 0:
            raise ValueError("Le nombre de déplacement n'est pas plus grand ou égale à 0")
        self.__nombreDeDeplacement = para_nombreDeplacement
    
    ### Icône du personnage
    @iconePersonnage.setter
    def iconePersonnage(self, para_iconePersonnage: str) -> None:
        if not isinstance(para_iconePersonnage, str):
            raise TypeError("L'icône du personnage n'est pas de type str")
        self.__iconePersonnage = para_iconePersonnage


    ################################
    ###         Méthodes         ###
    ################################

    """
    QUI: Sacha Fierin
    QUAND: 06/05/25
    QUOI: Méthode passerTour()
    Permet au personnage de passer son tour en mettant son nombre de déplacements à 0
    """
    def passerTour(self):
        self.__nombreDeDeplacement = 0
        print(f"{self.__nomPerso} passe son tour. Plus aucun déplacement possible.")
    
    
    
    """
    QUI: Sacha Fierin
    QUAND: 02/05/25
    QUOI: Méthode lancerDesDeplacement()
    Permet de lancer des dés afin de se déplacer
    """
    def lancerDesDeplacement(self):
        if self.__nombreDeDeplacement > 0:
            valeur = self.__nombreDeDeplacement
            self.__nombreDeDeplacement = valeur
        else:
            des = DesDeplacement()
            valeur1 = des.lancer()
            valeur2 = des.lancer()
            sommeDeDeplacement = valeur1 + valeur2
            self.__nombreDeDeplacement = sommeDeDeplacement
        print(f"Vous avez obtenu {sommeDeDeplacement} déplacements possibles.") 



    """
    QUI: Sacha Fierin
    QUAND: 02/05/25
    QUOI: Méthode seDeplacer()
    Permet au personnage de se déplacer dans une direction donnée
    """
    def seDeplacer(self, plateau):

        ### Si pas de déplacements restants alors lancer les dés de déplacement
        if self.__nombreDeDeplacement == 0:
            print("Lancer des dés de déplacement :")
            self.lancerDesDeplacement()
        while self.__nombreDeDeplacement > 0:

            plateau.afficher_plateau()
            print(f"Il vous reste {self.__nombreDeDeplacement} déplacement(s).")
            ### Demander la direction de déplacement
            direction = input("Dans quelle direction voulez-vous vous déplacer ? (haut/bas/gauche/droite) ou alors 'passer' pour passer votre tour >>> ").lower()
            
            ### Appeler la méthode de déplacement appropriée
            deplacement_reussi = False
            if direction == "haut":
                deplacement_reussi = self.avancerHaut(plateau)
            elif direction == "bas":
                deplacement_reussi = self.avancerBas(plateau)
            elif direction == "gauche":
                deplacement_reussi = self.avancerGauche(plateau)
            elif direction == "droite":
                deplacement_reussi = self.avancerDroite(plateau)
            elif direction == "passer":
                self.passerTour()
            else:
                print("Direction invalide. Veuillez choisir entre haut, bas, gauche ou droite.")


            ### Si le déplacement a réussi, diminuer le nombre de déplacements restants
            if deplacement_reussi:
                self.__nombreDeDeplacement = self.__nombreDeDeplacement - 1
                print(f"Il vous reste {self.__nombreDeDeplacement} déplacement(s).")
        
        print("Plus de déplacements disponibles.")


    """
    QUI: Sacha Fierin
    QUAND: 22/04/25
    QUOI: Méthode avancerHaut()
    Déplace le personnage d'une case vers le haut
    """
    def avancerHaut(self, plateau):
        nouvelleY = self.positionY - 1
        
        # Vérifier si la nouvelle position est dans les limites du plateau
        if 0 <= nouvelleY < plateau.nombreDeLigne:
            # Vérifier si la case est vide
            if plateau.plateau[nouvelleY][self.positionX] == " ":
                # Mettre à jour la position du personnage
                plateau.plateau[self.positionY][self.positionX] = " "  # Ancienne position
                self.positionY = nouvelleY
                plateau.plateau[nouvelleY][self.positionX] = str(self)
                print(f"{self.__nomPerso} s'est déplacé vers le haut.")
                return True
            else:
                print("Cette case est occupée. Veuillez choisir une autre direction.")
        else:
            print("Déplacement impossible : hors des limites du plateau.")
        return False



    """
    QUI: Sacha Fierin
    QUAND: 22/04/25
    QUOI: Méthode avancerBas()
    Déplace le personnage d'une case vers le bas
    """
    def avancerBas(self, plateau):

        nouvelleY = self.positionY + 1
        
        # Vérifier si la nouvelle position est dans les limites du plateau
        if 0 <= nouvelleY < plateau.nombreDeLigne:
            # Vérifier si la case est vide
            if plateau.plateau[nouvelleY][self.positionX] == " ":
                # Mettre à jour la position du personnage
                plateau.plateau[self.positionY][self.positionX] = " "  # Ancienne position
                self.positionY = nouvelleY
                plateau.plateau[nouvelleY][self.positionX] = str(self)
                print(f"{self.__nomPerso} s'est déplacé vers le bas.")
                return True
            else:
                print("Cette case est occupée. Veuillez choisir une autre direction.")
        else:
            print("Déplacement impossible : hors des limites du plateau.")
        return False



    """
    QUI: Sacha Fierin
    QUAND: 22/04/25
    QUOI: Méthode avancerGauche()
    Déplace le personnage d'une case vers la gauche
    """
    def avancerGauche(self, plateau):

        nouvelleX = self.positionX - 1
        
        # Vérifier si la nouvelle position est dans les limites du plateau
        if 0 <= nouvelleX < plateau.nombreDeColonne:
            # Vérifier si la case est vide
            if plateau.plateau[self.positionY][nouvelleX] == " ":
                # Mettre à jour la position du personnage
                plateau.plateau[self.positionY][self.positionX] = " "  # Ancienne position
                self.positionX = nouvelleX
                plateau.plateau[self.positionY][nouvelleX] = str(self)
                print(f"{self.__nomPerso} s'est déplacé vers la gauche.")
                return True
            else:
                print("Cette case est occupée. Veuillez choisir une autre direction.")
        else:
            print("Déplacement impossible : hors des limites du plateau.")
        return False



    """
    QUI: Sacha Fierin
    QUAND: 22/04/25
    QUOI: Méthode avancerDroite()
    Déplace le personnage d'une case vers la droite
    """
    def avancerDroite(self, plateau):
        nouvelleX = self.positionX + 1
        
        # Vérifier si la nouvelle position est dans les limites du plateau
        if 0 <= nouvelleX < plateau.nombreDeColonne:
            # Vérifier si la case est vide
            if plateau.plateau[self.positionY][nouvelleX] == " ":
                # Mettre à jour la position du personnage
                plateau.plateau[self.positionY][self.positionX] = " "  # Ancienne position
                self.positionX = nouvelleX
                plateau.plateau[self.positionY][nouvelleX] = str(self)
                print(f"{self.__nomPerso} s'est déplacé vers la droite.")
                return True
            else:
                print("Cette case est occupée. Veuillez choisir une autre direction.")
        else:
            print("Déplacement impossible : hors des limites du plateau.")
        return False



    """
    QUI: Sacha Fierin
    QUAND: 02/05/25
    QUOI: Méthode deplacerPersonnage()
    Déplace directement le personnage sur le plateau selon la direction choisie
    """
    def deplacerPersonnage(self, plateau, direction):
        nouvelleX = self.positionX
        nouvelleY = self.positionY
        
        if direction == "haut":
            nouvelleY -= 1
        elif direction == "bas":
            nouvelleY += 1
        elif direction == "gauche":
            nouvelleX -= 1
        elif direction == "droite":
            nouvelleX += 1
            
        if 0 <= nouvelleX < plateau.nombreDeColonne and 0 <= nouvelleY < plateau.nombreDeLigne:
            if plateau.plateau[nouvelleY][nouvelleX] == " ":
                plateau.plateau[self.positionY][self.positionX] = " "  # Effacer l'ancienne position
                self.positionX = nouvelleX
                self.positionY = nouvelleY
                plateau.plateau[nouvelleY][nouvelleX] = str(self)  # Utiliser l'icône du personnage
                print(f"{self.nomPerso} s'est déplacé vers {direction}.")
                return True
            else:
                print("Cette case est occupée. Veuillez choisir une autre direction.")
        else:
            print("Déplacement impossible : hors des limites du plateau.")
        return False
    

    
    """
    QUI: Thibaud Masset
    QUAND: 03/04/25
    QUOI: Méthode trouverEnnemisAPortee()
    Trouve tous les ennemis à portée d'attaque    
    """
    def trouverEnnemisAPortee(self, plateau, distance_max: int = 1) -> list:

        ennemis_a_portee = []
        
        # Parcourir toute les case autour du personnage
        for dx in range(-distance_max, distance_max + 1):
            for dy in range(-distance_max, distance_max + 1):
                # Ignorer la case actuelle
                if dx == 0 and dy == 0:
                    continue
                    
                nouveauX = self.positionX + dx
                nouveauY = self.positionY + dy
                
                # Vérifier si la case est dans les limites du plateau
                if 0 <= nouveauX < plateau.nombreDeColonne and 0 <= nouveauY < plateau.nombreDeLigne:
                    # Vérifier si un ennemi est présent sur la case
                    if isinstance(plateau.plateau[nouveauY][nouveauX], Personnage):
                        ennemis_a_portee.append(plateau.plateau[nouveauY][nouveauX])
                        
        return ennemis_a_portee



    """
    QUI: Thibaud Masset
    QUAND: 03/04/25
    QUOI: Méthode choisirEnnemi()
    Permet au joueur de choisir un ennemi parmi ceux à portée
    """
    def choisirEnnemi(self, ennemis: list) -> 'Personnage':
        if not ennemis:
            print("Aucun ennemi à portée d'attaque.")
            return None
            
        print("\nEnnemis à portée d'attaque :")
        for i, ennemi in enumerate(ennemis, 1):
            print(f"{i}. {ennemi.nomPerso} (PV: {ennemi.points_vie_Perso})")
            
        while True:
            try:
                choix = int(input("Choisissez un ennemi à attaquer (numéro) : ")) - 1
                if 0 <= choix < len(ennemis):
                    return ennemis[choix]
                else:
                    print("Numéro invalide, veuillez réessayer.")
            except ValueError:
                print("Veuillez entrer un numéro valide.")



    """
    QUI: Thibaud Masset
    QUAND: 03/04/25
    QUOI: Méthode lancerDesCombat()
    Lance les dés de combat et calcule les dégâts
    """
    def lancerDesCombat(self) -> int:
        # Utiliser la classe DesCombat pour lancer les dés
        resultat_des = self.__desCombat.lancer()
        
        # Calculer les dégâts en fonction du résultat du dé et des dégâts de l'arme
        degats = resultat_des * self.persoArme.pointsDegatsArme
        
        print(f"{self.nomPerso} lance les dés de combat : {resultat_des}")
        print(f"Dégâts potentiels : {degats}")
        
        return degats
    


    """
    QUI: Thibaud Masset
    QUAND: 03/04/25
    QUOI: Méthode lancerDesDefense()
    Lance les dés de défense et calcule la protection
    """
    def lancerDesDefense(self) -> int:

        # Utiliser la classe DesDefense pour lancer les dés
        resultat_des = self.__desDefense.lancer()
        
        # Calculer la protection en fonction du résultat du dé et de la protection de l'armure
        protection = resultat_des * self.persoArmure.pointsProtectionArmure
        
        print(f"{self.nomPerso} lance les dés de défense : {resultat_des}")
        print(f"Protection : {protection}")
        
        return protection
    


    """
    QUI: Thibaud Masset
    QUAND: 03/04/25
    QUOI: Méthode calculerDegatsFinaux()
    Calcule les dégâts finaux après application de la protection
    """
    def calculerDegatsFinaux(self, degats_bruts: int, protection: int) -> int:
        degats_finaux = max(0, degats_bruts - protection)
        print(f"Dégâts finaux après protection : {degats_finaux}")
        return degats_finaux
    


    """
    QUI: Thibaud Masset
    QUAND: 03/04/25
    QUOI: Méthode appliquerDegats()
    Applique les dégâts au personnage
    """
    def appliquerDegats(self, degats: int) -> None:
        self.points_vie_Perso = max(0, self.points_vie_Perso - degats)
        print(f"{self.nomPerso} perd {degats} points de vie.")
        print(f"Points de vie restants : {self.points_vie_Perso}")
        
        if self.points_vie_Perso == 0:
            print(f"{self.nomPerso} est vaincu !")



    """
    QUI: Thibaud Masset
    QUAND: 03/04/25
    QUOI: Méthode attaquer()
    Gère le processus d'attaque complet
    """
    def attaquer(self, plateau) -> None:
        # Trouver les ennemis à portée
        ennemis = self.trouverEnnemisAPortee(plateau)
        
        # Choisir un ennemi
        ennemi = self.choisirEnnemi(ennemis)
        if not ennemi:
            return
            
        print(f"\n{self.nomPerso} attaque {ennemi.nomPerso} !")
        
        # Lancer les dés de combat
        degats_bruts = self.lancerDesCombat()
        
        # L'ennemi se défend
        protection = ennemi.lancerDesDefense()
        
        # Calculer les dégâts finaux
        degats_finaux = self.calculerDegatsFinaux(degats_bruts, protection)
        
        # Appliquer les dégâts
        ennemi.appliquerDegats(degats_finaux)



    """
    QUI: Thibaud Masset
    QUAND: 03/04/25
    QUOI: Méthode seDefendre()
    Gère la défense du personnage
    """
    def seDefendre(self) -> int:

        print(f"{self.nomPerso} se prépare à se défendre !")
        return self.lancerDesDefense()






    """
    QUI: Sacha Fierin
    QUAND: 02/05/25
    QUOI: Méthode ouvrirCoffre()
    Ouvre un coffre si celui-ci est à proximité.
    """
    def ouvrirCoffre(self, plateau):
        # Vérifier les cases adjacentes pour trouver le coffre
        cases_adjacentes = [
            [self.positionX-1, self.positionY],  # haut
            [self.positionX+1, self.positionY],  # bas
            [self.positionX, self.positionY-1],  # gauche
            [self.positionX, self.positionY+1]   # droite
        ]
        
        for x, y in cases_adjacentes:
            if 0 <= x < len(plateau.plateau) and 0 <= y < len(plateau.plateau[0]):
                if plateau.plateau[x][y] == "X":  # Si on trouve un coffre
                    coffre = Coffre("Bombe", "X", x, y)
                    print(coffre.devoilerContenu())
                    plateau.plateau[x][y] = " "  # Remplacer le coffre par une case vide
                    return



    """
    QUI: Sacha Fierin
    QUAND: 02/05/25
    QUOI: Méthode __str__()
    Retourne l'icône du personnage pour l'affichage sur le plateau
    """
    def __str__(self):
        return self.__iconePersonnage

