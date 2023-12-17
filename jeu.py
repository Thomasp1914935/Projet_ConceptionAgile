import os
import pygame

class Joueurs:
    joueurs = []  # Liste de classe pour stocker tous les joueurs

    # Méthode pour initialiser un joueur
    def __init__(self, numero, nom):
        self.numero = numero
        self.nom = nom

    # [DEBUG]
    def __repr__(self):
        return f"   Joueur {self.numero} : {self.nom}"
    
class Taches:
    taches = []  # Liste de classe pour stocker toutes les tâches

    # Méthode pour initialiser une tâche
    def __init__(self, numero, titre, description, difficulte):
        self.numero = numero
        self.titre = titre
        self.description = description
        self.difficulte = difficulte

    # [DEBUG]
    def __repr__(self):
        return f"Tâche {self.numero} :\n   Titre : {self.titre}\n   Description : {self.description}\n   Difficulté : {self.difficulte}"

class Cartes:
    def __init__(self, nom_carte, position, fenetre, taille=None):
        # Charger l'image de la carte
        chemin_script = os.path.dirname(__file__)
        self.nom_carte = nom_carte
        chemin_carte = os.path.join(chemin_script, 'ressources', 'cartes', self.nom_carte + '.png')
        self.image = pygame.image.load(chemin_carte)

        # Redimensionner l'image si une taille est spécifiée
        if taille is not None:
            self.image = pygame.transform.scale(self.image, taille)

        # Stocker la position et la fenêtre
        self.position = position
        self.fenetre = fenetre

        # Attribut numero
        self.numero = None

        if nom_carte.isdigit():
            self.numero = int(nom_carte)
        

    def afficher(self):
        # Afficher l'image
        self.fenetre.blit(self.image, self.position)
    
    # Méthode pour vérifier si un bouton est survolé
    def est_survole(self, souris_x, souris_y):
        largeur, hauteur = self.image.get_size()
        if self.position[0] <= souris_x <= self.position[0] + largeur and self.position[1] <= souris_y <= self.position[1] + hauteur:
            return True
        return False

    # Méthode pour vérifier si une boîte de saisie est cliquée
    def est_clique(self, x, y):
        largeur, hauteur = self.image.get_size()
        return self.position[0] <= x <= self.position[0] + largeur and self.position[1] <= y <= self.position[1] + hauteur