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
    def __init__(self, x, y, largeur, hauteur, texte, taille_police, couleur_texte, couleur_bouton, fenetre):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.texte = texte
        self.taille_police = taille_police
        self.couleur_texte = couleur_texte
        self.couleur_bouton = couleur_bouton
        self.fenetre = fenetre

    # Méthode pour dessiner un bouton
    def dessiner(self):
        rayon = self.hauteur // 2
        pygame.draw.ellipse(self.fenetre, self.couleur_bouton, (self.x, self.y, 2*rayon, 2*rayon))  # Coin supérieur gauche
        pygame.draw.ellipse(self.fenetre, self.couleur_bouton, (self.x + self.largeur - 2*rayon, self.y, 2*rayon, 2*rayon))  # Coin supérieur droit
        pygame.draw.ellipse(self.fenetre, self.couleur_bouton, (self.x, self.y + self.hauteur - 2*rayon, 2*rayon, 2*rayon))  # Coin inférieur gauche
        pygame.draw.ellipse(self.fenetre, self.couleur_bouton, (self.x + self.largeur - 2*rayon, self.y + self.hauteur - 2*rayon, 2*rayon, 2*rayon))  # Coin inférieur droit
        pygame.draw.rect(self.fenetre, self.couleur_bouton, (self.x, self.y + rayon, self.largeur, self.hauteur - 2*rayon))  # Partie centrale verticale
        pygame.draw.rect(self.fenetre, self.couleur_bouton, (self.x + rayon, self.y, self.largeur - 2*rayon, self.hauteur))  # Partie centrale horizontale

        police = pygame.font.Font(None, self.taille_police)
        texte = police.render(self.texte, True, self.couleur_texte)
        self.fenetre.blit(texte, (self.x + (self.largeur - texte.get_width()) // 2, self.y + (self.hauteur - texte.get_height()) // 2))
    
    # Méthode pour vérifier si un bouton est survolé
    def est_survole(self, souris_x, souris_y):
        if self.x <= souris_x <= self.x + self.largeur and self.y <= souris_y <= self.y + self.hauteur:
            return True
        else:
            return False

    # Méthode pour vérifier si un bouton est cliqué
    def est_clique(self, x, y):
        return self.x <= x <= self.x + self.largeur and self.y <= y <= self.y + self.hauteur
    
class BoiteTexte:
    # Méthode pour initialiser une boîte de texte
    def __init__(self, x, y, texte, taille_police, couleur, fenetre):
        self.x = x
        self.y = y
        self.texte = texte
        self.taille_police = taille_police
        self.couleur = couleur
        self.fenetre = fenetre
        self.police = pygame.font.Font(None, self.taille_police)

    # Méthode pour dessiner une boîte de texte
    def dessiner(self):
        texte_surface = self.police.render(self.texte, True, self.couleur)
        self.fenetre.blit(texte_surface, (self.x, self.y - texte_surface.get_height()))
    
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

    # Méthode pour dessiner une boîte de saisie
    def dessiner(self):
        # Dessiner un rectangle avec des bords arrondis
        pygame.draw.rect(self.fenetre, self.couleur, (self.x, self.y, self.largeur, self.hauteur), 2, border_radius=20)

        # Dessiner le texte
        texte_surface = self.police.render(self.texte, True, (0, 0, 0))
        self.fenetre.blit(texte_surface, (self.x + 10, self.y + 5))

    # Méthode pour remplir une boîte de saisie
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
        btn_taille_police = 30
        btn_couleur_texte = (255, 255, 255)
        btn_couleur = (0, 0, 0)

        # Création du bouton "Lancer une partie"
        btn_lancer_l = 250
        btn_lancer_h = 50
        btn_lancer_x = (fnt_accueil_l - btn_lancer_l) / 2
        btn_lancer_y = (fnt_accueil_h - btn_lancer_h) / 2
        self.btn_lancer = Bouton(btn_lancer_x, btn_lancer_y, btn_lancer_l, btn_lancer_h,  "Lancer une partie", btn_taille_police, btn_couleur_texte, btn_couleur, self.fenetre)
        self.btn_lancer.dessiner()

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

        # Création des boîtes de saisie des noms de joueurs
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
        self.btn_ajouter_joueur = Bouton(self.btn_ajouter_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Ajouter un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_ajouter_joueur.dessiner()

        # Redessiner le bouton "Supprimer un joueur"
        self.btn_supprimer_joueur = Bouton(self.btn_supprimer_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Supprimer un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_supprimer_joueur.dessiner()

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
        self.btn_ajouter_joueur = Bouton(self.btn_ajouter_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Ajouter un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_ajouter_joueur.dessiner()

        # Redessiner le bouton "Supprimer un joueur"
        self.btn_supprimer_joueur = Bouton(self.btn_supprimer_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Supprimer un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_supprimer_joueur.dessiner()

        # Mettre à jour l'affichage
        pygame.display.flip()

    # Méthode pour récupérer les boîtes de saisie
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
        self.btn_ajouter_joueur = Bouton(self.btn_ajouter_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Ajouter un joueur", 20, (255, 255, 255), (125, 125, 125), self.fenetre)
        self.btn_ajouter_joueur.dessiner()

    # Méthode pour désactiver le bouton "Supprimer un joueur"
    def desactiver_btn_supprimer_joueur(self):
        self.btn_supprimer_joueur = Bouton(self.btn_supprimer_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Supprimer un joueur", 20, (255, 255, 255), (125, 125, 125), self.fenetre)
        self.btn_supprimer_joueur.dessiner()

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

class FntConfigTaches(Fenetre, Bouton, BoiteTexte, BoiteSaisie):
    def __init__(self):
        # Paramètres généraux de la fenêtre
        fnt_config_taches_l = 400
        fnt_config_taches_h = 700
        super().__init__(fnt_config_taches_l, fnt_config_taches_h)
        self.set_titre("Planning Poker : Configuration des tâches")
        self.set_couleur_fond((255, 255, 255))
        bt_couleur = (0, 0, 0)
        bs_couleur = (0, 0, 0)
        bt_taille_police = 25
        bs_taille_police = 30

        # Création de la boite de saisie du titre de la tâche
        bs_titre_l = 300
        bs_titre_h = 32
        bs_titre_x = (fnt_config_taches_l - bs_titre_l) / 2
        bs_titre_y = 100
        bs_titre_max_caracteres = 20
        bs_titre = BoiteSaisie(bs_titre_x, bs_titre_y, bs_titre_l, bs_titre_h, bs_taille_police, bs_couleur, bs_titre_max_caracteres, self.fenetre)
        bs_titre.dessiner()

        # Création d'un texte au-dessus de la boîte de saisie du titre
        bt_titre = BoiteTexte(bs_titre_x + 10, bs_titre_y, "Titre de la tâche", bt_taille_police, bt_couleur, self.fenetre)
        bt_titre.dessiner()

        # Création de la boite de saisie du titre de la tâche
        bs_description_l = 300
        bs_description_h = 160
        bs_description_x = (fnt_config_taches_l - bs_description_l) / 2
        bs_description_y = 175
        bs_desription_max_caracteres = 100
        bs_description = BoiteSaisie(bs_description_x, bs_description_y, bs_description_l, bs_description_h, bs_taille_police, bs_couleur, bs_desription_max_caracteres, self.fenetre)
        bs_description.dessiner()

        # Création d'un texte au-dessus de la boîte de saisie du titre
        bt_description = BoiteTexte(bs_description_x + 10, bs_description_y, "Description de la tâche", bt_taille_police, bt_couleur, self.fenetre)
        bt_description.dessiner()

        # Création du bouton "Enregistrer cette tâche"
        btn_enregistrer_l = 250
        btn_enregistrer_h = 40
        btn_enregistrer_x = (fnt_config_taches_l - btn_enregistrer_l) / 2
        btn_enregistrer_y = fnt_config_taches_h - 100
        self.btn_enregistrer = Bouton(btn_enregistrer_x, btn_enregistrer_y, btn_enregistrer_l, btn_enregistrer_h, "Enregistrer cette tâche", 30, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_enregistrer.dessiner()

        # Création du bouton "Valider"
        btn_valider_l = 100
        btn_valider_h = 40
        btn_valider_x = (fnt_config_taches_l - btn_valider_l) / 2
        btn_valider_y = fnt_config_taches_h - 50
        self.btn_valider = Bouton(btn_valider_x, btn_valider_y, btn_valider_l, btn_valider_h, "Valider", 30, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_valider.dessiner()

        # Création du bouton "Retour"
        btn_retour_l = 40
        btn_retour_h = 40
        btn_retour_x = 10
        btn_retour_y = 10
        self.btn_retour = Bouton(btn_retour_x, btn_retour_y, btn_retour_l, btn_retour_h, "<", 30, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_retour.dessiner()

    # Méthode pour récupérer le bouton "Enregistrer cette tâche"
    def get_btn_enregistrer(self):
        return self.btn_enregistrer

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
        self.btn_quitter = Bouton(btn_quitter_x, btn_quitter_y, btn_quitter_l, btn_quitter_h, "Quitter la partie", 30, (255, 255, 255), (200, 0, 0), self.fenetre)
        self.btn_quitter.dessiner()
    
    # Méthode pour récupérer le bouton "Quitter la partie"
    def get_btn_quitter(self):
        return self.btn_quitter

    # Méthode pour afficher la fenêtre
    def afficher(self):
        super().afficher()

    # Méthode pour fermer la fenêtre
    def fermer(self):
        super().fermer()