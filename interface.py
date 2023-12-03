from jeu import Joueur

import sys    # Importation du module sys pour accéder aux fonctionnalités système de Python
import pygame # Importation de la bibliothèque Pygame pour créer des jeux et des applications multimédias

class FenetreAccueil:
    # Méthode pour initialiser la fenêtre d'accueil
    def __init__(self):
        # Initialisation de toutes les bibliothèques Pygame et leurs modules associés
        pygame.init()

        # Configuration de la fenêtre accueil
        self.screen_width = 400                                                        # Largeur de la fenêtre
        self.screen_height = 300                                                       # Hauteur de la fenêtre
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) # Initialisation de la fenêtre accueil
        pygame.display.set_caption('Planning Poker - Accueil')                         # Titre de la fenêtre
        self.clock = pygame.time.Clock()                                               # Objet pour contrôler la vitesse de la boucle de jeu
        self.font = pygame.font.Font(None, 36)                                         # Police utilisée pour le texte

        # Configuration du bouton "Lancer une partie"
        button_width = 250                                                         # Largeur du bouton
        button_height = 50                                                         # Hauteur du bouton
        button_x = (self.screen_width - button_width) // 2                         # Position x du bouton
        button_y = (self.screen_height - button_height) // 2                       # Position y du bouton
        self.button = pygame.Rect(button_x, button_y, button_width, button_height) # Création du bouton
        border_radius = 15                                                         # Rayon de l'arrondi des coins
        self.button_radius = border_radius                                         # Ajout d'un attribut pour le rayon d'arrondi du bouton
        self.button_color = (0, 0, 0)                                              # Couleur du bouton
        self.text_color = (255, 255, 255)                                          # Couleur du texte

        # Configuration du bouton retour
        self.return_button = pygame.Rect(10, 10, 30, 30) # Création du bouton retour
        border_radius = 3                                # Rayon de l'arrondi des coins
        self.return_button_radius = border_radius        # Ajout d'un attribut pour le rayon d'arrondi du bouton
        
        # Variable de contrôle pour la boucle principale du jeu
        self.is_running = True

    # Méthode pour contrôler l'interface utilisateur de la fenêtre d'accueil
    def run(self):
        while self.is_running:                # Boucle principale tant que le jeu est en cours
            self.screen.fill((255, 255, 255)) # Remplit l'écran avec du blanc

            # Boucle pour gérer les événements (clics de souris, fermeture de fenêtre)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:               # Si l'utilisateur ferme la fenêtre
                    self.is_running = False                 # Met fin à la boucle du jeu
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Si un clic de souris est détecté
                    if self.button.collidepoint(event.pos): # Vérification si le clic est sur le bouton
                        self.open_joueurs_window()          # Ouverture de la fenêtre de configuration des joueurs
            
            # Changement de curseur en fonction de l'état de survol de chaque bouton
            if self.button.collidepoint(pygame.mouse.get_pos()):    # Si survol du bouton "Lancer une partie"
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:                                                   # Si aucun bouton n'est survolé
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            # Paramètres d'affichage du bouton "Lancer une partie"
            pygame.draw.rect(self.screen, self.button_color, self.button, border_radius=self.button_radius) # Dessin du bouton avec la couleur spécifiée
            text = self.font.render('Lancer une partie', True, self.text_color)                             # Création du texte pour le bouton
            text_rect = text.get_rect(center=self.button.center)                                            # Centrage du texte par rapport au bouton
            self.screen.blit(text, text_rect)                                                               # Affichage du texte sur le bouton

            pygame.display.flip() # Mise à jour de l'affichage sur l'écran
            self.clock.tick(120)   # Contrôle de la vitesse de rafraîchissement de l'écran

        pygame.quit() # Quitte Pygame
        sys.exit()    # Quitte le programme

    # Méthode pour aller à la fenêtre de configuration des joueurs
    def open_joueurs_window(self):
        fenetre_joueurs = FenetreJoueurs() # Création d'une nouvelle instance de FenetreJoueurs
        fenetre_joueurs.run()              # Exécution de la méthode run() de FenetreJoueurs pour afficher la fenêtre

class FenetreJoueurs(FenetreAccueil):
    # Méthode pour initialiser la fenêtre de configuration des joueurs
    def __init__(self):
        # Récupération des paramètres de la classe parent
        super().__init__()
                                                      
        # Configuration de la fenêtre de configuration des joueurs
        self.screen_width = 400                                                        # Largeur de la fenêtre
        self.screen_height = 700                                                       # Hauteur de la fenêtre
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) # Initialisation de la fenêtre de configuration des joueurs
        pygame.display.set_caption('Paramètres de la partie - Joueurs')                # Titre de la fenêtre

        # Initialisation des champs de saisie des noms des joueurs
        self.input_boxes = [
            pygame.Rect(50, 100, 200, 30), # Champs de saisie pour le joueur 1
            pygame.Rect(50, 150, 200, 30)  # Champs de saisie pour le joueur 2
        ]
        self.joueurs = []  # Liste pour stocker les instances des joueurs

        # Configuration du bouton "Ajouter un joueur"
        self.add_player_button = pygame.Rect(50, 200, 250, 50) # Création du bouton "Ajouter un joueur"
        border_radius = 10                                     # Rayon de l'arrondi des coins
        self.add_player_button_radius = border_radius          # Ajout d'un attribut pour le rayon d'arrondi du bouton

        # Configuration du bouton valider
        button_width = 100                                                                  # Largeur du bouton
        button_height = 40                                                                  # Hauteur du bouton
        button_x = (self.screen_width - button_width) // 2                                  # Position x du bouton
        button_y = self.screen_height - 60                                                  # Position y du bouton
        self.validate_button = pygame.Rect(button_x, button_y, button_width, button_height) # Création du bouton valider
        border_radius = 10                                                                  # Rayon de l'arrondi des coins
        self.validate_button_radius = border_radius                                         # Ajout d'un attribut pour le rayon d'arrondi du bouton

    # Méthode pour contrôler l'interface utilisateur de la fenêtre de configuration des joueurs
    def run(self):
        while self.is_running:                # Boucle principale tant que le jeu est en cours
            self.screen.fill((255, 255, 255)) # Remplit l'écran avec du blanc

            # Boucle pour gérer les événements (clics de souris, fermeture de fenêtre)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                            # Si l'utilisateur ferme la fenêtre
                    self.is_running = False                              # Met fin à la boucle du jeu
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.return_button.collidepoint(event.pos):       # Vérification du clic sur le bouton retour
                        self.return_to_menu()                            # Appel de la méthode pour retourner à l'accueil
                    elif self.add_player_button.collidepoint(event.pos): # Vérification du clic sur le bouton "Ajouter un joueur"
                        self.add_player()                                # Appel de la méthode pour ajouter un joueur
                    elif self.validate_button.collidepoint(event.pos):   # Vérification du clic sur le bouton valider
                        self.go_to_config_taches()                       # Appel de la méthode pour aller à la fenêtre de configuration des tâches

            # Changement de curseur en fonction de l'état de survol de chaque bouton
            if self.return_button.collidepoint(pygame.mouse.get_pos()):       # Si survol du bouton retour
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            elif self.add_player_button.collidepoint(pygame.mouse.get_pos()): # Si survol du bouton "Ajouter un joueur"
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            elif self.validate_button.collidepoint(pygame.mouse.get_pos()):   # Si survol du bouton valider
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:                                                             # Si aucun bouton n'est survolé
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            
            # Paramètres d'affichage du bouton retour
            pygame.draw.rect(self.screen, self.button_color, self.return_button, border_radius=self.return_button_radius) # Dessin du bouton avec la couleur spécifiée
            text = self.font.render('<', True, self.text_color)                                                           # Création du texte pour le bouton
            text_rect = text.get_rect(center=self.return_button.center)                                                   # Centrage du texte par rapport au bouton
            self.screen.blit(text, text_rect)                                                                             # Affichage du texte sur le bouton

            # Paramètres d'affichage du bouton "Ajouter un joueur"
            pygame.draw.rect(self.screen, self.button_color, self.add_player_button, border_radius=self.add_player_button_radius) # Dessin du bouton avec la couleur spécifiée
            self.add_player_text = self.font.render('Ajouter un joueur', True, self.text_color)                                   # Création du texte pour le bouton
            self.text_rect_add_player = self.add_player_text.get_rect(center=self.add_player_button.center)                       # Centrage du texte par rapport au bouton
            self.screen.blit(self.add_player_text, self.text_rect_add_player)                                                     # Affichage du texte sur le bouton

            # Paramètres d'affichage du bouton valider
            pygame.draw.rect(self.screen, self.button_color, self.validate_button, border_radius=self.validate_button_radius) # Dessin du bouton avec la couleur spécifiée
            text_next = self.font.render('Valider', True, self.text_color)                                                    # Création du texte pour le bouton
            text_rect_next = text_next.get_rect(center=self.validate_button.center)                                           # Centrage du texte par rapport au bouton
            self.screen.blit(text_next, text_rect_next)                                                                       # Affichage du texte sur le bouton

            for box in self.input_boxes:
                pygame.draw.rect(self.screen, (0, 0, 0), box, 2)

            pygame.display.flip() # Mise à jour de l'affichage sur l'écran
            self.clock.tick(120)  # Contrôle de la vitesse de rafraîchissement de l'écran

        pygame.quit() # Quitte Pygame
        sys.exit()    # Quitte le programme

    # Méthode pour revenir sur la fenêtre d'accueil
    def return_to_menu(self):
        self.is_running = False            # Met fin à la boucle de la fenêtre de configuration des joueurs
        fenetre_accueil = FenetreAccueil() # Création d'une nouvelle instance de FenetreAccueil
        fenetre_accueil.run()              # Exécution de la méthode run de FenetreAccueil pour revenir à l'accueil

    def add_player(self):
        # Ajout d'un joueur à la liste des joueurs avec les noms saisis dans les champs de texte
        new_player_names = []
        for index, box in enumerate(self.input_boxes):
            # Si le champ de saisie est vide, ajoutez une chaîne vide pour ce joueur
            if not box.collidepoint(pygame.mouse.get_pos()):  
                new_player_names.append("")
            else:
                new_player_names.append("")  # Vous pouvez utiliser ici votre propre logique pour obtenir le texte saisi

        for name in new_player_names:
            if name:
                nouveau_joueur = Joueur(len(self.joueurs) + 1, name)
                self.joueurs.append(nouveau_joueur)
     
    
    # Méthode pour aller à la fenêtre de configuration des tâches
    def go_to_config_taches(self):
        self.is_running = False          # Met fin à la boucle de la fenêtre de configuration des joueurs
        fenetre_taches = FenetreTaches() # Création d'une nouvelle instance de FenetreTaches
        fenetre_taches.run()             # Exécution de la méthode run de FenetreTaches pour aller à la configuration des tâches

class FenetreTaches(FenetreAccueil):
    # Méthode pour initialiser la fenêtre de configuration des tâches
    def __init__(self):
        # Récupération des paramètres de la classe parent
        super().__init__()

        # Configuration de la fenêtre de configuration des tâches
        pygame.display.set_caption('Paramètres de la partie - Tâches') # Titre de la fenêtre

    # Méthode pour contrôler l'interface utilisateur de la fenêtre de configuration des tâches
    def run(self):
        while self.is_running:                # Boucle principale tant que le jeu est en cours
            self.screen.fill((255, 255, 255)) # Remplit l'écran avec du blanc

            # Boucle pour gérer les événements (clics de souris, fermeture de fenêtre)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                      # Si l'utilisateur ferme la fenêtre
                    self.is_running = False                        # Met fin à la boucle du jeu
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.return_button.collidepoint(event.pos): # Vérification du clic sur le bouton retour
                        self.return_to_config_joueurs()            # Appel de la méthode pour retourner à la configuration des joueurs
            
            # Changement de curseur en fonction de l'état de survol de chaque bouton
            if self.return_button.collidepoint(pygame.mouse.get_pos()): # Si survol du bouton retour
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:                                                       # Si aucun bouton n'est survolé
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            
            # Paramètres d'affichage du bouton retour
            pygame.draw.rect(self.screen, self.button_color, self.return_button, border_radius=self.return_button_radius) # Dessin du bouton avec la couleur spécifiée
            text = self.font.render('<', True, self.text_color)                                                           # Création du texte pour le bouton
            text_rect = text.get_rect(center=self.return_button.center)                                                   # Centrage du texte par rapport au bouton
            self.screen.blit(text, text_rect)                                                                             # Affichage du texte sur le bouton

            pygame.display.flip() # Mise à jour de l'affichage sur l'écran
            self.clock.tick(120)  # Contrôle de la vitesse de rafraîchissement de l'écran

        pygame.quit() # Quitte Pygame
        sys.exit()    # Quitte le programme

    # Méthode pour revenir sur la fenêtre de configuration des joueurs
    def return_to_config_joueurs(self):
        self.is_running = False            # Met fin à la boucle de la fenêtre de configuration des tâches
        fenetre_joueurs = FenetreJoueurs() # Création d'une nouvelle instance de FenetreJoueurs
        fenetre_joueurs.run()              # Exécution de la méthode run de FenetreJoueurs pour revenir à la configuration des joueurs