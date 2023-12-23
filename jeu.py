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

class Partie:
    """
    Classe représentant une partie du jeu.

    Attributs:
        joueurs (list): Liste des joueurs de la partie.
        taches (list): Liste des tâches de la partie.
        mode_jeu (str): Le mode de jeu choisi.
        tour (int): Le tour actuel.
    """

    def __init__(self, joueurs, taches, mode_jeu):
        self.joueurs = joueurs
        self.taches = taches
        self.mode_jeu = mode_jeu
        self.tour = 0

    def joueur_actuel(self):
        """
        Méthode pour obtenir le joueur actuel.

        Renvvoie:
            Le joueur actuel.
        """
        return self.joueurs[self.tour % len(self.joueurs)]

    def tache_actuelle(self):
        """
        Méthode pour obtenir la tâche actuelle.

        Renvoie:
            La tâche actuelle.
        """
        return self.taches[self.tour // len(self.joueurs)]

    def passer_au_tour_suivant(self):
        """
        Méthode pour passer au tour suivant.
        """
        self.tour += 1

    def est_terminee(self):
        """
        Méthode pour vérifier si la partie est terminée.

        Renvoie:
            True si la partie est terminée, False sinon.
        """
        return self.tour >= len(self.joueurs) * len(self.taches)

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