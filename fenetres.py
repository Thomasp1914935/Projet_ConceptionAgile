import os
from datetime import datetime
import pygame

from interface import Fenetre, Rectangle, Bouton, BoiteTexte, BoiteSaisie
from jeu import Cartes

class FntAccueil(Fenetre, Bouton, BoiteTexte):
    """
    Classe représentant la fenêtre d'accueil du jeu Planning Poker.
    
    Elle permet aux utilisateurs de démarrer une nouvelle partie selon le mode choisi ou de charger une partie existante.
    """

    def __init__(self):
        # Paramètres de la fenêtre
        fnt_accueil_l = 450
        fnt_accueil_h = 700
        super().__init__(fnt_accueil_l, fnt_accueil_h)
        self.set_titre("Planning Poker : Accueil")
        self.set_couleur_fond((255, 255, 255))
        self.btn_l = 270
        self.btn_h = 40
        self.btn_x = (fnt_accueil_l - self.btn_l) / 2
        btn_espacement = 60
        self.btn_taille_police = 30
        self.btn_couleur_texte = (255, 255, 255)
        btn_couleur = (0, 0, 0)

        # Affichage de l'icone de l'application
        chemin_script = os.path.dirname(__file__)
        chemin_icone = (chemin_script, 'ressources', 'icone.png')
        chemin_icone = os.path.join(os.path.sep, *chemin_icone)
        icone = pygame.image.load(chemin_icone)
        img_icone_l = 50
        img_icone_h = 50
        icone = pygame.transform.scale(icone, (img_icone_l, img_icone_h))
        img_icone_x = fnt_accueil_l / 2 - icone.get_width() / 2
        img_icone_y = 50
        self.fenetre.blit(icone, (img_icone_x, img_icone_y))

        # Création du message d'accueil
        bt_pp = BoiteTexte(fnt_accueil_l / 2, 100, "Planning Poker", 40, (0, 0, 0), True, 100, self.fenetre)
        bt_pp.dessiner()
        bt_mode_jeu = BoiteTexte(fnt_accueil_l / 2, 150, "Démarrez une nouvelle partie en choississant un mode de jeu :", 25, (0, 0, 0), True, 40, self.fenetre)
        bt_mode_jeu.dessiner()

        # Création du bouton "Mode strict"
        btn_strict_y = 200
        self.btn_strict = Bouton(self.btn_x, btn_strict_y, self.btn_l, self.btn_h, "Mode strict", self.btn_taille_police, self.btn_couleur_texte, btn_couleur, self.fenetre)
        self.btn_strict.dessiner()

        # Création du bouton "Mode moyenne"
        btn_moyenne_y = btn_strict_y + btn_espacement
        self.btn_moyenne = Bouton(self.btn_x, btn_moyenne_y, self.btn_l, self.btn_h, "Mode moyenne", self.btn_taille_police, self.btn_couleur_texte, btn_couleur, self.fenetre)
        self.btn_moyenne.dessiner()

        # Création du bouton "Mode médiane"
        btn_mediane_y = btn_moyenne_y + btn_espacement
        self.btn_mediane = Bouton(self.btn_x, btn_mediane_y, self.btn_l, self.btn_h, "Mode médiane", self.btn_taille_police, self.btn_couleur_texte, btn_couleur, self.fenetre)
        self.btn_mediane.dessiner()

        # Création du bouton "Mode majorité absolue"
        btn_majabs_y = btn_mediane_y + btn_espacement
        self.btn_majabs = Bouton(self.btn_x, btn_majabs_y, self.btn_l, self.btn_h, "Mode majorité absolue", self.btn_taille_police, self.btn_couleur_texte, btn_couleur, self.fenetre)
        self.btn_majabs.dessiner()

        # Création du bouton "Mode majorité relative"
        btn_majrel_y = btn_majabs_y + btn_espacement
        self.btn_majrel = Bouton(self.btn_x, btn_majrel_y, self.btn_l, self.btn_h, "Mode majorité relative", self.btn_taille_police, self.btn_couleur_texte, btn_couleur, self.fenetre)
        self.btn_majrel.dessiner()
        
        # Création du message de reprise de partie
        bt_reprendre_partie = BoiteTexte(fnt_accueil_l / 2, btn_majrel_y + 100, "Vous pouvez aussi reprendre la dernière partie enregistrée :", 25, (0, 0, 0), True, 40, self.fenetre)
        bt_reprendre_partie.dessiner()

        # Création du bouton "Reprendre la partie"
        self.btn_reprendre_partie_y = btn_majrel_y + 150
        self.btn_reprendre_partie = Bouton(self.btn_x, self.btn_reprendre_partie_y, self.btn_l, self.btn_h, "Reprendre la partie", self.btn_taille_police, self.btn_couleur_texte, btn_couleur, self.fenetre)
        self.btn_reprendre_partie.dessiner()

    def get_btn_strict(self):
        """
        Renvoie le bouton "Mode strict" de la fenêtre d'accueil.

        Renvoie:
            Bouton: Le bouton "Mode strict".
        """
        return self.btn_strict
    
    def get_btn_moyenne(self):
        """
        Renvoie le bouton "Mode moyenne" de la fenêtre d'accueil.

        Renvoie:
            Bouton: Le bouton "Mode moyenne".
        """
        return self.btn_moyenne
    
    def get_btn_mediane(self):
        """
        Renvoie le bouton "Mode mediane" de la fenêtre d'accueil.

        Renvoie:
            Bouton: Le bouton "Mode mediane".
        """
        return self.btn_mediane
    
    def get_btn_majabs(self):
        """
        Renvoie le bouton "Mode majorite absolue" de la fenêtre d'accueil.
        
        Renvoie:
            Bouton: Le bouton "Mode majorite absolue".
        """
        return self.btn_majabs
    
    def get_btn_majrel(self):
        """
        Renvoie le bouton "Mode majorite relative" de la fenêtre d'accueil.

        Renvoie:
            Bouton: Le bouton "Mode majorite relative".
        """
        return self.btn_majrel
    
    def get_btn_reprendre_partie(self):
        """
        Renvoie le bouton "Reprendre la partie" de la fenêtre d'accueil.

        Renvoie:
            Bouton: Le bouton "Reprendre la partie".
        """
        return self.btn_reprendre_partie
    
    def desactiver_btn_reprendre_partie(self):
        """
        Désactive le bouton "Reprendre la partie".

        Cette méthode change l'apparence du bouton pour le rendre inactif.
        """
        self.btn_reprendre_partie = Bouton(self.btn_x, self.btn_reprendre_partie_y, self.btn_l, self.btn_h, "Reprendre la partie", self.btn_taille_police, self.btn_couleur_texte, (125, 125, 125), self.fenetre)
        self.btn_reprendre_partie.dessiner()

    def afficher(self):
        """
        Affiche la fenêtre d'accueil.
        """
        super().afficher()
    
    def fermer(self):
        """
        Ferme la fenêtre d'accueil.
        """
        super().fermer()

class FntConfigJoueurs(Fenetre, Bouton, BoiteTexte, BoiteSaisie):
    """
    Classe représentant la fenêtre de configuration des joueurs.
    
    Cette fenêtre permet de configurer les différents joueurs du jeu.

    Attributs:
        fnt_config_joueurs_l (int): Largeur de la fenêtre.
        fnt_config_joueurs_h (int): Hauteur de la fenêtre.
        bs_joueurs (list): Liste des boîtes de saisie des noms de joueurs.
        bt_joueurs (list): Liste des étiquettes des noms de joueurs.
        bt_couleur (tuple): Couleur du texte des étiquettes.
        bs_couleur (tuple): Couleur du texte des boîtes de saisie.
        bt_taille_police (int): Taille de la police des étiquettes.
        bs_taille_police (int): Taille de la police des boîtes de saisie.
        bs_joueur_l (int): Largeur des boîtes de saisie des noms de joueurs.
        bs_joueur_h (int): Hauteur des boîtes de saisie des noms de joueurs.
        bs_joueur_x (float): Position en x des boîtes de saisie des noms de joueurs.
        bs_joueur_y (int): Position en y des boîtes de saisie des noms de joueurs.
        bs_joueur_max_caracteres (int): Nombre maximum de caractères dans les boîtes de saisie des noms de joueurs.
        btn_joueur_l (int): Largeur des boutons "Ajouter un joueur" et "Supprimer un joueur".
        btn_joueur_h (int): Hauteur des boutons "Ajouter un joueur" et "Supprimer un joueur".
        btn_ajouter_joueur_x (float): Position en x du bouton "Ajouter un joueur".
        btn_supprimer_joueur_x (float): Position en x du bouton "Supprimer un joueur".
        btn_joueur_y (int): Position en y des boutons "Ajouter un joueur" et "Supprimer un joueur".
        btn_valider (Bouton): Bouton "Valider".
        btn_retour (Bouton): Bouton "Retour".
    """

    def __init__(self):
        # Paramètres de la fenêtre
        self.fnt_config_joueurs_l = 450
        self.fnt_config_joueurs_h = 500
        super().__init__(self.fnt_config_joueurs_l, self.fnt_config_joueurs_h)
        self.set_titre("Planning Poker : Configuration des joueurs")
        self.set_couleur_fond((255, 255, 255))
        self.bs_joueurs = []
        self.bt_joueurs = []
        self.bt_couleur = (0, 0, 0)
        self.bs_couleur = (0, 0, 0)
        self.bt_taille_police = 25
        self.bs_taille_police = 30

        # Création des boîtes de saisie des noms de joueurs
        self.bs_joueur_l = 300
        self.bs_joueur_h = 30
        self.bs_joueur_x = (self.fnt_config_joueurs_l - self.bs_joueur_l) / 2
        self.bs_joueur_y = 100
        self.bs_joueur_max_caracteres = 15
        self.bs_joueurs = [BoiteSaisie(self.bs_joueur_x, self.bs_joueur_y, self.bs_joueur_l, self.bs_joueur_h, self.bs_taille_police, self.bs_couleur, self.bs_joueur_max_caracteres, 15, self.fenetre)]

        # Création d'un texte au-dessus de la boîte de saisie des noms de joueurs
        self.bt_joueur = BoiteTexte(self.bs_joueur_x + 10, self.bs_joueur_y - 20, "Nom du joueur n°1", self.bt_taille_police, self.bt_couleur, False, 17, self.fenetre)
        self.bt_joueur.dessiner()

        # Création du bouton "Ajouter un joueur" et "Supprimer un joueur"
        self.btn_joueur_l = 170
        self.btn_joueur_h = 30
        self.btn_ajouter_joueur_x = self.fnt_config_joueurs_l * 1.2 / 4 - self.btn_joueur_l / 2
        self.btn_supprimer_joueur_x = self.fnt_config_joueurs_l * 2.8 / 4 - self.btn_joueur_l / 2
        self.btn_joueur_y = 150

        # Création du bouton "Valider"
        btn_valider_l = 100
        btn_valider_h = 40
        btn_valider_x = (self.fnt_config_joueurs_l - btn_valider_l) / 2
        btn_valider_y = self.fnt_config_joueurs_h - 50
        self.btn_valider = Bouton(btn_valider_x, btn_valider_y, btn_valider_l, btn_valider_h, "Valider", 30, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_valider.dessiner()

        # Création du bouton "Retour"
        btn_retour_l = 40
        btn_retour_h = 40
        btn_retour_x = 10
        btn_retour_y = 10
        self.btn_retour = Bouton(btn_retour_x, btn_retour_y, btn_retour_l, btn_retour_h, "<", 30, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_retour.dessiner()

        # Création de la boîte de saisie 2
        self.ajouter_bs_joueur()
    
    def ajouter_bs_joueur(self):
        """
        Ajoute une boîte de saisie pour un nouveau joueur.

        Cette méthode crée une nouvelle boîte de saisie en dessous de la dernière, ainsi qu'une nouvelle étiquette correspondante.
        Elle met également à jour la position des boutons "Ajouter un joueur" et "Supprimer un joueur".
        """
        # Création d'une nouvelle boîte de saisie en dessous de la dernière
        derniere_bs_joueur = self.bs_joueurs[-1]
        nouvelle_bs_joueur = BoiteSaisie(derniere_bs_joueur.x, derniere_bs_joueur.y + 60, self.bs_joueur_l, self.bs_joueur_h, self.bs_taille_police, self.bs_couleur, self.bs_joueur_max_caracteres, 15, self.fenetre)
        self.bs_joueurs.append(nouvelle_bs_joueur)

        # Création de la nouvelle étiquette
        nouvelle_bt_joueur = BoiteTexte(self.bs_joueur_x + 10, derniere_bs_joueur.y + 40, f"Nom du joueur n°{len(self.bs_joueurs)}", self.bt_taille_police, self.bt_couleur, False, 17, self.fenetre)
        self.bt_joueurs.append(nouvelle_bt_joueur)

        # Faire descendre les boutons "Ajouter un joueur" et "Supprimer un joueur"
        ancien_y = self.btn_joueur_y
        self.btn_joueur_y += 60

        # Effacement des anciens boutons en dessinant un rectangle de la couleur de fond sur son ancienne position
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_ajouter_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_supprimer_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))
        
        # Affichage de la nouvelle boîte de saisie
        nouvelle_bt_joueur.dessiner()

        # Réaffichage de toutes les boîtes de saisie
        for bs_joueur in self.bs_joueurs:
            bs_joueur.dessiner()

        # Réaffichage du bouton "Ajouter un joueur"
        self.btn_ajouter_joueur = Bouton(self.btn_ajouter_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Ajouter un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_ajouter_joueur.dessiner()

        # Réaffichage du bouton "Supprimer un joueur"
        self.btn_supprimer_joueur = Bouton(self.btn_supprimer_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Supprimer un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_supprimer_joueur.dessiner()

        # Mise à jour de l'affichage
        pygame.display.flip()

    def supprimer_bs_joueur(self):
        """
        Supprime la dernière boîte de saisie et son étiquette correspondante.

        Cette méthode supprime la dernière boîte de saisie de la liste, ainsi que son étiquette correspondante.
        Elle met également à jour la position des boutons "Ajouter un joueur" et "Supprimer un joueur".
        """
        # Suppression de la dernière boîte de saisie et de la dernière étiquette
        derniere_bs_joueur = self.bs_joueurs.pop()
        derniere_bt_joueur = self.bt_joueurs.pop()

        # Faire monter le bouton "Ajouter un joueur" et "Supprimer un joueur" de 60 pixels
        ancien_y = self.btn_joueur_y
        self.btn_joueur_y -= 60

        # Effacement de l'ancienne boîte de saisie en dessinant un rectangle de la couleur de fond sur sa position
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(derniere_bs_joueur.x, derniere_bs_joueur.y, self.bs_joueur_l, self.bs_joueur_h))

        # Effacement de l'ancienne étiquette et des anciens boutons en dessinant un rectangle de la couleur de fond sur sa position
        bt_joueur_largeur, bt_joueur_hauteur = derniere_bt_joueur.get_taille()
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(derniere_bt_joueur.x, derniere_bt_joueur.y - 17, bt_joueur_largeur, bt_joueur_hauteur))
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_ajouter_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_supprimer_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))

        # Réaffichage du bouton "Ajouter un joueur"
        self.btn_ajouter_joueur = Bouton(self.btn_ajouter_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Ajouter un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_ajouter_joueur.dessiner()

        # Réaffichage du bouton "Supprimer un joueur"
        self.btn_supprimer_joueur = Bouton(self.btn_supprimer_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Supprimer un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_supprimer_joueur.dessiner()

        # Mise à jour de l'affichage
        pygame.display.flip()

    def get_bs_joueurs(self):
        """
        Renvoie la liste des boîtes de saisie des noms de joueurs.

        Renvoie:
            list: Liste des boîtes de saisie des noms de joueurs.
        """
        return self.bs_joueurs
    
    def get_btn_ajouter_joueur(self):
        """
        Renvoie le bouton "Ajouter un joueur".

        Renvoie:
            Bouton: Bouton "Ajouter un joueur".
        """
        return self.btn_ajouter_joueur
    
    def get_btn_supprimer_joueur(self):
        """
        Renvoie le bouton "Supprimer un joueur".

        Renvoie:
            Bouton: Bouton "Supprimer un joueur".
        """
        return self.btn_supprimer_joueur
    
    def desactiver_btn_ajouter_joueur(self):
        """
        Désactive le bouton "Ajouter un joueur".

        Cette méthode change l'apparence du bouton pour le rendre inactif.
        """
        self.btn_ajouter_joueur = Bouton(self.btn_ajouter_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Ajouter un joueur", 20, (255, 255, 255), (125, 125, 125), self.fenetre)
        self.btn_ajouter_joueur.dessiner()

    def desactiver_btn_supprimer_joueur(self):
        """
        Désactive le bouton "Supprimer un joueur".

        Cette méthode change l'apparence du bouton pour le rendre inactif.
        """
        self.btn_supprimer_joueur = Bouton(self.btn_supprimer_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Supprimer un joueur", 20, (255, 255, 255), (125, 125, 125), self.fenetre)
        self.btn_supprimer_joueur.dessiner()

    def get_btn_valider(self):
        """
        Renvoie le bouton "Valider".

        Renvoie:
            Bouton: Bouton "Valider".
        """
        return self.btn_valider
    
    def get_btn_retour(self):
        """
        Renvoie le bouton "Retour".

        Renvoie:
            Bouton: Bouton "Retour".
        """
        return self.btn_retour
    
    def afficher_msg_erreur(self, message):
        """
        Affiche un message d'erreur.

        Cette méthode affiche un message d'erreur au-dessus du bouton "Valider".

        Arguments:
            message (str): Message d'erreur à afficher.
        """
        bt_msg_erreur = BoiteTexte(self.fnt_config_joueurs_l / 2, self.get_btn_valider().y - 25, message, 20, (200, 0, 0), True, 51, self.fenetre)
        bt_msg_erreur.dessiner()

    def afficher(self):
        """
        Affiche la fenêtre.

        Cette méthode affiche la fenêtre avec tous ses éléments.
        """
        super().afficher()

    def fermer(self):
        """
        Ferme la fenêtre.

        Cette méthode ferme la fenêtre.
        """
        super().fermer()

class FntConfigTaches(Fenetre, Bouton, BoiteTexte, BoiteSaisie):
    """
    Classe représentant la fenêtre de configuration des tâches.

    Cette fenêtre permet de configurer les différentes tâches du planning poker.
    Elle contient des boîtes de saisie pour le titre et la description de chaque tâche,
    ainsi que des boutons pour enregistrer, valider et retourner à la fenêtre précédente.

    Attributs:
        fnt_config_taches_l (int): Largeur de la fenêtre.
        fnt_config_taches_h (int): Hauteur de la fenêtre.
        bs_titre (BoiteSaisie): Boîte de saisie du titre de la tâche.
        bt_titre (BoiteTexte): Texte au-dessus de la boîte de saisie du titre de la tâche.
        bs_description (BoiteSaisie): Boîte de saisie de la description de la tâche.
        bt_description (BoiteTexte): Texte au-dessus de la boîte de saisie de la description de la tâche.
        btn_enregistrer (Bouton): Bouton "Enregistrer cette tâche".
        btn_valider (Bouton): Bouton "Valider".
        btn_retour (Bouton): Bouton "Retour".
    """

    def __init__(self):
        # Paramètres généraux de la fenêtre
        self.fnt_config_taches_l = 450
        self.fnt_config_taches_h = 500
        super().__init__(self.fnt_config_taches_l, self.fnt_config_taches_h)
        self.set_titre("Planning Poker : Configuration des tâches")
        self.set_couleur_fond((255, 255, 255))
        self.bt_couleur = (0, 0, 0)
        bs_couleur = (0, 0, 0)
        self.bt_taille_police = 25
        bs_taille_police = 30

        # Création de la boite de saisie du titre de la tâche
        bs_titre_l = 380
        bs_titre_h = 30
        self.bs_titre_x = (self.fnt_config_taches_l - bs_titre_l) / 2
        self.bs_titre_y = 100
        bs_titre_max_caracteres = 20
        self.bs_titre = BoiteSaisie(self.bs_titre_x, self.bs_titre_y, bs_titre_l, bs_titre_h, bs_taille_police, bs_couleur, bs_titre_max_caracteres, 20, self.fenetre)
        self.bs_titre.dessiner()

        # Création d'un texte au-dessus de la boîte de saisie du titre
        self.bt_titre = BoiteTexte(self.bs_titre_x + 10, self.bs_titre_y - 20, "Titre de la tâche n°1", self.bt_taille_police, self.bt_couleur, False, 23, self.fenetre)
        self.bt_titre.dessiner()

        # Création de la boite de saisie de la description de la tâche
        bs_description_l = 380
        bs_description_h = 170
        self.bs_description_x = (self.fnt_config_taches_l - bs_description_l) / 2
        self.bs_description_y = 175
        bs_desription_max_caracteres = 160
        self.bs_description = BoiteSaisie(self.bs_description_x, self.bs_description_y, bs_description_l, bs_description_h, bs_taille_police, bs_couleur, bs_desription_max_caracteres, 20, self.fenetre)
        self.bs_description.dessiner()

        # Création d'un texte au-dessus de la description de la tâche
        self.bt_description = BoiteTexte(self.bs_description_x + 10, self.bs_description_y - 20, "Description de la tâche n°1", self.bt_taille_police, self.bt_couleur, False, 29, self.fenetre)
        self.bt_description.dessiner()

        # Création du bouton "Enregistrer cette tâche"
        btn_enregistrer_l = 170
        btn_enregistrer_h = 30
        btn_enregistrer_x = (self.fnt_config_taches_l - btn_enregistrer_l) / 2
        btn_enregistrer_y = self.fnt_config_taches_h - 140
        self.btn_enregistrer = Bouton(btn_enregistrer_x, btn_enregistrer_y, btn_enregistrer_l, btn_enregistrer_h, "Enregistrer cette tâche", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_enregistrer.dessiner()

        # Création du bouton "Valider"
        btn_valider_l = 100
        btn_valider_h = 40
        btn_valider_x = (self.fnt_config_taches_l - btn_valider_l) / 2
        btn_valider_y = self.fnt_config_taches_h - 50
        self.btn_valider = Bouton(btn_valider_x, btn_valider_y, btn_valider_l, btn_valider_h, "Valider", 30, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_valider.dessiner()

        # Création du bouton "Retour"
        btn_retour_l = 40
        btn_retour_h = 40
        btn_retour_x = 10
        btn_retour_y = 10
        self.btn_retour = Bouton(btn_retour_x, btn_retour_y, btn_retour_l, btn_retour_h, "<", 30, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_retour.dessiner()

    def get_bs_titre(self):
        """
        Méthode pour récupérer la boîte de saisie du titre de la tâche.

        Renvoie:
            BoiteSaisie: La boîte de saisie du titre de la tâche.
        """
        return self.bs_titre
    
    def get_bs_description(self):
        """
        Méthode pour récupérer la boîte de saisie de la description de la tâche.

        Renvoie:
            BoiteSaisie: La boîte de saisie de la description de la tâche.
        """
        return self.bs_description

    def get_btn_enregistrer(self):
        """
        Méthode pour récupérer le bouton "Enregistrer cette tâche".

        Renvoie:
            Bouton: Le bouton "Enregistrer cette tâche".
        """
        return self.btn_enregistrer

    def get_btn_valider(self):
        """
        Méthode pour récupérer le bouton "Valider".

        Renvoie:
            Bouton: Le bouton "Valider".
        """
        return self.btn_valider
    
    def get_btn_retour(self):
        """
        Méthode pour récupérer le bouton "Retour".

        Renvoie:
            Bouton: Le bouton "Retour".
        """
        return self.btn_retour
    
    def actualiser_bt_titre(self, nb_taches):
        """
        Méthode pour actualiser le texte de la boîte de saisie du titre.

        Arguments:
            nb_taches (int): Le numéro de la tâche.
        """
        self.bt_titre.reset_texte()
        self.bt_titre = BoiteTexte(self.bs_titre_x + 10, self.bs_titre_y - 20, f"Titre de la tâche n°{nb_taches}", self.bt_taille_police, self.bt_couleur, False, 23, self.fenetre)
        self.bt_titre.dessiner()

    def actualiser_bt_description(self, nb_taches):
        """
        Méthode pour actualiser le texte de la boîte de saisie de la description.

        Arguments:
            nb_taches (int): Le numéro de la tâche.
        """
        self.bt_description.reset_texte()
        self.bt_description = BoiteTexte(self.bs_description_x + 10, self.bs_description_y - 20, f"Description de la tâche n°{nb_taches}", self.bt_taille_police, self.bt_couleur, False, 29, self.fenetre)
        self.bt_description.dessiner()
    
    def reset_bs(self):
        """
        Méthode pour réinitialiser les boîtes de saisie.
        """
        self.bs_titre.reset_texte()
        self.bs_description.reset_texte()
        pygame.display.flip()

    def afficher_msg_erreur(self, message):
        """
        Méthode pour afficher un message d'erreur.

        Arguments:
            message (str): Le message d'erreur à afficher.
        """
        Rectangle(30, self.get_btn_valider().y - 30, 400, 25, (255, 255, 255), (255, 255, 255), self.fenetre).dessiner()
        bt_msg_erreur = BoiteTexte(self.fnt_config_taches_l / 2, self.get_btn_valider().y - 25, message, 20, (200, 0, 0), True, 60, self.fenetre)
        bt_msg_erreur.dessiner()

    def afficher(self):
        """
        Méthode pour afficher la fenêtre.
        """
        super().afficher()

    def fermer(self):
        """
        Méthode pour fermer la fenêtre.
        """
        super().fermer()
        
class FntJeu(Fenetre, Rectangle, Bouton, BoiteTexte, BoiteSaisie, Cartes):
    """
    Classe représentant la fenêtre de jeu.
    
    Cette fenêtre affiche les informations utiles au bon déroulement du jeu, le plateau de carte, ainsi que les logs et le chat.
    
    Attributs:
        ecran (pygame.Surface): L'écran sur lequel s'affiche la fenêtre.
        ecran_l (int): Largeur de l'écran.
        ecran_h (int): Hauteur de l'écran.
        rect_marge (int): Marge entre les rectangles.
        rect_l (int): Largeur des rectangles.
        rect_h (int): Hauteur des rectangles.
        logs (list): Liste des logs.
        bt_texte_logs (BoiteTexte): Boîte de texte pour les logs.
        noms_cartes (list): Liste des noms des cartes.
        liste_cartes (list): Liste des cartes.
        btn_quitter (Bouton): Bouton pour quitter la partie.
    """
    def __init__(self, mode_jeu, tache, joueur):
        # Paramètres de la fenêtre
        super().__init__(0, 0)
        self.ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.ecran_l, self.ecran_h = self.ecran.get_size()
        self.set_titre("Planning Poker : Plateau de jeu")
        self.set_couleur_fond((255, 255, 255))
        self.mode_jeu = mode_jeu
        self.logs = []

        # Affichage du mode de jeu
        bt_mode_jeu = BoiteTexte(self.ecran_l / 3 * 2, self.ecran_h / 10, f"Mode de jeu : {self.mode_jeu}", 40, (0, 0, 0), True, 100, self.ecran)
        bt_mode_jeu.dessiner()

        # Création des rectangles de logs et de chat
        self.rect_marge = 20
        self.rect_l = self.ecran_l / 3 - 2 * self.rect_marge
        self.rect_h = self.ecran_h / 2 - 1.5 * self.rect_marge
        rect_logs = Rectangle(self.rect_marge, self.rect_marge, self.rect_l, self.rect_h, (255, 255, 255), (0, 0, 0), self.ecran)
        rect_chat = Rectangle(self.rect_marge, self.rect_h + 2 * self.rect_marge, self.rect_l, self.rect_h, (255, 255, 255), (0, 0, 0), self.ecran)
        rect_logs.dessiner()
        rect_chat.dessiner()

        # Création des titres des rectangles de logs et de chat
        bt_titre_logs = BoiteTexte(self.rect_marge + self.rect_l / 2, self.rect_marge + 10, "Logs", 30, (0, 0, 0), True, 4, self.ecran)
        bt_titre_chat = BoiteTexte(self.rect_marge + self.rect_l / 2, self.rect_h + 2 * self.rect_marge + 10, "Chat", 30, (0, 0, 0), True, 4, self.ecran)
        bt_titre_logs.dessiner()
        bt_titre_chat.dessiner()

        # Création de la boîte de texte des logs
        self.bt_texte_logs = BoiteTexte(self.rect_marge + 10, self.rect_marge + 40, "", 30, (0, 0, 0), False, 100, self.ecran)

        # Afffichage des éléments de la fenêtre de jeu
        self.affichage_tache(tache)
        self.affichage_joueur(joueur)
        self.plateau_cartes()

        # Création du bouton "Quitter la partie"
        btn_quitter_l = 200
        btn_quitter_h = 40
        btn_quitter_x = (self.ecran_l - btn_quitter_l) - 10
        btn_quitter_y = 10
        self.btn_quitter = Bouton(btn_quitter_x, btn_quitter_y, btn_quitter_l, btn_quitter_h, "Quitter la partie", 30, (255, 255, 255), (200, 0, 0), self.fenetre)
        self.btn_quitter.dessiner()
    
    def log_debut_partie(self):
        """
        Méthode de log pour le début de la partie.
        """
        self.ajouter_log("Début de la partie")

    def log_fin_partie(self):
        """
        Méthode de log pour la fin de la partie.
        """
        self.ajouter_log("Fin de la partie")
    
    def log_tour_joueur(self, joueur):
        """
        Méthode de log pour annoncer le tour d'un joueur.
        """
        self.ajouter_log(f"C'est au tour du joueur n°{joueur.numero} de jouer")

    def log_choix_carte(self, joueur):
        """
        Méthode de log pour le choix d'une carte par un joueur.
        """
        self.ajouter_log(f"Le joueur n°{joueur.numero} a choisi une carte")

    def log_cartes_choisies(self, joueur, carte):
        """
        Méthode de log pour le résultat d'un tour.
        """
        self.ajouter_log(f"Le joueur n°{joueur.numero} a choisi la carte {carte}")

    def ajouter_log(self, texte):
        """
        Ajoute un log.
        
        Cette méthode ajoute un log à la liste des logs, et met à jour la boîte de texte des logs.
        
        Arguments:
            texte (str): Le texte à ajouter au log.
            
        Renvoie:
            list: Liste des logs.
        """
        # Obtention de l'heure actuelle
        heure = datetime.now().strftime('%H:%M:%S')
        # Ajout du texte au début du log existant
        self.logs.insert(0, f"[{heure}] : {texte}")
        # Si la liste des logs dépasse 15, supprimer le log le plus ancien
        if len(self.logs) > 15:
            self.logs.pop()
        
        # Effacement de l'ancienne zone de texte
        self.bt_texte_logs.reset_texte()
        self.bt_texte_logs.set_texte("\n".join(self.logs))
        self.bt_texte_logs.dessiner()

    def affichage_tache(self, tache):
        """
        Affiche la tâche en cours.
        
        Cette méthode affiche la tâche en cours dans la boîte de texte des logs.
        
        Arguments:
            tache (Tache): La tâche en cours.
            
        Renvoie:
            Tache: La tâche en cours.
        """
        # Calcul des coordonnées pour l'affichage des tâches
        x = self.ecran_l / 3 * 2
        y = self.ecran_h / 5

        Rectangle(self.ecran_l / 5 * 1.95, y - 10, 800, 260, (255, 255, 255), (255, 255, 255), self.fenetre).dessiner()

        # Création d'une boîte de texte pour le titre
        bt_titre_tache = BoiteTexte(x, y, f"Titre de la tâche n°{tache.numero} : {tache.titre}", 40, (0, 0, 0), True, 46, self.ecran)

        # Création d'une boîte de texte pour la description
        bt_description_tache = BoiteTexte(x, y + 50, f"Description de la tâche n°{tache.numero} : {tache.description}", 40, (0, 0, 0), True, 30, self.ecran)

        # Affichage des boîtes de texte
        bt_titre_tache.dessiner()
        bt_description_tache.dessiner()

        # Mise à jour de l'affichage
        pygame.display.flip()

    def affichage_joueur(self, joueur):
        """
        Affiche le joueur en cours.
        
        Cette méthode affiche le joueur en cours dans la boîte de texte des logs.
        
        Arguments:
            joueur (Joueur): Le joueur en cours.
            
        Renvoie:
            Joueur: Le joueur en cours.
        """
        # Calcul des coordonnées pour l'affichage du joueur
        x = self.ecran_l / 3 * 2
        y = self.ecran_h / 2

        Rectangle(self.ecran_l / 5 * 1.95, y - 10, 800, 45, (255, 255, 255), (255, 255, 255), self.fenetre).dessiner()

        # Création d'une boîte de texte pour le nom du joueur
        bt_nom_joueur = BoiteTexte(x, y, f"C'est au tour de {joueur.nom} de jouer", 40, (0, 0, 0), True, 46, self.ecran)

        # Affichage de la boîte de texte
        bt_nom_joueur.dessiner()

        # Mise à jour de l'affichage
        pygame.display.flip()

    def affichage_fin_jeu(self, option):
        """
        Affiche la fin du jeu.

        Arguments:
            option (str): L'option d'affichage.
        
        Cette méthode affiche la fin du jeu dans la boîte de texte des logs.
        """
        # Calcul des coordonnées pour l'affichage de la fin du jeu
        x = self.ecran_l / 3 * 2
        y = self.ecran_h / 4

        Rectangle(self.ecran_l / 5 * 1.95, self.ecran_h / 10, 800, 400, (255, 255, 255), (255, 255, 255), self.fenetre).dessiner()

        # Création d'une boîte de texte pour la fin du jeu
        if option == 1:
            bt_fin_jeu = BoiteTexte(x, y, "Toutes les tâches ont été traitées. La partie est terminée et sauvegardée avec succès, vous pouvez quitter le jeu.", 40, (0, 0, 0), True, 50, self.ecran)
        elif option == 2:
            bt_fin_jeu = BoiteTexte(x, y, "Tous les joueurs ont choisi la carte café. La partie est mise en pause et sauvegardée avec succès, vous pouvez quitter le jeu.", 40, (0, 0, 0), True, 50, self.ecran)

        # Affichage de la boîte de texte
        bt_fin_jeu.dessiner()

        # Mise à jour de l'affichage
        pygame.display.flip()

    def plateau_cartes(self):
        """
        Affiche le plateau de cartes.
        
        Cette méthode affiche le plateau de cartes dans la fenêtre.
        
        Renvoie:
            list: Liste des cartes.
        """
        # Définition de la taille et l'espacement des cartes
        taille_carte = (self.ecran_l // 11, self.ecran_h // 5)
        espacement = 20
        marge = 20

        # Calcul de la position de départ du plateau de cartes
        x_debut = self.ecran_l - (6 * taille_carte[0] + 5 * espacement) - marge
        y_debut = self.ecran_h - (2 * taille_carte[1] + espacement) - marge

        # Création de la liste de noms des cartes
        self.noms_cartes = ['0', '1', '2', '3', '5', '8', '13', '20', '40', '100', 'interro', 'cafe']

        # Affichage des cartes
        self.liste_cartes = []
        for i, nom_carte in enumerate(self.noms_cartes):
            x = x_debut + (i % 6) * (taille_carte[0] + espacement)
            y = y_debut + (i // 6) * (taille_carte[1] + espacement)

            carte = Cartes(nom_carte, (x, y), self.fenetre, taille_carte)
            self.liste_cartes.append(carte)
        
        for carte in self.liste_cartes:
            carte.afficher()

        # Mise à jour de l'affichage
        pygame.display.flip()

    def get_cartes(self):
        """
        Renvoie la liste des cartes.

        Renvoie:
            list: Liste des cartes.
        """
        return self.liste_cartes
    
    def get_btn_quitter(self):
        """
        Renvoie le bouton "Quitter la partie".
        
        Renvoie:
            Bouton: Le bouton "Quitter la partie".
        """
        return self.btn_quitter

    def afficher(self):
        """
        Affiche la fenêtre.
        """
        super().afficher()

    def fermer(self):
        """
        Ferme la fenêtre.
        """
        super().fermer()