from jeu import Joueur

import sys    # Importation du module sys pour accéder aux fonctionnalités système de Python
import pygame # Importation de la bibliothèque Pygame pour créer des jeux et des applications multimédias

# Initialisation de toutes les bibliothèques Pygame et leurs modules associés
pygame.init()
pygame.font.init()

class Fenetre:
    # Méthode pour initialiser la fenêtre
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))

    # Méthode pour définir le titre de la fenêtre
    def set_titre(self, titre):
        pygame.display.set_caption(titre)
    
    # Méthode pour définir la couleur de fond de la fenêtre
    def set_couleur_fond(self, couleur):
        self.fenetre.fill(couleur)

    # Méthode pour afficher/mettre à jour la fenêtre
    def afficher(self):
        pygame.display.flip()
    
    # Méthode pour fermer la fenêtre
    def fermer(self):
        pygame.display.quit()

class Bouton:
    # Méthode pour initialiser un bouton
    def __init__(self, x, y, largeur, hauteur, couleur, texte):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.texte = texte

    # Méthode pour dessiner un bouton
    def dessiner(self, fenetre, taille_police, couleur_texte):
        rayon = self.hauteur // 2
        pygame.draw.ellipse(fenetre, self.couleur, (self.x, self.y, 2*rayon, 2*rayon))  # Coin supérieur gauche
        pygame.draw.ellipse(fenetre, self.couleur, (self.x + self.largeur - 2*rayon, self.y, 2*rayon, 2*rayon))  # Coin supérieur droit
        pygame.draw.ellipse(fenetre, self.couleur, (self.x, self.y + self.hauteur - 2*rayon, 2*rayon, 2*rayon))  # Coin inférieur gauche
        pygame.draw.ellipse(fenetre, self.couleur, (self.x + self.largeur - 2*rayon, self.y + self.hauteur - 2*rayon, 2*rayon, 2*rayon))  # Coin inférieur droit
        pygame.draw.rect(fenetre, self.couleur, (self.x, self.y + rayon, self.largeur, self.hauteur - 2*rayon))  # Partie centrale verticale
        pygame.draw.rect(fenetre, self.couleur, (self.x + rayon, self.y, self.largeur - 2*rayon, self.hauteur))  # Partie centrale horizontale

        police = pygame.font.Font(None, taille_police)
        texte = police.render(self.texte, True, couleur_texte)
        fenetre.blit(texte, (self.x + (self.largeur - texte.get_width()) // 2, self.y + (self.hauteur - texte.get_height()) // 2))
    
    # Méthode pour vérifier si un bouton est survolé
    def est_survole(self, souris_x, souris_y):
        if self.x <= souris_x <= self.x + self.largeur and self.y <= souris_y <= self.y + self.hauteur:
            return True
        else:
            return False

    # Méthode pour vérifier si un bouton est cliqué
    def est_clique(self, x, y):
        return self.x <= x <= self.x + self.largeur and self.y <= y <= self.y + self.hauteur
    
class BoiteSaisie:
    # Méthode pour initialiser une boîte de saisie
    def __init__(self, x, y, largeur, hauteur, taille_police, couleur, texte=''):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.couleur = couleur
        self.texte = texte
        self.police = pygame.font.Font(None, taille_police)
        self.texte_surface = self.police.render(self.texte, True, self.couleur) 
        self.taille_max = 15

    # Méthode pour gérer les événements
    def evenement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(self.texte)
                self.texte = ''
            elif event.key == pygame.K_BACKSPACE:
                self.texte = self.texte[:-1]
            else:
                if len(self.texte) < self.taille_max:
                    self.texte += event.unicode
            self.texte_surface = self.police.render(self.texte, True, self.couleur)

    # Méthode pour dessiner une boîte de saisie
    def dessiner(self, fenetre):
        fenetre.blit(self.texte_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(fenetre, self.couleur, self.rect, 2)

    # Méthode pour récupérer le texte d'une boîte de saisie
    def get_texte(self):
        return self.texte
    
class FntAccueil(Fenetre, Bouton):
    def __init__(self):
        # Paramètres de la fenêtre
        fnt_accueil_l = 400
        fnt_accueil_h = 300
        super().__init__(fnt_accueil_l, fnt_accueil_h)
        self.set_titre("Planning Poker : Accueil")
        self.set_couleur_fond((255, 255, 255))

        # Création du bouton "Lancer une partie"
        btn_lancer_l = 250
        btn_lancer_h = 50
        btn_lancer_x = (fnt_accueil_l - btn_lancer_l) / 2
        btn_lancer_y = (fnt_accueil_h - btn_lancer_h) / 2
        self.btn_lancer = Bouton(btn_lancer_x, btn_lancer_y, btn_lancer_l, btn_lancer_h, (0, 0, 0), "Lancer une partie")
        self.btn_lancer.dessiner(self.fenetre, 30, (255, 255, 255))

    # Méthode pour récupérer le bouton "Lancer une partie"
    def get_btn_lancer(self):
        return self.btn_lancer
    
    # Méthode pour afficher la fenêtre
    def afficher(self):
        super().afficher()
    
    # Méthode pour fermer la fenêtre
    def fermer(self):
        super().fermer()

class FntConfigJoueurs(Fenetre, Bouton, BoiteSaisie):
    def __init__(self):
        # Paramètres de la fenêtre
        fnt_config_joueurs_l = 400
        fnt_config_joueurs_h = 700
        super().__init__(fnt_config_joueurs_l, fnt_config_joueurs_h)
        self.set_titre("Planning Poker : Configuration des joueurs")
        self.set_couleur_fond((255, 255, 255))

        # Création de deux boîtes de saisie
        boite_saisie_l = 200
        boite_saisie_h = 32
        boite_saisie_x = (fnt_config_joueurs_l - boite_saisie_l) / 2
        self.boite_saisie1 = BoiteSaisie(boite_saisie_x, 100, boite_saisie_l, boite_saisie_h, 32, (0, 0, 0))
        self.boite_saisie1.dessiner(self.fenetre)
        self.boite_saisie2 = BoiteSaisie(boite_saisie_x, 150, boite_saisie_l, boite_saisie_h, 32, (0, 0, 0))
        self.boite_saisie2.dessiner(self.fenetre)

        # Création du bouton "Ajouter un joueur"
        btn_ajouter_joueur_l = 200
        btn_ajouter_joueur_h = 40
        btn_ajouter_joueur_x = (fnt_config_joueurs_l - btn_ajouter_joueur_l) / 2
        btn_ajouter_joueur_y = 200
        self.btn_ajouter_joueur = Bouton(btn_ajouter_joueur_x, btn_ajouter_joueur_y, btn_ajouter_joueur_l, btn_ajouter_joueur_h, (0, 0, 0), "Ajouter un joueur")
        self.btn_ajouter_joueur.dessiner(self.fenetre, 30, (255, 255, 255))

        # Création du bouton "Valider"
        btn_valider_l = 100
        btn_valider_h = 40
        btn_valider_x = (fnt_config_joueurs_l - btn_valider_l) / 2
        btn_valider_y = fnt_config_joueurs_h - 50
        self.btn_valider = Bouton(btn_valider_x, btn_valider_y, btn_valider_l, btn_valider_h, (0, 0, 0), "Valider")
        self.btn_valider.dessiner(self.fenetre, 30, (255, 255, 255))

        # Création du bouton "Retour"
        btn_retour_l = 40
        btn_retour_h = 40
        btn_retour_x = 10
        btn_retour_y = 10
        self.btn_retour = Bouton(btn_retour_x, btn_retour_y, btn_retour_l, btn_retour_h, (0, 0, 0), "<")
        self.btn_retour.dessiner(self.fenetre, 30, (255, 255, 255))

    # Méthode pour récupérer la boîte de saisie 1
    def get_boite_saisie1(self):
        return self.boite_saisie1
    
    # Méthode pour récupérer la boîte de saisie 2
    def get_boite_saisie2(self):
        return self.boite_saisie2
    
    # Méthode pour récupérer le bouton "Ajouter un joueur"
    def get_btn_ajouter_joueur(self):
        return self.btn_ajouter_joueur

    # Méthode pour récupérer le bouton "Valider"
    def get_btn_valider(self):
        return self.btn_valider
    
    # Méthode pour récupérer le bouton "Retour"
    def get_btn_retour(self):
        return self.btn_retour

    # Méthode pour afficher la fenêtre
    def afficher(self):
        super().afficher()

    # Méthode pour fermer la fenêtre
    def fermer(self):
        super().fermer()

class FntConfigTaches(Fenetre, Bouton):
    def __init__(self):
        # Paramètres de la fenêtre
        fnt_config_taches_l = 400
        fnt_config_taches_h = 700
        super().__init__(fnt_config_taches_l, fnt_config_taches_h)
        self.set_titre("Planning Poker : Configuration des tâches")
        self.set_couleur_fond((255, 255, 255))

        # Création du bouton "Valider"
        btn_valider_l = 100
        btn_valider_h = 40
        btn_valider_x = (fnt_config_taches_l - btn_valider_l) / 2
        btn_valider_y = fnt_config_taches_h - 50
        self.btn_valider = Bouton(btn_valider_x, btn_valider_y, btn_valider_l, btn_valider_h, (0, 0, 0), "Valider")
        self.btn_valider.dessiner(self.fenetre, 30, (255, 255, 255))

        # Création du bouton "Retour"
        btn_retour_l = 40
        btn_retour_h = 40
        btn_retour_x = 10
        btn_retour_y = 10
        self.btn_retour = Bouton(btn_retour_x, btn_retour_y, btn_retour_l, btn_retour_h, (0, 0, 0), "<")
        self.btn_retour.dessiner(self.fenetre, 30, (255, 255, 255))

    # Méthode pour récupérer le bouton "Valider"
    def get_btn_valider(self):
        return self.btn_valider
    
    # Méthode pour récupérer le bouton "Retour"
    def get_btn_retour(self):
        return self.btn_retour

    # Méthode pour afficher la fenêtre
    def afficher(self):
        super().afficher()

    # Méthode pour fermer la fenêtre
    def fermer(self):
        super().fermer()

class FntJeu(Fenetre, Bouton):
    def __init__(self):
        # Paramètres de la fenêtre
        super().__init__(0, 0)
        self.ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        ecran_l, ecran_h = self.ecran.get_size() # Récupération de la taille de l'écran
        self.set_titre("Planning Poker : Plateau de jeu")
        self.set_couleur_fond((255, 255, 255))

        # Création du bouton "Quitter la partie"
        btn_quitter_l = 200
        btn_quitter_h = 40
        btn_quitter_x = (ecran_l - btn_quitter_l) - 10 # Calcul de la coordonnée x du bouton
        btn_quitter_y = 10
        self.btn_quitter = Bouton(btn_quitter_x, btn_quitter_y, btn_quitter_l, btn_quitter_h, (200, 0, 0), "Quitter la partie")
        self.btn_quitter.dessiner(self.fenetre, 30, (255, 255, 255))
    
    # Méthode pour récupérer le bouton "Quitter la partie"
    def get_btn_quitter(self):
        return self.btn_quitter

    # Méthode pour afficher la fenêtre
    def afficher(self):
        super().afficher()

    # Méthode pour fermer la fenêtre
    def fermer(self):
        super().fermer()