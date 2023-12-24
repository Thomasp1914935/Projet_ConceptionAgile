import os
import pygame

class Joueurs:
    """
    Classe représentant un joueur du jeu.
    
    Attributs:
        joueurs (list): Liste de classe pour stocker tous les joueurs.
        numero (int): Le numéro du joueur.
        nom (str): Le nom du joueur.
    """
    joueurs = []

    def __init__(self, numero, nom):
        self.numero = numero
        self.nom = nom

    # [DEBUG] : Affiche les informations du joueur
    def __repr__(self):
        return f"   Joueur {self.numero} : {self.nom}"
    
class Taches:
    """
    Classe représentant une tâche du jeu.

    Attributs:
        taches (list): Liste de classe pour stocker toutes les tâches.
        numero (int): Le numéro de la tâche.
        titre (str): Le titre de la tâche.
        description (str): La description de la tâche.
        difficulte (int): La difficulté de la tâche.
    """
    taches = []

    def __init__(self, numero, titre, description, difficulte):
        self.numero = numero
        self.titre = titre
        self.description = description
        self.difficulte = difficulte

    # [DEBUG] : Affiche les informations de la tâche
    def __repr__(self):
        return f"Tâche {self.numero} :\n   Titre : {self.titre}\n   Description : {self.description}\n   Difficulté : {self.difficulte}"

class Cartes:
    """
    Classe représentant une carte du jeu.

    Attributs:
        nom_carte (str): Le nom de la carte.
        position (tuple): La position de la carte sur la fenêtre.
        fenetre (pygame.Surface): La fenêtre d'affichage du jeu.
        taille (tuple, optional): La taille de la carte (par défaut None).
    """

    def __init__(self, nom_carte, position, fenetre, taille=None):
        chemin_script = os.path.dirname(__file__)
        self.nom_carte = nom_carte
        chemin_carte = os.path.join(chemin_script, 'ressources', 'cartes', self.nom_carte + '.png')
        self.image = pygame.image.load(chemin_carte)

        if taille is not None:
            self.image = pygame.transform.scale(self.image, taille)

        self.position = position
        self.fenetre = fenetre    

    def afficher(self):
        """
        Affiche l'image de la carte sur la fenêtre.
        """
        self.fenetre.blit(self.image, self.position)
    
    def est_survole(self, souris_x, souris_y):
        """
        Vérifie si la carte est survolée par la souris.

        Arguments:
            souris_x (int): La position en x de la souris.
            souris_y (int): La position en y de la souris.

        Renvoie:
            bool: True si la carte est survolée, False sinon.
        """
        largeur, hauteur = self.image.get_size()
        if self.position[0] <= souris_x <= self.position[0] + largeur and self.position[1] <= souris_y <= self.position[1] + hauteur:
            return True
        return False

    def est_clique(self, x, y):
        """
        Vérifie si la carte est cliquée.

        Arguments:
            x (int): La position en x du clic.
            y (int): La position en y du clic.

        Renvoie:
            bool: True si la carte est cliquée, False sinon.
        """
        largeur, hauteur = self.image.get_size()
        return self.position[0] <= x <= self.position[0] + largeur and self.position[1] <= y <= self.position[1] + hauteur
    
class Partie:
    """
    Classe représentant la partie, le mode de jeu.

    Attributs:
        self.mode: Le mode de jeu.
        joueur_actuel: Le nb joueur en tain de jouer.
        les cartes choisies dans un tableau.
        le nombre de taches.
    """
    def __init__(self, mode):
        self.mode = mode
        self.joueur_actuel = 0
        self.cartes_choisies = []
        self.nb_taches_traitees = 0

    def jouer(self, fnt_jeu, souris_x, souris_y):
            for carte in fnt_jeu.liste_cartes:
                if carte.est_clique(souris_x, souris_y):
                    # Si toutes les tâches n'ont pas été traitées
                    if self.nb_taches_traitees <= len(Taches.taches):
                        # Si tout les joueurs n'ont pas joué
                        if self.joueur_actuel < len(Joueurs.joueurs) - 1:
                            print(f"[EVENT] : Carte '{carte.nom_carte}' cliquée") # [DEBUG]
                            self.cartes_choisies.append(carte)
                            # Ajouter un log pour le choix de la carte
                            fnt_jeu.log_choix_carte(Joueurs.joueurs[self.joueur_actuel])
                            # Incrémenter le tour du joueur
                            self.joueur_actuel += 1
                            # Ajouter un log pour le tour du joueur
                            fnt_jeu.log_tour_joueur(Joueurs.joueurs[self.joueur_actuel])
                            fnt_jeu.affichage_joueur(Joueurs.joueurs[self.joueur_actuel])
                        elif self.joueur_actuel < len(Joueurs.joueurs):
                            print(f"[EVENT] : Carte '{carte.nom_carte}' cliquée") # [DEBUG]
                            self.cartes_choisies.append(carte)
                            # Ajouter un log pour le choix de la carte
                            fnt_jeu.log_choix_carte(Joueurs.joueurs[self.joueur_actuel])
                            # Incrémenter le tour du joueur
                            self.joueur_actuel += 1
                            if not self.verifier_cartes():
                                print("Toutes les cartes choisies ne sont pas identiques!")
                                self.joueur_actuel = 0
                                self.cartes_choisies = []
                            else:
                                print("Toutes les cartes choisies sont identiques!")

    def verifier_cartes(self):
        return len(set(self.cartes_choisies)) <= 1