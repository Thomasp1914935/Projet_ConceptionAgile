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