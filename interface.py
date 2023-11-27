import pygame
import sys

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

        # Configuration du bouton pour lancer une partie
        button_width = 250                                                         # Largeur du bouton
        button_height = 50                                                         # Hauteur du bouton
        button_x = (self.screen_width - button_width) // 2                         # Position x du bouton
        button_y = (self.screen_height - button_height) // 2                       # Position y du bouton
        self.button = pygame.Rect(button_x, button_y, button_width, button_height) # Création du bouton
        self.button_color = (0, 0, 0)                                              # Couleur du bouton
        self.text_color = (255, 255, 255)                                          # Couleur du texte
        
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

            pygame.draw.rect(self.screen, self.button_color, self.button)       # Dessin du bouton avec la couleur spécifiée
            text = self.font.render('Lancer une partie', True, self.text_color) # Création du texte pour le bouton
            text_rect = text.get_rect(center=self.button.center)                # Centrage du texte par rapport au bouton
            self.screen.blit(text, text_rect)                                   # Affichage du texte sur le bouton

            pygame.display.flip() # Mise à jour de l'affichage sur l'écran
            self.clock.tick(120)   # Contrôle de la vitesse de rafraîchissement de l'écran

        pygame.quit() # Quitte Pygame
        sys.exit()    # Quitte le programme

    # Méthode pour ouvrir une nouvelle fenêtre de configuration des joueurs
    def open_joueurs_window(self):
        fenetre_joueurs = FenetreJoueurs() # Création d'une nouvelle instance de FenetreJoueurs
        fenetre_joueurs.run()              # Exécution de la méthode run() de FenetreJoueurs pour afficher la fenêtre

class FenetreJoueurs(FenetreAccueil):
    # Méthode pour initialiser la fenêtre de configuration des joueurs
    def __init__(self):
        super().__init__()                                              # Récupération des paramètres de la classe parent
        pygame.display.set_caption('Paramètres de la partie - Joueurs') # Titre de la fenêtre
        self.return_button = pygame.Rect(10, 10, 30, 30)                # Création du bouton retour

    # Méthode pour contrôler l'interface utilisateur de la fenêtre d'accueil
    def run(self):
        while self.is_running:                # Boucle principale tant que le jeu est en cours
            self.screen.fill((255, 255, 255)) # Remplit l'écran avec du blanc

            # Boucle pour gérer les événements (clics de souris, fermeture de fenêtre)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Si l'utilisateur ferme la fenêtre
                    self.is_running = False   # Met fin à la boucle du jeu
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.return_button.collidepoint(event.pos):  # Vérification du clic sur le bouton retour
                        self.return_to_menu()                       # Appel de la méthode pour retourner à l'accueil
            
            pygame.draw.rect(self.screen, self.button_color, self.return_button) # Dessin du bouton avec la couleur spécifiée
            text = self.font.render('<', True, self.text_color)                  # Création du texte pour le bouton
            text_rect = text.get_rect(center=self.return_button.center)          # Centrage du texte par rapport au bouton
            self.screen.blit(text, text_rect)                                    # Affichage du texte sur le bouton

            pygame.display.flip() # Mise à jour de l'affichage sur l'écran
            self.clock.tick(120)  # Contrôle de la vitesse de rafraîchissement de l'écran

        pygame.quit() # Quitte Pygame
        sys.exit()    # Quitte le programme

    def return_to_menu(self):
        self.is_running = False            # Met fin à la boucle de la fenêtre de joueurs
        fenetre_accueil = FenetreAccueil() # Création d'une nouvelle instance de FenetreAccueil
        fenetre_accueil.run()              # Exécution de la méthode run de FenetreAccueil pour revenir à l'accueil