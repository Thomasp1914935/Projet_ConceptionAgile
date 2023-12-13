import pygame

from interface import FntAccueil, FntConfigJoueurs, FntConfigTaches, FntJeu

if __name__ == "__main__":

    # Initialisation de l'horloge
    horloge = pygame.time.Clock()

    # Affichage de la fenêtre Accueil
    fnt_accueil = FntAccueil()
    fnt_accueil.afficher()

    # Initialisation des autres fenêtres
    fnt_config_joueurs = None
    fnt_config_taches = None
    fnt_jeu = None

    # Boucle d'événements de l'application
    running = True
    while running:
        # Définition des variables globales
        horloge.tick(120) # Limiter la fréquence de rafraîchissement à 120 FPS
        souris_x, souris_y = pygame.mouse.get_pos() # Récupération des coordonnées de la souris

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Evénements si la souris est déplacée
            elif event.type == pygame.MOUSEMOTION:

                # Création d'une liste de tous les boutons
                boutons = []
                if fnt_accueil is not None:
                    boutons.append(fnt_accueil.get_btn_lancer())
                if fnt_config_joueurs is not None:
                    boutons.append(fnt_config_joueurs.get_btn_ajouter_joueur())
                    boutons.append(fnt_config_joueurs.get_btn_valider())
                    boutons.append(fnt_config_joueurs.get_btn_retour())
                if fnt_config_taches is not None:
                    boutons.append(fnt_config_taches.get_btn_valider())
                    boutons.append(fnt_config_taches.get_btn_retour())
                if fnt_jeu is not None:
                    boutons.append(fnt_jeu.get_btn_quitter())

                # Vérification si le curseur de la souris est sur un bouton
                for bouton in boutons:
                    if bouton.est_survole(souris_x, souris_y):
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) # Changement du curseur de la souris en forme de main
                        break
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) # Changement du curseur de la souris en forme de flèche

            # Evénements si un bouton de la souris est cliqué
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if fnt_accueil is not None:
                    if fnt_accueil.get_btn_lancer().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Lancer une partie' cliqué") # [DEBUG]
                        fnt_accueil.fermer() # Fermeture de la fenêtre d'accueil
                        fnt_accueil = None # Réinitialisation de fnt_accueil
                        fnt_config_joueurs = FntConfigJoueurs() # Création de la fenêtre de configuration des joueurs
                        fnt_config_joueurs.afficher() # Affichage de la fenêtre de configuration des joueurs
                        nb_joueurs = 2 # Nombre de joueurs
                        fnt_config_joueurs.desactiver_btn_supprimer_joueur()
                
                elif fnt_config_joueurs is not None:
                    if fnt_config_joueurs.get_btn_ajouter_joueur().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Ajouter un joueur' cliqué") # [DEBUG]
                        if nb_joueurs < 4:
                            nb_joueurs += 1
                            print("[UPDATE] : Nombre de joueurs : " + str(nb_joueurs)) # [DEBUG]
                            fnt_config_joueurs.ajouter_boite_saisie() # Ajout d'une boîte de saisie
                        elif nb_joueurs == 4:
                            nb_joueurs += 1
                            print("[UDPATE] : Nombre de joueurs : " + str(nb_joueurs)) # [DEBUG]
                            fnt_config_joueurs.ajouter_boite_saisie() # Ajout d'une boîte de saisie
                            fnt_config_joueurs.desactiver_btn_ajouter_joueur()  # Désactiver le bouton "Supprimer un joueur"
                        else:
                            print("[WARNING] : Nombre de joueurs maximum atteint") # [DEBUG]
                    
                    elif fnt_config_joueurs.get_btn_supprimer_joueur().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Supprimer un joueur' cliqué") # [DEBUG]
                        if nb_joueurs > 3:
                            nb_joueurs -= 1
                            print("[UPDATE] : Nombre de joueurs : " + str(nb_joueurs)) # [DEBUG]
                            fnt_config_joueurs.supprimer_boite_saisie() # Suppresion d'une boîte de saisie
                        elif nb_joueurs == 3:
                            nb_joueurs -= 1
                            print("[UDPATE] : Nombre de joueurs : " + str(nb_joueurs)) # [DEBUG]
                            fnt_config_joueurs.supprimer_boite_saisie() # Suppression d'une boîte de saisie
                            fnt_config_joueurs.desactiver_btn_supprimer_joueur()  # Désactiver le bouton "Supprimer un joueur"
                        else:
                            print("[WARNING] : Nombre de joueurs minimum atteint") # [DEBUG]
                

                    elif fnt_config_joueurs.get_btn_valider().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Valider' cliqué") # [DEBUG]
                        fnt_config_joueurs.fermer() # Fermeture de la fenêtre de configuration des joueurs
                        fnt_config_joueurs = None # Réinitialisation de fnt_config_joueurs
                        fnt_config_taches = FntConfigTaches() # Création de la fenêtre de configuration des tâches
                        fnt_config_taches.afficher() # Affichage de la fenêtre de configuration des tâches
                
                    elif fnt_config_joueurs.get_btn_retour().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Retour' cliqué") # [DEBUG]
                        fnt_config_joueurs.fermer() # Fermeture de la fenêtre de configuration des joueurs
                        fnt_config_joueurs = None # Réinitialisation de fnt_config_joueurs
                        fnt_accueil = FntAccueil() # Réinitialisation de fnt_accueil
                        fnt_accueil.afficher() # Réaffichage de la fenêtre d'accueil

                elif fnt_config_taches is not None:
                    if fnt_config_taches.get_btn_valider().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Valider' cliqué") # [DEBUG]
                        fnt_config_taches.fermer() # Fermeture de la fenêtre de configuration des tâches
                        fnt_config_taches = None # Réinitialisation de fnt_config_taches
                        fnt_jeu = FntJeu() # Création de la fenêtre de jeu
                        fnt_jeu.afficher() # Affichage de la fenêtre de jeu
                
                    elif fnt_config_taches.get_btn_retour().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Retour' cliqué") # [DEBUG]
                        fnt_config_taches.fermer() # Fermeture de la fenêtre de configuration des tâches
                        fnt_config_taches = None # Réinitialisation de fnt_config_taches
                        fnt_config_joueurs = FntConfigJoueurs() # Création de la fenêtre de configuration des joueurs
                        fnt_config_joueurs.afficher() # Affichage de la fenêtre de configuration des joueurs
                        nb_joueurs = 2 # Nombre de joueurs
                    
                elif fnt_jeu is not None:
                    if fnt_jeu.get_btn_quitter().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Quitter la partie' cliqué") # [DEBUG]
                        fnt_jeu.fermer() # Fermeture de la fenêtre de jeu
                        fnt_jeu = None # Réinitialisation de fnt_jeu
                        fnt_accueil = FntAccueil() # Réinitialisation de fnt_accueil
                        fnt_accueil.afficher() # Réaffichage de la fenêtre d'accueil
            
            # Evénements si une touche du clavier est pressée
            elif event.type == pygame.KEYDOWN:
                if fnt_config_joueurs is not None:
                    # Parcourir toutes les boîtes de saisie
                    for i, boite_saisie in enumerate(fnt_config_joueurs.get_boites_saisie()):
                        if boite_saisie.est_clique(souris_x, souris_y):
                            boite_saisie.evenement(event)
                            print("[UPDATE] Boite de saisie {} : ".format(i+1) + boite_saisie.get_texte()) # [DEBUG]

        # Mettre à jour l'affichage
        pygame.display.flip()
    pygame.quit()