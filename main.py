import pygame

from interface import BoiteSaisie
from fenetres import FntAccueil, FntConfigJoueurs, FntConfigTaches, FntJeu
from jeu import Joueurs, Taches

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

                # Création d'une liste de tous les éléments interactifs (boutons et boîtes de saisie)
                elements = []
                if fnt_accueil is not None:
                    elements.append(fnt_accueil.get_btn_lancer())
                if fnt_config_joueurs is not None:
                    elements.extend(fnt_config_joueurs.get_bs_joueurs())
                    elements.append(fnt_config_joueurs.get_btn_ajouter_joueur())
                    elements.append(fnt_config_joueurs.get_btn_supprimer_joueur())
                    elements.append(fnt_config_joueurs.get_btn_valider())
                    elements.append(fnt_config_joueurs.get_btn_retour())
                if fnt_config_taches is not None:
                    elements.append(fnt_config_taches.get_bs_titre())
                    elements.append(fnt_config_taches.get_bs_description())
                    elements.append(fnt_config_taches.get_btn_enregistrer())
                    elements.append(fnt_config_taches.get_btn_valider())
                    elements.append(fnt_config_taches.get_btn_retour())
                if fnt_jeu is not None:
                    elements.extend(fnt_jeu.get_cartes())
                    elements.append(fnt_jeu.get_btn_quitter())

                # Vérification si le curseur de la souris est sur un élément interactif
                cursor = pygame.SYSTEM_CURSOR_ARROW  # Initialisation du curseur en mode normal
                for element in elements:
                    if element.est_survole(souris_x, souris_y):
                        if isinstance(element, BoiteSaisie):
                            cursor = pygame.SYSTEM_CURSOR_IBEAM  # Mode texte pour les boîtes de saisie
                        else:
                            cursor = pygame.SYSTEM_CURSOR_HAND  # Mode main pour les boutons
                        break

                # Changement du curseur de la souris
                pygame.mouse.set_cursor(cursor)

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
                            fnt_config_joueurs.ajouter_bs_joueur() # Ajout d'une boîte de saisie
                        elif nb_joueurs == 4:
                            nb_joueurs += 1
                            print("[UDPATE] : Nombre de joueurs : " + str(nb_joueurs)) # [DEBUG]
                            fnt_config_joueurs.ajouter_bs_joueur() # Ajout d'une boîte de saisie
                            fnt_config_joueurs.desactiver_btn_ajouter_joueur()  # Désactiver le bouton "Supprimer un joueur"
                        else:
                            print("[WARNING] : Nombre de joueurs maximum atteint") # [DEBUG]
                    
                    elif fnt_config_joueurs.get_btn_supprimer_joueur().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Supprimer un joueur' cliqué") # [DEBUG]
                        if nb_joueurs > 3:
                            nb_joueurs -= 1
                            print("[UPDATE] : Nombre de joueurs : " + str(nb_joueurs)) # [DEBUG]
                            fnt_config_joueurs.supprimer_bs_joueur() # Suppresion d'une boîte de saisie
                        elif nb_joueurs == 3:
                            nb_joueurs -= 1
                            print("[UDPATE] : Nombre de joueurs : " + str(nb_joueurs)) # [DEBUG]
                            fnt_config_joueurs.supprimer_bs_joueur() # Suppression d'une boîte de saisie
                            fnt_config_joueurs.desactiver_btn_supprimer_joueur()  # Désactiver le bouton "Supprimer un joueur"
                        else:
                            print("[WARNING] : Nombre de joueurs minimum atteint") # [DEBUG]
                

                    elif fnt_config_joueurs.get_btn_valider().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Valider' cliqué") # [DEBUG]
                        
                        Joueurs.joueurs = []
                        # Parcourir toutes les boîtes de saisie
                        for i, boite_saisie in enumerate(fnt_config_joueurs.get_bs_joueurs()):
                            # Créer un nouveau joueur avec le numéro et le texte de la boîte de saisie comme nom
                            joueur = Joueurs(i+1, boite_saisie.get_texte())

                            # Ajouter le joueur à la liste des joueurs
                            Joueurs.joueurs.append(joueur)
                        # Afficher la liste des joueurs [DEBUG]
                        print("Liste des joueurs :")
                        for joueur in Joueurs.joueurs:
                            print(joueur)

                        # Vérifier si tous les joueurs ont un nom non vide
                        if all(joueur.nom for joueur in Joueurs.joueurs):
                            fnt_config_joueurs.fermer() # Fermeture de la fenêtre de configuration des joueurs
                            fnt_config_joueurs = None # Réinitialisation de fnt_config_joueurs
                            fnt_config_taches = FntConfigTaches() # Création de la fenêtre de configuration des tâches
                            fnt_config_taches.afficher() # Affichage de la fenêtre de configuration des tâches
                            Taches.taches = [] # Réinitialisation de la liste des tâches
                            nb_taches = 0 # Nombre de tâches
                        else:
                            print("[WARNING] : Tous les joueurs doivent avoir un nom") # [DEBUG]
                            fnt_config_joueurs.afficher_msg_erreur("Attention : tous les joueurs doivent avoir un nom !")
                
                    elif fnt_config_joueurs.get_btn_retour().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Retour' cliqué") # [DEBUG]
                        fnt_config_joueurs.fermer() # Fermeture de la fenêtre de configuration des joueurs
                        fnt_config_joueurs = None # Réinitialisation de fnt_config_joueurs
                        fnt_accueil = FntAccueil() # Réinitialisation de fnt_accueil
                        fnt_accueil.afficher() # Réaffichage de la fenêtre d'accueil

                elif fnt_config_taches is not None:
                    if fnt_config_taches.get_btn_enregistrer().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Enregistrer cette tache' cliqué") # [DEBUG]

                        titre = fnt_config_taches.get_bs_titre().get_texte()
                        description = fnt_config_taches.get_bs_description().get_texte()

                        if titre:  # Vérifier si le titre n'est pas vide
                            if not description:  # Si la description est vide
                                description = "Aucune description"  # Définir la description par défaut

                            # Enregistrer la tâche
                            numero = len(Taches.taches) + 1  # Numéro de la tâche
                            difficulte = None  # Difficulté de la tâche (à modifier selon vos besoins)
                            tache = Taches(numero, titre, description, difficulte)
                            Taches.taches.append(tache)

                            # Incrémenter le nombre de tâches
                            nb_taches += 1

                            # Actualisation de l'affichage
                            fnt_config_taches.actualiser_bt_titre(nb_taches+1)
                            fnt_config_taches.actualiser_bt_description(nb_taches+1)
                            fnt_config_taches.reset_bs()
                            print(f"[INFO] : La tâche '{titre}' enregistrée avec succès") # [DEBUG]
                        else:
                            print("[WARNING] : Le titre de la tâche ne peut pas être vide") # [DEBUG]
                            fnt_config_taches.afficher_msg_erreur("Attention : le titre de la tâche ne peut pas être vide !")

                        # Afficher la liste des tâches [DEBUG]
                        print("Liste des tâches :")
                        for tache in Taches.taches:
                            print(tache)

                    elif fnt_config_taches.get_btn_valider().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Valider' cliqué") # [DEBUG]
                        if nb_taches == 0:
                            fnt_config_taches.afficher_msg_erreur("             Attention : aucune tâche n'a été enregistrée !             ")
                            print("[WARNING] : Aucune tâche enregistrée") # [DEBUG]
                        else:
                            fnt_config_taches.fermer() # Fermeture de la fenêtre de configuration des tâches
                            fnt_config_taches = None # Réinitialisation de fnt_config_taches
                            nb_taches_traitees = 0 # Nombre de tâches traitées
                            tache_a_traiter = Taches.taches[nb_taches_traitees] # Tâche à traiter
                            fnt_jeu = FntJeu(tache_a_traiter) # Création de la fenêtre de jeu
                            fnt_jeu.afficher() # Affichage de la fenêtre de jeu
                
                    elif fnt_config_taches.get_btn_retour().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Retour' cliqué") # [DEBUG]
                        fnt_config_taches.fermer() # Fermeture de la fenêtre de configuration des tâches
                        fnt_config_taches = None # Réinitialisation de fnt_config_taches
                        fnt_config_joueurs = FntConfigJoueurs() # Création de la fenêtre de configuration des joueurs
                        fnt_config_joueurs.afficher() # Affichage de la fenêtre de configuration des joueurs
                        nb_joueurs = 2 # Nombre de joueurs
                        fnt_config_joueurs.desactiver_btn_supprimer_joueur()
                    
                elif fnt_jeu is not None:
                    for carte in fnt_jeu.liste_cartes:
                        if carte.est_clique(souris_x, souris_y):
                            print(f"[EVENT] : Carte '{carte.nom_carte}' cliquée") # [DEBUG]*
                            fnt_jeu.choisir_carte(carte)  #appel la fonction choisir carte

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
                    for i, boite_saisie in enumerate(fnt_config_joueurs.get_bs_joueurs()):
                        if boite_saisie.est_clique(souris_x, souris_y):
                            boite_saisie.evenement(event)
                            print("[UPDATE] Boite de saisie {} : ".format(i+1) + boite_saisie.get_texte()) # [DEBUG]
                
                elif fnt_config_taches is not None:
                    if fnt_config_taches.get_bs_titre().est_clique(souris_x, souris_y):
                        fnt_config_taches.get_bs_titre().evenement(event)
                        print("[UPDATE] Boite de saisie 'Titre' : " + fnt_config_taches.get_bs_titre().get_texte()) # [DEBUG]
                        
                    elif fnt_config_taches.get_bs_description().est_clique(souris_x, souris_y):
                        fnt_config_taches.get_bs_description().evenement(event)
                        print("[UPDATE] Boite de saisie 'Description' : " + fnt_config_taches.get_bs_description().get_texte()) # [DEBUG]

        # Mettre à jour l'affichage
        pygame.display.flip()
    pygame.quit()