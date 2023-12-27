import os
from datetime import datetime
import json
import hashlib
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
    def __init__(self, mode, tache_actuelle, fenetre):
        self.mode = mode
        self.joueur_actuel = 0
        self.cartes_choisies = []
        self.log_cartes_choisies = []
        self.tache_actuelle = tache_actuelle
        self.premier_tour = True
        self.partie_finie = False
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
                return 0
            elif self.joueur_actuel == len(Joueurs.joueurs) - 1:
                print(f"[EVENT] : Carte '{carte.nom_carte}' cliquée") # [DEBUG]
                if carte.nom_carte != "interro" and carte.nom_carte != "cafe":
                    self.cartes_choisies.append(carte)
                self.log_cartes_choisies.append(carte)
                if all(carte.nom_carte == "interro" for carte in self.log_cartes_choisies):
                    self.rejouer_tour()
                    return 0
                elif all(carte.nom_carte == "cafe" for carte in self.log_cartes_choisies):
                    self.fin_partie()
                    return 2
                else:
                    tour_valide = self.fin_tour()
                    if tour_valide == True:
                        if self.tache_actuelle > len(Taches.taches):
                            self.partie_finie = True
                            self.fin_partie()
                            return 1
                    return 0
                    
    def fin_tour(self):
        """
        Fonction qui détermine l'issus du tour en fonction du mode de jeu.
        """
        if self.mode == "strict" or self.premier_tour == True:
            if not len(set(self.cartes_choisies)) <= 1:
                print("[INFO] : Toutes les cartes choisies ne sont pas identiques !") # [DEBUG]
                self.rejouer_tour()
                self.premier_tour = False
                return False
            else:
                print("[INFO] : Toutes les cartes choisies sont identiques !") # [DEBUG]
                strict = mean([int(carte.nom_carte) for carte in self.cartes_choisies])
                Taches.taches[self.tache_actuelle - 1].difficulte = strict
                self.tache_suivante()
                self.premier_tour = True
                return True
        elif self.mode == "moyenne":
            moyenne = mean([int(carte.nom_carte) for carte in self.cartes_choisies])
            print(f"[INFO] : La moyenne des cartes est de {moyenne}") # [DEBUG]
            Taches.taches[self.tache_actuelle - 1].difficulte = moyenne
            self.tache_suivante()
            self.premier_tour = True
            return True
        elif self.mode == "médiane":
            mediane = median([int(carte.nom_carte) for carte in self.cartes_choisies])
            print(f"[INFO] : La médiane des cartes est de {mediane}") # [DEBUG]
            Taches.taches[self.tache_actuelle - 1].difficulte = mediane
            self.tache_suivante()
            self.premier_tour = True
            return True
        elif self.mode == "majorité absolue":
            valeurs_cartes = [int(carte.nom_carte) for carte in self.cartes_choisies]
            compteur = Counter(valeurs_cartes)
            valeur, nombre = compteur.most_common(1)[0]
            if nombre / len(valeurs_cartes) > 0.5:
                Taches.taches[self.tache_actuelle - 1].difficulte = valeur
                print(f"[INFO] : La carte {valeur} a la majorité absolue !") # [DEBUG]
                self.tache_suivante()
                self.premier_tour = True
                return True
            else:
                print("[INFO] : Aucune carte n'a la majorité absolue !")  # [DEBUG]
                self.rejouer_tour()
                self.premier_tour = False
                return False
        elif self.mode == "majorité relative":
            valeurs_cartes = [int(carte.nom_carte) for carte in self.cartes_choisies]
            compteur = Counter(valeurs_cartes)
            valeur, nombre = compteur.most_common(1)[0]
            if nombre > 1:
                Taches.taches[self.tache_actuelle - 1].difficulte = valeur
                print(f"[INFO] : La carte {valeur} a la majorité relative !") # [DEBUG]
                self.tache_suivante()
                self.premier_tour = True
                return True
            else:
                print("[INFO] : Aucune carte n'a la majorité relative !") # [DEBUG]
                self.rejouer_tour()
                self.premier_tour = False
                return False

    def rejouer_tour(self):
        """
        Fonction qui permet de rejouer le tour.
        """
        print("[INFO] : Le tour doit être rejoué !") # [DEBUG]
        self.joueur_actuel = 0
        self.cartes_choisies = []
        self.log_cartes_choisies = []
        self.fenetre.affichage_joueur(Joueurs.joueurs[self.joueur_actuel])
    
    def tache_suivante(self):
        """
        Fonction qui permet de passer à la tâche suivante.
        """
        print(f"[INFO] : Résultat de la tâche :\n", Taches.taches[self.tache_actuelle - 1]) # [DEBUG]
        self.tache_actuelle += 1
        self.joueur_actuel = 0
        self.cartes_choisies = []
        self.log_cartes_choisies = []
        if self.tache_actuelle <= len(Taches.taches):
            print(f"[INFO] : Tâche suivante à traiter :\n", Taches.taches[self.tache_actuelle - 1]) # [DEBUG]
            self.fenetre.affichage_tache(Taches.taches[self.tache_actuelle - 1])
            self.fenetre.affichage_joueur(Joueurs.joueurs[self.joueur_actuel])
    
    def fin_partie(self):
        """
        Fonction qui gère la fin de la partie.
        """
        if self.partie_finie == True:
            print("[INFO] : Toutes les tâches ont été traitées !") # [DEBUG]
            self.joueur_actuel = None
            self.cartes_choisies = []
            self.log_cartes_choisies = []
            self.tache_actuelle = None
            self.sauvergarde_partie()
        else:
            print("[INFO] : Tous les joueurs ont choisi la carte café.") # [DEBUG]
            self.joueur_actuel = 0
            self.cartes_choisies = []
            self.log_cartes_choisies = []
            self.sauvergarde_partie()                        

    def sauvergarde_partie(self):
        """
        Fonction qui permet d'enregistrer la partie dans un fichier JSON.
        """
        sauvegarde = {
            "horodatage": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "partie_finie": self.partie_finie,
            "mode_jeu": self.mode,
            "joueur_actuel": self.joueur_actuel,
            "cartes_choisies": [carte.nom_carte for carte in self.cartes_choisies],
            "log_cartes_choisies": [carte.nom_carte for carte in self.log_cartes_choisies],
            "tache_actuelle": self.tache_actuelle,
            "joueurs": [{"numero": joueur.numero, "nom": joueur.nom} for joueur in Joueurs.joueurs],
            "taches": [{"numero": tache.numero, "titre": tache.titre, "description": tache.description, "difficulte": tache.difficulte} for tache in Taches.taches]
        }
        
        sauvegarde_str = json.dumps(sauvegarde, sort_keys=True)
        sauvegarde_hash = hashlib.sha256(sauvegarde_str.encode()).hexdigest()
        
        with open('sauvegarde.json', 'w') as f:
            json.dump({'data': sauvegarde, 'hash': sauvegarde_hash}, f)

        print("[INFO] : La partie a été enregistrée avec succès") # [DEBUG]

    def analyse_sauvegarde(self):
        """
        Méthode pour vérifier l'intégrité de la sauvegarde.
        """
        with open('sauvegarde.json', 'r') as f:
            sauvegarde = json.load(f)
        self.data = sauvegarde['data']
        hash = sauvegarde['hash']
        sauvegarde_str = json.dumps(self.data, sort_keys=True)
        sauvegarde_hash = hashlib.sha256(sauvegarde_str.encode()).hexdigest()

        if sauvegarde_hash != hash:
            return 2

        cles = ["horodatage", "partie_finie", "mode_jeu", "joueur_actuel", "cartes_choisies", "log_cartes_choisies", "tache_actuelle", "joueurs", "taches"]

        for cle in cles:
            if cle not in self.data:
                return 1
        return 0
    
    def charger_sauvegarde(self):
        """
        Méthode pour charger une partie à partir d'une sauvegarde.
        """
        # Vérifier si la partie est terminée
        partie_finie = self.data['partie_finie']
        
        # Initialiser l'état du jeu à partir de la sauvegarde
        self.horodatage = self.data['horodatage']
        self.mode_jeu = self.data['mode_jeu']
        self.joueur_actuel = self.data['joueur_actuel']
        self.cartes_choisies = [Cartes(nom) for nom in self.data['cartes_choisies']]
        self.log_cartes_choisies = [Cartes(nom) for nom in self.data['log_cartes_choisies']]
        self.tache_actuelle = self.data['tache_actuelle']
        Joueurs.joueurs = [Joueurs(joueur['numero'], joueur['nom']) for joueur in self.data['joueurs']]
        Taches.taches = [Taches(tache['numero'], tache['titre'], tache['description'], tache['difficulte']) for tache in self.data['taches']]

        # Retourner les valeurs demandées
        return partie_finie, self.mode_jeu, self.tache_actuelle, self.joueur_actuel