import os
import pygame

from statistics import mean, median
from collections import Counter

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
    def __init__(self, mode, fenetre):
        self.mode = mode
        self.joueur_actuel = 0
        self.cartes_choisies = []
        self.log_cartes_choisies = []
        self.tache_actuelle = 1
        self.fenetre = fenetre

    def jouer(self, carte):
        """
        Fonction qui permet de jouer une carte.
        
        Arguments:
            carte (Cartes): La carte à jouer.
        """
        if self.tache_actuelle <= len(Taches.taches):
            if self.joueur_actuel < len(Joueurs.joueurs) - 1:
                print(f"[EVENT] : Carte '{carte.nom_carte}' cliquée") # [DEBUG]
                if carte.nom_carte != "interro" and carte.nom_carte != "cafe":
                    self.cartes_choisies.append(carte)
                self.log_cartes_choisies.append(carte)
                self.joueur_actuel += 1
                self.fenetre.affichage_joueur(Joueurs.joueurs[self.joueur_actuel])
            elif self.joueur_actuel == len(Joueurs.joueurs) - 1:
                print(f"[EVENT] : Carte '{carte.nom_carte}' cliquée") # [DEBUG]
                if carte.nom_carte != "interro" and carte.nom_carte != "cafe":
                    self.cartes_choisies.append(carte)
                self.log_cartes_choisies.append(carte)
                self.joueur_actuel += 1
                if all(carte.nom_carte == "cafe" for carte in self.log_cartes_choisies):
                        print("[INFO] : Tous les joueurs ont choisi la carte café. La partie est mise en pause et enregistrée.") # [DEBUG]
                        # Rajouter le traitement pour enregistrer la partie
                else:
                    self.fin_tour()
        elif self.tache_actuelle > len(Taches.taches):
            print("[INFO] : Toutes les tâches ont été traitées!") # [DEBUG]
            # Rajouter le traitement pour enregistrer la partie

    def fin_tour(self):
        """
        Fonction qui détermine l'issus du tour en fonction du mode de jeu.
        """
        if self.mode == "strict":
            if not len(set(self.cartes_choisies)) <= 1:
                print("[INFO] : Toutes les cartes choisies ne sont pas identiques !") # [DEBUG]
                self.rejouer_tour()
            else:
                print("[INFO] : Toutes les cartes choisies sont identiques !") # [DEBUG]
                strict = mean([int(carte.nom_carte) for carte in self.cartes_choisies])
                Taches.taches[self.tache_actuelle - 1].difficulte = strict
                self.tache_suivante()
        elif self.mode == "moyenne":
            moyenne = mean([int(carte.nom_carte) for carte in self.cartes_choisies])
            print(f"[INFO] : La moyenne de difficulté est de {moyenne}") # [DEBUG]
            Taches.taches[self.tache_actuelle - 1].difficulte = moyenne
            self.tache_suivante()
        elif self.mode == "médiane":
            mediane = median([int(carte.nom_carte) for carte in self.cartes_choisies])
            print(f"[INFO] : La médiane de difficulté est de {mediane}") # [DEBUG]
            Taches.taches[self.tache_actuelle - 1].difficulte = mediane
            self.tache_suivante()
        elif self.mode == "majorité absolue":
            valeurs_cartes = [int(carte.nom_carte) for carte in self.cartes_choisies]
            compteur = Counter(valeurs_cartes)
            valeur, nombre = compteur.most_common(1)[0]
            if nombre / len(valeurs_cartes) > 0.5:
                Taches.taches[self.tache_actuelle - 1].difficulte = valeur
                print(f"[INFO] : La difficulté {valeur} a la majorité absolue !") # [DEBUG]
                self.tache_suivante()
            else:
                print("[INFO] : Aucune difficulté n'a la majorité absolue !")  # [DEBUG]
                self.rejouer_tour()
        elif self.mode == "majorité relative":
            valeurs_cartes = [int(carte.nom_carte) for carte in self.cartes_choisies]
            compteur = Counter(valeurs_cartes)
            valeur, nombre = compteur.most_common(1)[0]
            if nombre > 1:
                Taches.taches[self.tache_actuelle - 1].difficulte = valeur
                print(f"[INFO] : La difficulté {valeur} a la majorité relative !") # [DEBUG]
                self.tache_suivante()
            else:
                print("[INFO] : Aucune difficulté n'a la majorité relative !") # [DEBUG]
                self.rejouer_tour()

    def rejouer_tour(self):
        """
        Fonction qui permet de rejouer le tour.
        """
        print("[INFO] : Le tour doit être rejoué !") # [DEBUG]
        self.joueur_actuel = 0
        self.cartes_choisies = []
        self.fenetre.affichage_joueur(Joueurs.joueurs[self.joueur_actuel])
    
    def tache_suivante(self):
        """
        Fonction qui permet de passer à la tâche suivante.
        """
        print(f"[INFO] : Résultat de la tâche :\n", Taches.taches[self.tache_actuelle - 1]) # [DEBUG]
        self.tache_actuelle += 1
        self.joueur_actuel = 0
        self.cartes_choisies = []
        if self.tache_actuelle <= len(Taches.taches):
            print(f"[INFO] : Tâche suivante à traiter :\n", Taches.taches[self.tache_actuelle - 1]) # [DEBUG]
            self.fenetre.affichage_tache(Taches.taches[self.tache_actuelle - 1])
            self.fenetre.affichage_joueur(Joueurs.joueurs[self.joueur_actuel])