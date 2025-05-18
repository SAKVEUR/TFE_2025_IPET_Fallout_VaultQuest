"""
QUI: Mathis Binnemans & Sacha Fierin
QUAND: 25/03/25
QUOI: Classe Partie
"""

####################
###    Import    ###
####################
from Joueur import Joueur
from Personnage import Personnage
from MaitreDuJeu import MaitreDuJeu
from Heros import Heros
from Monstre import Monstre
from Plateau import Plateau
from Arme import Arme
from Armure import Armure
from Porte import Porte
from Coffre import Coffre
from De import De
from DesCombat import DesCombat
from DesDefense import DesDefense
from DesDeplacement import DesDeplacement
from Quete import Quete

##################################
### Constructeur / Destructeur ###
##################################
class Partie():
    def __init__(self):
        
        ### Liste des joueurs
        self.__joueurs = []
        ### Joueur actuellement actif
        self.__joueurActif: Joueur = None
        ### Ordre de jeu des joueurs
        self.__ordreJoueur: int = 1
        ### État de la partie, ici en cours
        self.__estFinie: bool = False
        ### État du coffre (si la bombe a été trouvée)
        self.__etatOuvertureCoffre: bool = False

        ### Initialisation des listes d'armes, armures, monstres, héros, quetes
        self.monstres_disponibles_quete1 = []
        self.monstres_disponibles_quete2 = []
        self.monstres_disponibles_quete3 = []
        self.monstres_qui_joue = []  # Liste des monstres actifs de la quête
        self.heros_disponibles = []  # Liste des héros disponibles pour les joueurs
        self.heros_qui_joue = []
        self.livretQuetes = []
        self.queteActuelle:Quete = None
        self.plateauActuel:Plateau = None

    #####################
    ###    Getters    ###
    #####################

    ### Les joueurs
    @property
    def joueurs(self):
        return self.__joueurs

    ### L'ordre du joueur actif
    @property
    def ordreJoueur(self):
        return self.__ordreJoueur

    ### Le joueur actif
    @property
    def joueurActif(self):
        return self.__joueurActif
    
    ### L'état de la partie
    @property
    def estFinie(self):
        return self.__estFinie

    ### État du coffre
    @property
    def etatOuvertureCoffre(self):
        return self.__etatOuvertureCoffre

    #####################
    ###    Setters    ###
    #####################

    ### Les joueurs
    @joueurs.setter
    def joueurs(self, joueurs):
        if not isinstance(joueurs, list):
            raise TypeError("Les joueurs doivent être dans une liste.")
        if not all(isinstance(joueur, Joueur) for joueur in joueurs):
            raise TypeError("Tous les éléments de la liste doivent être des instances de la classe Joueur.")
        self.__joueurs = joueurs

    ### L'ordre du joueur actif
    @ordreJoueur.setter
    def ordreJoueur(self, ordre: int):
        if not isinstance(ordre, int):
            raise TypeError("L'ordre du joueur doit être un entier.")
        if ordre <= 0:
            raise ValueError("L'ordre du joueur doit être supérieur à 0.")
        self.__ordreJoueur = ordre

    ### Le joueur actif
    @joueurActif.setter
    def joueurActif(self, joueur):
        if not isinstance(joueur, Joueur):
            raise TypeError("Le joueur actif doit être une instance de la classe Joueur.")
        self.__joueurActif = joueur

    ### L'état de la partie
    @estFinie.setter
    def estFinie(self, valeur: bool):
        if not isinstance(valeur, bool):
            raise TypeError("L'état de la partie doit être un booléen.")
        self.__estFinie = valeur

    ### État du coffre
    @etatOuvertureCoffre.setter
    def etatOuvertureCoffre(self, valeur: bool):
        if not isinstance(valeur, bool):
            raise TypeError("L'état du coffre doit être un booléen.")
        self.__etatOuvertureCoffre = valeur

    ################################
    ###         Méthodes         ###
    ################################

    ### Démarrer une partie ###
    def demarrer(self):
        print("Bienvenue dans l'aventure ! Préparation de la partie...")
        self.creerQuetes()
        self.InitialiserMateriel()  # Initialise le matériel du jeu, y compris les héros
        self.creerJoueurs()  # Crée les joueurs après avoir initialisé les héros
        self.choisirQueteEtPlateau()  # Choisit la quête et définit le plateau actuel
        print("\nVoici les infos de votre quête :")
        self.queteActuelle.afficherQueteChoisie()

    """
    QUI: Mathis Binnemans
    QUAND: 22/04/25
    QUOI: creerQuetes
    """
    def creerQuetes(self):
        ### Initialise les quêtes du jeu
        quete1 = Quete("L'appel à la défense", "Entré dans l'abri, on se rend compte de l'état après le passage des bombes...", "Vous avez terminé la quête!", 1)
        self.livretQuetes.append(quete1)
        quete2 = Quete("Le labyrinthe", "Les choses se corsent. Un bruit suspect à l'étage supérieur a mis les troupes d'Atomos en alerte...", "Vous avez terminé la quête!", 2)
        self.livretQuetes.append(quete2)
        quete3 = Quete("Résistance finale", "Après avoir traversé ces couloirs sans fin, éliminé ses sbires et évité ses pièges...", "Vous avez terminé la quête!", 3)
        self.livretQuetes.append(quete3)

    def choisirQueteEtPlateau(self):
        """
        QUI: Mathis Binnemans et Sacha Fierin
        QUAND: 14/04/25
        QUOI: Méthode de sélection de quête
        """
        while True:
            try:
                choix = int(input("Veuillez choisir une des trois quêtes (1, 2, 3) >>> "))
                if choix < 1 or choix > len(self.livretQuetes):
                    raise ValueError
                self.queteActuelle = self.livretQuetes[choix - 1]
                self.plateauActuel = self.queteActuelle.plateau
                
                # Transférer les monstres de la quête choisie vers monstres_qui_joue
                if choix == 1:
                    self.monstres_qui_joue.extend(self.monstres_disponibles_quete1)
                elif choix == 2:
                    self.monstres_qui_joue.extend(self.monstres_disponibles_quete2)
                elif choix == 3:
                    self.monstres_qui_joue.extend(self.monstres_disponibles_quete3)
                
                # Placer les personnages sur le plateau
                self.placerPersonnages()
                
                break
            except ValueError:
                print("Erreur : veuillez entrer un nombre entre 1 et 3.")

    """
    QUI: Sacha Fierin
    QUAND: 19/05/25
    QUOI: Méthode placerPersonnages()
    Place les héros et les monstres sur le plateau
    """
    def placerPersonnages(self):
        ### Placer les monstres sur le plateau actuel
        if self.plateauActuel is not None and self.monstres_qui_joue:
            try:
                for i, monstre in enumerate(self.monstres_qui_joue):
                    if monstre is not None:  # Vérifier si le monstre existe
                        if i == 0:
                            self.plateauActuel.plateau[monstre.positionY][monstre.positionX] = monstre
                        elif i == 1:
                            self.plateauActuel.plateau[monstre.positionY][monstre.positionX] = monstre
                        elif i == 2:
                            self.plateauActuel.plateau[monstre.positionY][monstre.positionX] = monstre
            except Exception as e:
                print(f"Erreur lors du placement des monstres : {e}")

        ### Placer les héros sur le plateau actuel
        if self.plateauActuel is not None:
            for i, heros in enumerate(self.heros_qui_joue):
                if i == 0:  # Premier héros
                    heros.positionX = 17
                    heros.positionY = 12
                    self.plateauActuel.plateau[heros.positionY][heros.positionX] = heros
                elif i == 1:  # Deuxième héros
                    heros.positionX = 18
                    heros.positionY = 12
                    self.plateauActuel.plateau[heros.positionY][heros.positionX] = heros
                elif i == 2:  # Troisième héros
                    heros.positionX = 17
                    heros.positionY = 13
                    self.plateauActuel.plateau[heros.positionY][heros.positionX] = heros
                elif i == 3:  # Quatrième héros
                    heros.positionX = 18
                    heros.positionY = 13
                    self.plateauActuel.plateau[heros.positionY][heros.positionX] = heros

    """
    QUI: Sacha Fierin
    QUAND: 03/04/25
    QUOI: Méthode InitialiserMateriel
    """
    ### Initialise le matériel du jeu"""
    def InitialiserMateriel(self):
        self.creerDesCombat()
        self.creerDesDefense()
        self.creerDesDeplacement()
        self.creerArme()
        self.creerArmure()
        self.creerPorte()
        self.creerCoffre()
        self.creerMonstre()
        self.creerHeros()

    """
    QUI: Sacha Fierin
    QUAND: 03/04/25
    QUOI: Méthode creerDesCombat()
    Créer les des de combat du jeu
    """
    def creerDesCombat(self):
        ### Création des dés de combat ###
        desCombat1 = DesCombat(6, 3)

    """
    QUI: Sacha Fierin
    QUAND: 03/04/25
    QUOI: Méthode creerDesDefense()
    Créer les des de défense du jeu
    """
    def creerDesDefense(self):
        ### Création des dés de défense ###
        desDefense1 = DesDefense(6, 2)

    """
    QUI: Sacha Fierin
    QUAND: 03/04/25
    QUOI: Méthode creerDesDeplacement()
    Créer les des de déplacement du jeu
    """
    def creerDesDeplacement(self):
        ### Création des dés de déplacement ###
        desDeplacement1 = DesDeplacement(6)
        desDeplacement2 = DesDeplacement(6)

    """
    QUI: Sacha Fierin
    QUAND: 03/04/25
    QUOI: Méthode creerArme()
    Créer les Armes du jeu
    """
    def creerArme(self):
        ### Créer toute les armes du jeu ###
        self.arme1 = Arme("Massue à pics", 3) # Goule mutante / Goule
        self.arme2 = Arme("Pistolet à clou", 5) # Pillard des Wastlands / Pillard
        self.arme3 = Arme("Pisto-laser", 4) # Impitoyable / Memmbre de la confrerie de l'acier
        self.arme4 = Arme("Exploseur de crane", 8) # Bourlingueur canibal / Atomos

    """
    QUI: Sacha Fierin
    QUAND: 03/04/25
    QUOI: Méthode creerArmure()
    Créer les Armures du jeu
    """
    def creerArmure(self):
        ### Créer toute les armures du jeu ###
        self.armure0 = Armure("Armure niveau 0", 1) # Bourlingueur canibal / Goule / Atomos
        self.armure1 = Armure("Armure niveau 1", 5) # Pillard des Wastlands / Impitoyable / Pillard
        self.armure2 = Armure("Armure niveau 2", 10) # Goule mutante / Memmbre de la confrerie de l'acier

    """
    QUI: Sacha Fierin
    QUAND: 03/04/25
    QUOI: Méthode creerPorte()
    Créer les portes du jeu
    """
    def creerPorte(self):
        ### Créer et ajouter à la liste toute les portes du jeu ###

        self.porte1 = Porte(1, "%")
        self.porte2 = Porte(2, "%")
        self.porte3 = Porte(3, "%")
        self.porte4 = Porte(4, "%")
        self.porte5 = Porte(5, "%")
        self.porte6 = Porte(6, "%")

    """
    QUI: Sacha Fierin
    QUAND: 03/04/25
    QUOI: Méthode creerCoffre()
    Créer les coffres du jeu
    """
    def creerCoffre(self):
        ### Création d'un coffre ###
        coffre = Coffre("Bombe", "X")

    """
    QUI: Sacha Fierin
    QUAND: 03/04/25
    QUOI: Méthode creerMonstre()
    Créer les monstres du jeu
    """
    def creerMonstre(self):
        ### Créer les Monstre de la partie

        ### Monstres de la quete 1
        self.monstres_disponibles_quete1.append(Monstre("Goule", 13, self.arme1, self.armure0, 1, 6, 5, "1"))
        self.monstres_disponibles_quete1.append(Monstre("Goule", 13, self.arme1, self.armure0, 11, 4, 5, "1"))
        self.monstres_disponibles_quete1.append(Monstre("Goule", 13, self.arme1, self.armure0, 18, 1, 5, "1"))

        ### Monstres de la quete 2
        self.monstres_disponibles_quete2.append(Monstre("Goule", 13, self.arme1, self.armure0, None, None, 5, "1"))
        self.monstres_disponibles_quete2.append(Monstre("Pillard", 15, self.arme2, self.armure1, None, None, 7, "2"))
        self.monstres_disponibles_quete2.append(Monstre("Pillard", 15, self.arme2, self.armure1, None, None, 7, "2"))
        self.monstres_disponibles_quete2.append(Monstre("Pillard", 15, self.arme2, self.armure1, None, None, 7, "2"))

        ### Monstres de la quete 3
        self.monstres_disponibles_quete3.append(Monstre("Goule", 13, self.arme1, self.armure0, None, None, 5, "1"))
        self.monstres_disponibles_quete3.append(Monstre("Pillard", 15, self.arme2, self.armure1, None, None, 7, "2"))
        self.monstres_disponibles_quete3.append(Monstre("Membre de la confrérie de l'acier", 11, self.arme3, self.armure2, None, None, 13, "3"))
        self.monstres_disponibles_quete3.append(Monstre("Membre de la confrérie de l'acier", 11, self.arme3, self.armure2, None, None, 13, "3"))
        self.monstres_disponibles_quete3.append(Monstre("Atomos", 30, self.arme4, self.armure0, None, None, 11, "4"))

    """
    QUI: Sacha Fierin
    QUAND: 03/04/25
    QUOI: Méthode creerHeros()
    Créer les héros du jeu
    """
    def creerHeros(self):
        """
        QUI: Sacha Fierin
        QUAND: 08/05/25
        QUOI: Méthode creerHeros()
        Crée les héros disponibles pour la partie avec leurs caractéristiques
        """
        # Créer les héros disponibles avec leurs caractéristiques
        self.heros_disponibles.append(Heros("Goule mutante", 16, self.arme1, self.armure2, None, None, 0, "A"))
        self.heros_disponibles.append(Heros("Pillard des Wastlands", 19, self.arme2, self.armure1, None, None, 0, "B"))
        self.heros_disponibles.append(Heros("Impitoyable", 17, self.arme3, self.armure1, None, None, 0, "C"))
        self.heros_disponibles.append(Heros("Bourlingueur canibal", 23, self.arme4, self.armure0, None, None, 0, "D"))

    """
    QUI: Sacha Fierin
    QUAND: 03/04/25
    QUOI: Méthode verifierCasesAdjacente()
    Vérifier les cases adjacentes et afficher les actions possibles
    """
    def verifierCasesAdjacente(self, personnage: Personnage):
        actions_possibles = []
        
        # Vérifier les 4 cases adjacentes
        cases_adjacentes = [
            (personnage.positionX, personnage.positionY-1),  # haut
            (personnage.positionX, personnage.positionY+1),  # bas
            (personnage.positionX-1, personnage.positionY),  # gauche
            (personnage.positionX+1, personnage.positionY)   # droite
        ]
        
        for x, y in cases_adjacentes:
            # Vérifier si les coordonnées sont valides
            if 0 <= x < self.plateauActuel.nombreDeColonne and 0 <= y < self.plateauActuel.nombreDeLigne:
                case = self.plateauActuel.plateau[y][x]
                
                if case == " ":
                    actions_possibles.append(("se déplacer", x, y))
                elif case == "X":
                    actions_possibles.append(("ouvrir le coffre", x, y))
                elif case == "%":
                    actions_possibles.append(("ouvrir la porte", x, y))
                elif isinstance(case, Personnage):
                    actions_possibles.append(("attaquer", x, y))
        
        # Afficher le plateau avant les actions possibles
        print("\nÉtat actuel du plateau :")
        self.plateauActuel.afficher_plateau()
        
        # Afficher les actions possibles de manière numérotée
        if actions_possibles:
            print("\nActions possibles :")
            for i, (action, x, y) in enumerate(actions_possibles, 1):
                print(f"{i}) {action} en ({x}, {y})")
            self.choisirAction(actions_possibles, personnage)
        else:
            print("\nAucune action possible.")

    def choisirAction(self, actions_possibles, personnage):
        try:
            choix = int(input("Veuillez choisir une action (numéro) ou 0 pour passer >>> "))
            if choix == 0:
                personnage.passerTour()
            elif 1 <= choix <= len(actions_possibles):
                action, x, y = actions_possibles[choix - 1]
                if action == "se déplacer":
                    personnage.seDeplacer(self.plateauActuel)
                elif action == "attaquer":
                    personnage.attaquer(self.plateauActuel)
                elif action == "ouvrir le coffre":
                    personnage.ouvrirCoffre(self.plateauActuel)
                elif action == "ouvrir la porte":
                    print("ouvrir la porte")
            else:
                print("Action invalide")
        except ValueError:
            print("Veuillez entrer un numéro")
 
    """
    QUI: Sacha Fierin
    QUAND: 03/04/25
    QUOI: Méthode finDePartie()
    Termine la partie
    """
    def finDePartie(self) -> None:
        self.__estFinie = True
        print("La partie est terminée.")

    """
    QUI: Mathis Binnemans & Sacha Fierin
    QUAND: 09/05/25
    QUOI: Méthode creerJoueurs()
    Crée les joueurs dont un maitre du jeu (obligatoire) et les autres joueurs héros compris entre 1 et 4
    """
    def creerJoueurs(self):
        ### Créer le maître du jeu
        joueur_maitreDuJeu = Joueur(None, True)
        self.__joueurs.append(joueur_maitreDuJeu)
        print("Le 1er joueur sera le maître du jeu")

        ### Demander le nombre de joueurs (les héros)
        nombre_joueurs = 0
        while nombre_joueurs < 1 or nombre_joueurs > 4:
            try:
                nombre_joueurs = int(input("Nombre de joueurs (héros) (1-4) : "))
                if nombre_joueurs < 1 or nombre_joueurs > 4:
                    print("Le nombre de joueurs doit être entre 1 et 4.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

        ### Créer les joueurs
        for i in range(nombre_joueurs):
            joueur = Joueur()
            self.__joueurs.append(joueur)

        ### Nommer les joueurs
        self.nommerJoueurs()

    """
    QUI: Mathis Binnemans & Sacha Fierin
    QUAND: 09/05/25
    QUOI: Méthode nommerJoueurs()
    Permet à chaque joueur de choisir son nom.
    """
    def nommerJoueurs(self):
        """
        Permet à chaque joueur de choisir son nom.
        """
        print("\n=== Nommage des joueurs ===")
        for i, joueur in enumerate(self.__joueurs, 1):
            print(f"\nJoueur {i}:")
            joueur.nommerJoueur()

        ### Choisir les héros
        self.choisirHerosJoueurs()

    """
    QUI: Mathis Binnemans & Sacha Fierin
    QUAND: 09/05/25
    QUOI: Méthode choisirHerosJoueurs()
    Permet à chaque joueur (sauf le maître du jeu) de choisir un héros
    """
    def choisirHerosJoueurs(self):
        """
        Permet à chaque joueur (sauf le maître du jeu) de choisir un héros
        parmi ceux disponibles.
        """
        print("\n=== Choix des héros ===")
        for joueur in self.__joueurs:
            if not joueur.est_maitreDuJeu:
                self.heros_disponibles = joueur.choisirPersonnageHeros(self.heros_disponibles)
                # Ajouter le héros choisi à la liste des héros qui jouent
                if joueur.personnage is not None:
                    self.heros_qui_joue.append(joueur.personnage)

    """
    QUI: Sacha Fierin
    QUAND: 09/05/25
    QUOI: Méthode verifierFinPartie()
    Vérifie si la partie est terminée
    """
    def verifierFinPartie(self):
        """
        Vérifie les conditions de fin de partie.
        La partie peut se terminer si :
        - Tous les héros sont morts
        - La quête est accomplie (bombe trouvée)
        """

        # Vérifier si la bombe a été trouvée
        if self.__etatOuvertureCoffre:
            print("\nLa Bombe a été retrouvée. Les HÉROS ont remporté la quête !")
            self.finDePartie()
            return True
            
        return False

    """
    QUI: Sacha Fierin
    QUAND: 09/05/25
    QUOI: Méthode jouerTour()
    Gère le déroulement d'un tour complet de jeu
    """
    def jouerTour(self):
        """
        Méthode principale qui gère le déroulement d'un tour complet de jeu.
        Elle alterne entre les tours des héros et des monstres.
        """
        numero_tour = 1
        
        while not self.__estFinie:
            print(f"\n=== Tour {numero_tour} ===")
            
            # Tour des héros
            self.jouerTourHeros()
            
            # Tour des monstres
            self.jouerTourMonstres()
            
            # Vérification de fin de partie
            if self.verifierFinPartie():
                break
                
            numero_tour += 1

    """
    QUI: Sacha Fierin
    QUAND: 09/05/25
    QUOI: Méthode jouerTourHeros()
    Gère le tour de tous les héros
    """
    def jouerTourHeros(self):
        """
        Gère le tour de tous les héros jouables.
        Chaque héros peut effectuer ses actions dans l'ordre.
        """
        print("\n=== Tour des héros ===")
        for heros in self.heros_qui_joue:
            if heros.points_vie_Perso > 0:  # On ne fait jouer que les héros vivants
                print(f"\nC'est au tour de {heros.nomPerso}")
                self.verifierCasesAdjacente(heros)
        print("\n=== Fin du tour des héros ===")

    """
    QUI: Sacha Fierin
    QUAND: 09/05/25
    QUOI: Méthode jouerTourMonstres()
    Gère le tour de tous les monstres
    """
    def jouerTourMonstres(self):
        """
        Gère le tour de tous les monstres présents sur le plateau.
        Les monstres effectuent leurs actions sous le contrôle du maître du jeu.
        """
        print("\n=== Tour des monstres ===")
        
        # Faire jouer chaque monstre de la quête
        for monstre in self.monstres_qui_joue:
            if monstre.points_vie_Perso > 0:  # On ne fait jouer que les monstres vivants
                print(f"\nC'est au tour du monstre {monstre.nomPerso}")
                self.verifierCasesAdjacente(monstre)
        print("\n=== Fin du tour des monstres ===")
