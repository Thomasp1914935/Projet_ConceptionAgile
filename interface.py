import pygame

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
    def __init__(self, x, y, largeur, hauteur, taille_police, couleur, max_caracteres, fenetre):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.couleur = couleur
        self.police = pygame.font.Font(None, taille_police)
        self.texte = ""
        self.max_caracteres = max_caracteres
        self.fenetre = fenetre
        self.selectionnee = False

    # Méthode pour dessiner une boîte de saisie
    def dessiner(self):
        pygame.draw.rect(self.fenetre, (255, 255, 255), self.rect)
        pygame.draw.rect(self.fenetre, self.couleur, self.rect, 2)
        texte_surface = self.police.render(self.texte, True, self.couleur)
        self.fenetre.blit(texte_surface, (self.rect.x + 5, self.rect.y + 5))

    # Méthode pour vérifier si une boîte de saisie est cliquée
    def evenement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.texte = self.texte[:-1]
            else:
                if len(self.texte) < self.max_caracteres:
                    self.texte += event.unicode
        self.dessiner()

    # Méthode pour vérifier si un bouton est survolé
    def est_survole(self, souris_x, souris_y):
        if self.x <= souris_x <= self.x + self.largeur and self.y <= souris_y <= self.y + self.hauteur:
            return True
        else:
            return False

    # Méthode pour vérifier si une boîte de saisie est cliquée
    def est_clique(self, x, y):
        return self.x <= x <= self.x + self.largeur and self.y <= y <= self.y + self.hauteur

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
        self.fnt_config_joueurs_l = 400
        self.fnt_config_joueurs_h = 700
        super().__init__(self.fnt_config_joueurs_l, self.fnt_config_joueurs_h)
        self.set_titre("Planning Poker : Configuration des joueurs")
        self.set_couleur_fond((255, 255, 255))
        self.boites_saisie = []

        # Création de la boîte de saisie
        self.boite_saisie_l = 250
        self.boite_saisie_h = 32
        self.boite_saisie_x = (self.fnt_config_joueurs_l - self.boite_saisie_l) / 2
        self.boite_saisie_y = 100
        self.taille_police = 30
        self.couleur = (0, 0, 0)
        self.max_caracteres = 15
        self.boites_saisie = [BoiteSaisie(self.boite_saisie_x, self.boite_saisie_y, self.boite_saisie_l, self.boite_saisie_h, self.taille_police, self.couleur, self.max_caracteres, self.fenetre)] # Liste des boîtes de saisie

        # Création du bouton "Ajouter un joueur" et "Supprimer un joueur"
        self.btn_joueur_l = 150
        self.btn_joueur_h = 30
        self.btn_ajouter_joueur_x = self.fnt_config_joueurs_l * 1.2 / 4 - self.btn_joueur_l / 2
        self.btn_supprimer_joueur_x = self.fnt_config_joueurs_l * 2.8 / 4 - self.btn_joueur_l / 2
        self.btn_joueur_y = 150

        # Création du bouton "Valider"
        btn_valider_l = 100
        btn_valider_h = 40
        btn_valider_x = (self.fnt_config_joueurs_l - btn_valider_l) / 2
        btn_valider_y = self.fnt_config_joueurs_h - 50
        self.btn_valider = Bouton(btn_valider_x, btn_valider_y, btn_valider_l, btn_valider_h, (0, 0, 0), "Valider")
        self.btn_valider.dessiner(self.fenetre, 30, (255, 255, 255))

        # Création du bouton "Retour"
        btn_retour_l = 40
        btn_retour_h = 40
        btn_retour_x = 10
        btn_retour_y = 10
        self.btn_retour = Bouton(btn_retour_x, btn_retour_y, btn_retour_l, btn_retour_h, (0, 0, 0), "<")
        self.btn_retour.dessiner(self.fenetre, 30, (255, 255, 255))

        # Création de la boîte de saisie 2
        self.ajouter_boite_saisie()
    
    # Méthode pour ajouter une boîte de saisie
    def ajouter_boite_saisie(self):
        # Créer une nouvelle boîte de saisie en dessous de la dernière
        derniere_boite = self.boites_saisie[-1]
        nouvelle_boite = BoiteSaisie(derniere_boite.x, derniere_boite.y + 50, self.boite_saisie_l, self.boite_saisie_h, self.taille_police, self.couleur, self.max_caracteres, self.fenetre)
        self.boites_saisie.append(nouvelle_boite)

        # Faire descendre les boutons "Ajouter un joueur" et "Supprimer un joueur" de 50 pixels
        ancien_y = self.btn_joueur_y
        self.btn_joueur_y += 50

        # Effacer l'ancien bouton en dessinant un rectangle de la couleur de fond sur son ancienne position
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_ajouter_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))

        # Effacer l'ancien bouton en dessinant un rectangle de la couleur de fond sur son ancienne position
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_supprimer_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))

        # Redessiner toutes les boîtes de saisie
        for boite in self.boites_saisie:
            boite.dessiner()

        # Redessiner le bouton "Ajouter un joueur"
        self.btn_ajouter_joueur = Bouton(self.btn_ajouter_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, (0, 0, 0), "Ajouter un joueur")
        self.btn_ajouter_joueur.dessiner(self.fenetre, 20, (255, 255, 255))

        # Redessiner le bouton "Supprimer un joueur"
        self.btn_supprimer_joueur = Bouton(self.btn_supprimer_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, (0, 0, 0), "Supprimer un joueur")
        self.btn_supprimer_joueur.dessiner(self.fenetre, 20, (255, 255, 255))

        # Mettre à jour l'affichage
        pygame.display.flip()

    # Méthode pour supprimer une boîte de saisie
    def supprimer_boite_saisie(self):
        # Supprimer la dernière boîte de saisie
        derniere_boite = self.boites_saisie.pop()

        # Faire monter le bouton "Ajouter un joueur" et "Supprimer un joueur" de 50 pixels
        ancien_y = self.btn_joueur_y
        self.btn_joueur_y -= 50

        # Effacer l'ancienne boîte de saisie en dessinant un rectangle de la couleur de fond sur sa position
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(derniere_boite.x, derniere_boite.y, self.boite_saisie_l, self.boite_saisie_h))

        # Effacer l'ancien bouton en dessinant un rectangle de la couleur de fond sur son ancienne position
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_ajouter_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))

        # Effacer l'ancien bouton en dessinant un rectangle de la couleur de fond sur son ancienne position
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_supprimer_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))

        # Redessiner toutes les boîtes de saisie
        for boite in self.boites_saisie:
            boite.dessiner()

        # Redessiner le bouton "Ajouter un joueur"
        self.btn_ajouter_joueur = Bouton(self.btn_ajouter_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, (0, 0, 0), "Ajouter un joueur")
        self.btn_ajouter_joueur.dessiner(self.fenetre, 20, (255, 255, 255))

        # Redessiner le bouton "Supprimer un joueur"
        self.btn_supprimer_joueur = Bouton(self.btn_supprimer_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, (0, 0, 0), "Supprimer un joueur")
        self.btn_supprimer_joueur.dessiner(self.fenetre, 20, (255, 255, 255))

        # Mettre à jour l'affichage
        pygame.display.flip()

    def get_boites_saisie(self):
        return self.boites_saisie
    
    # Méthode pour récupérer le bouton "Ajouter un joueur"
    def get_btn_ajouter_joueur(self):
        return self.btn_ajouter_joueur
    
    # Méthode pour récupérer le bouton "Supprimer un joueur"
    def get_btn_supprimer_joueur(self):
        return self.btn_supprimer_joueur
    
    # Méthode pour désactiver le bouton "Ajouter un joueur"
    def desactiver_btn_ajouter_joueur(self):
        self.btn_ajouter_joueur = Bouton(self.btn_ajouter_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, (125, 125, 125), "Ajouter un joueur")
        self.btn_ajouter_joueur.dessiner(self.fenetre, 20, (255, 255, 255))

    # Méthode pour désactiver le bouton "Supprimer un joueur"
    def desactiver_btn_supprimer_joueur(self):
        self.btn_supprimer_joueur = Bouton(self.btn_supprimer_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, (125, 125, 125), "Supprimer un joueur")
        self.btn_supprimer_joueur.dessiner(self.fenetre, 20, (255, 255, 255))

    # Méthode pour récupérer le bouton "Valider"
    def get_btn_valider(self):
        return self.btn_valider
    
    # Méthode pour récupérer le bouton "Retour"
    def get_btn_retour(self):
        return self.btn_retour
    
    # Méthode pour afficher un message d'erreur
    def afficher_message_erreur(self, message):
        font = pygame.font.Font(None, 20)
        text = font.render(message, True, (200, 0, 0))
        text_rect = text.get_rect(center=(self.fnt_config_joueurs_l / 2, self.get_btn_valider().y - 20))
        self.fenetre.blit(text, text_rect)
        pygame.display.flip()

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