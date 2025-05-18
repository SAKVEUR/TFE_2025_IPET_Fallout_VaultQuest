"""
QUI: Mathis Binnemans & Thibaud Masset
QUAND: 19/03/25
QUOI: Classe Joueur
"""

##################################
### Constructeur / Destructeur ###
##################################
class Joueur():
    def __init__(self, para_nomJoueur:str="joueur", est_maitre_du_jeu: bool = False):

        self.__nomJoueur:str = para_nomJoueur
        self.__est_maitreDuJeu:bool = est_maitre_du_jeu

    #####################
    ###    Getters    ###
    #####################

    ### Est le maître du jeu
    @property
    def est_maitreDuJeu(self) -> bool:
        return self.__est_maitreDuJeu

    ### Nom du joueur
    @property
    def nomJoueur(self) -> str:
        return self.__nomJoueur

    ################################
    ###         Méthodes         ###
    ################################

    """
    QUI: Sacha Fierin
    QUAND: 18/05/25
    QUOI: Méthode choisirPersonnageHeros()
    Permet au joueur de choisir un héros parmi ceux disponibles.
    """
    def choisirPersonnageHeros(self, heros_disponibles: list) -> list:

        print(f"\n{self.__nomJoueur}, choisissez votre héros :")
        
        # Afficher les héros disponibles
        for i, heros in enumerate(heros_disponibles, 1):
            print(f"\n{i}. {heros.nomPerso}")
            print(f"   Points de vie : {heros.points_vie_Perso}")
            print(f"   Arme : {heros.persoArme.nomArme} (Dégâts: {heros.persoArme.pointsDegatsArme})")
            print(f"   Armure : {heros.persoArmure.nomArmure} (Protection: {heros.persoArmure.pointsProtectionArmure})")
        
        # Demander le choix du joueur
        while True:
            try:
                choix = int(input("\nEntrez le numéro de votre héros : "))
                if 1 <= choix <= len(heros_disponibles):
                    # Assigner le héros choisi au joueur
                    self.personnage = heros_disponibles[choix - 1]
                    # Retirer le héros choisi de la liste des héros disponibles
                    heros_disponibles.pop(choix - 1)
                    print(f"\nVous avez choisi {self.personnage.nomPerso} !")
                    return heros_disponibles
                else:
                    print(f"Veuillez entrer un nombre entre 1 et {len(heros_disponibles)}.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")



    """
    QUI: Sacha Fierin
    QUAND: 18/05/25
    QUOI: Méthode nommerJoueur()
    Permet au joueur de choisir son nom.
    """
    def nommerJoueur(self):
        """
        Permet au joueur de choisir son nom.
        Le nom ne peut pas être vide.
        """
        while True:
            nom = input("Entrez votre nom : ").strip()
            if nom:  # Vérifie que le nom n'est pas vide
                self.__nomJoueur = nom
                break
            else:
                print("Le nom ne peut pas être vide.")
