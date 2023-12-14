import pygame

from interface import Fenetre, Bouton, BoiteTexte, BoiteSaisie

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

class FntConfigJoueurs(Fenetre, Bouton, BoiteTexte, BoiteSaisie):
    def __init__(self):
        # Paramètres de la fenêtre
        self.fnt_config_joueurs_l = 450
        self.fnt_config_joueurs_h = 500
        super().__init__(self.fnt_config_joueurs_l, self.fnt_config_joueurs_h)
        self.set_titre("Planning Poker : Configuration des joueurs")
        self.set_couleur_fond((255, 255, 255))
        self.boites_saisie = []
        self.bt_joueurs = []
        self.bt_couleur = (0, 0, 0)
        self.bt_taille_police = 25

        # Création des boîtes de saisie des noms de joueurs
        self.boite_saisie_l = 300
        self.boite_saisie_h = 30
        self.boite_saisie_x = (self.fnt_config_joueurs_l - self.boite_saisie_l) / 2
        self.boite_saisie_y = 100
        self.taille_police = 30
        self.couleur = (0, 0, 0)
        self.max_caracteres = 15
        self.boites_saisie = [BoiteSaisie(self.boite_saisie_x, self.boite_saisie_y, self.boite_saisie_l, self.boite_saisie_h, self.taille_police, self.couleur, self.max_caracteres, 15, self.fenetre)] # Liste des boîtes de saisie

        # Création d'un texte au-dessus de la boîte de saisie des noms de joueurs
        self.bt_joueur = BoiteTexte(self.boite_saisie_x + 10, self.boite_saisie_y, "Nom du joueur n°1", self.bt_taille_police, self.bt_couleur, False, self.fenetre)
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
    
    # Méthode pour ajouter une boîte de saisie
    def ajouter_bs_joueur(self):
        # Créer une nouvelle boîte de saisie en dessous de la dernière
        derniere_boite = self.boites_saisie[-1]
        nouvelle_boite = BoiteSaisie(derniere_boite.x, derniere_boite.y + 60, self.boite_saisie_l, self.boite_saisie_h, self.taille_police, self.couleur, self.max_caracteres, 15, self.fenetre)
        self.boites_saisie.append(nouvelle_boite)

        # Création de la nouvelle étiquette
        nouvelle_bt_joueur = BoiteTexte(self.boite_saisie_x + 10, derniere_boite.y + 60, f"Nom du joueur n°{len(self.boites_saisie)}", self.bt_taille_police, self.bt_couleur, False, self.fenetre)
        self.bt_joueurs.append(nouvelle_bt_joueur)

        # Faire descendre les boutons "Ajouter un joueur" et "Supprimer un joueur" de 50 pixels
        ancien_y = self.btn_joueur_y
        self.btn_joueur_y += 60

        # Effacer l'ancien bouton en dessinant un rectangle de la couleur de fond sur son ancienne position
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_ajouter_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))

        # Effacer l'ancien bouton en dessinant un rectangle de la couleur de fond sur son ancienne position
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_supprimer_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))

        # Redessiner toutes les boîtes de saisie
        for boite in self.boites_saisie:
            boite.dessiner()

        # Redessiner toutes les boîtes de texte
        for bt_joueur in self.bt_joueurs:
            bt_joueur.dessiner()

        # Redessiner le bouton "Ajouter un joueur"
        self.btn_ajouter_joueur = Bouton(self.btn_ajouter_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Ajouter un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_ajouter_joueur.dessiner()

        # Redessiner le bouton "Supprimer un joueur"
        self.btn_supprimer_joueur = Bouton(self.btn_supprimer_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Supprimer un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_supprimer_joueur.dessiner()

        # Mettre à jour l'affichage
        pygame.display.flip()

    # Méthode pour supprimer une boîte de saisie
    def supprimer_bs_joueur(self):
        # Supprimer la dernière boîte de saisie
        derniere_boite = self.boites_saisie.pop()

        # Supprimer la dernière étiquette
        derniere_etiquette = self.bt_joueurs.pop()

        # Faire monter le bouton "Ajouter un joueur" et "Supprimer un joueur" de 60 pixels
        ancien_y = self.btn_joueur_y
        self.btn_joueur_y -= 60

        # Effacer l'ancienne boîte de saisie en dessinant un rectangle de la couleur de fond sur sa position
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(derniere_boite.x, derniere_boite.y, self.boite_saisie_l, self.boite_saisie_h))

        # Effacer l'ancienne étiquette en dessinant un rectangle de la couleur de fond sur sa position
        largeur_etiquette, hauteur_etiquette = derniere_etiquette.get_taille()
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(derniere_etiquette.x, derniere_etiquette.y - 18, largeur_etiquette, hauteur_etiquette))

        # Effacer l'ancien bouton en dessinant un rectangle de la couleur de fond sur son ancienne position
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_ajouter_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))

        # Effacer l'ancien bouton en dessinant un rectangle de la couleur de fond sur son ancienne position
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_supprimer_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))

        # Redessiner le bouton "Ajouter un joueur"
        self.btn_ajouter_joueur = Bouton(self.btn_ajouter_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Ajouter un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_ajouter_joueur.dessiner()

        # Redessiner le bouton "Supprimer un joueur"
        self.btn_supprimer_joueur = Bouton(self.btn_supprimer_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Supprimer un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_supprimer_joueur.dessiner()

        # Mettre à jour l'affichage
        pygame.display.flip()

    # Méthode pour récupérer les boîtes de saisie
    def get_bs_joueurs(self):
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
    def afficher_msg_erreur(self, message):
        # Création d'un texte au-dessus de la boîte de saisie du titre
        bt_msg_erreur = BoiteTexte(self.fnt_config_joueurs_l / 2, self.get_btn_valider().y - 20, message, 20, (200, 0, 0), True, self.fenetre)
        bt_msg_erreur.dessiner()

    # Méthode pour afficher la fenêtre
    def afficher(self):
        super().afficher()

    # Méthode pour fermer la fenêtre
    def fermer(self):
        super().fermer()

class FntConfigTaches(Fenetre, Bouton, BoiteTexte, BoiteSaisie):
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
        self.bt_titre = BoiteTexte(self.bs_titre_x + 10, self.bs_titre_y, "Titre de la tâche n°1", self.bt_taille_police, self.bt_couleur, False, self.fenetre)
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
        self.bt_description = BoiteTexte(self.bs_description_x + 10, self.bs_description_y, "Description de la tâche n°1", self.bt_taille_police, self.bt_couleur, False, self.fenetre)
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

    # Méthode pour récupérer la boîte de saisie du titre de la tâche
    def get_bs_titre(self):
        return self.bs_titre
    
    # Méthode pour récupérer la boîte de saisie de la description de la tâche
    def get_bs_description(self):
        return self.bs_description

    # Méthode pour récupérer le bouton "Enregistrer cette tâche"
    def get_btn_enregistrer(self):
        return self.btn_enregistrer

    # Méthode pour récupérer le bouton "Valider"
    def get_btn_valider(self):
        return self.btn_valider
    
    # Méthode pour récupérer le bouton "Retour"
    def get_btn_retour(self):
        return self.btn_retour
    
    # Méthode pour actualiser le texte de la boîte de saisie du titre
    def actualiser_bt_titre(self, nb_taches):
        self.bt_titre.reset_texte()
        self.bt_titre = BoiteTexte(self.bs_titre_x + 10, self.bs_titre_y, f"Titre de la tâche n°{nb_taches}", self.bt_taille_police, self.bt_couleur, False, self.fenetre)
        self.bt_titre.dessiner()

    # Méthode pour actualiser le texte de la boîte de saisie de la description
    def actualiser_bt_description(self, nb_taches):
        self.bt_description.reset_texte()
        self.bt_description = BoiteTexte(self.bs_description_x + 10, self.bs_description_y, f"Description de la tâche n°{nb_taches}", self.bt_taille_police, self.bt_couleur, False, self.fenetre)
        self.bt_description.dessiner()
    
    # Méthode pour réinitialiser les boîtes de saisie
    def reset_bs(self):
        self.bs_titre.reset_texte()
        self.bs_description.reset_texte()
        pygame.display.flip()

    # Méthode pour afficher un message d'erreur
    def afficher_msg_erreur(self, message):
        # Création d'un texte au-dessus de la boîte de saisie du titre
        bt_msg_erreur = BoiteTexte(self.fnt_config_taches_l / 2, self.get_btn_valider().y - 20, message, 20, (200, 0, 0), True, self.fenetre)
        bt_msg_erreur.dessiner()

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