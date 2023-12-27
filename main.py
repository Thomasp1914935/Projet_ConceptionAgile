import os
from tkinter import messagebox
import pygame

from interface import BoiteSaisie
from fenetres import FntAccueil, FntConfigJoueurs, FntConfigTaches, FntJeu
from jeu import Joueurs, Taches, Partie

if __name__ == "__main__":
    # Initialisation de l'horloge
    horloge = pygame.time.Clock()

    # Affichage de la fenêtre Accueil
    fnt_accueil = FntAccueil()
    fnt_accueil.afficher()
    if not os.path.isfile('sauvegarde.json'):
        sauvegarde = False
        fnt_accueil.desactiver_btn_reprendre_partie()
    else:
        sauvegarde = True

    # Initialisation des autres fenêtres
    fnt_config_joueurs = None
    fnt_config_taches = None
    fnt_jeu = None

    # Boucle d'événements de l'application
    running = True
    while running:
        # Définition des variables globales
        horloge.tick(120) # Limitation de la fréquence de rafraîchissement à 120 FPS
        souris_x, souris_y = pygame.mouse.get_pos() # Récupération des coordonnées de la souris

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # [EVENEMENT] : Souris déplacée
            elif event.type == pygame.MOUSEMOTION:

                # Création d'une liste de tous les éléments interactifs (boutons et boîtes de saisie) de l'application
                elements = []
                if fnt_accueil is not None:
                    elements.append(fnt_accueil.get_btn_strict())
                    elements.append(fnt_accueil.get_btn_moyenne())
                    elements.append(fnt_accueil.get_btn_mediane())
                    elements.append(fnt_accueil.get_btn_majabs())
                    elements.append(fnt_accueil.get_btn_majrel())
                    elements.append(fnt_accueil.get_btn_reprendre_partie())
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

            # [EVENEMENT] : Clic de la souris
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                # Evénements de la fenêtre Accueil
                if fnt_accueil is not None:
                    # Evénement du bouton 'Mode strict'
                    if fnt_accueil.get_btn_strict().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Mode strict' cliqué") # [DEBUG]
                        fnt_accueil.fermer()
                        fnt_accueil = None
                        fnt_config_joueurs = FntConfigJoueurs()
                        fnt_config_joueurs.afficher()
                        fnt_config_joueurs.desactiver_btn_supprimer_joueur()
                        mode_jeu = "strict"
                        nb_joueurs = 2
                    
                    # Evénement du bouton 'Mode moyenne'
                    elif fnt_accueil.get_btn_moyenne().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Mode moyenne' cliqué") # [DEBUG]
                        fnt_accueil.fermer()
                        fnt_accueil = None
                        fnt_config_joueurs = FntConfigJoueurs()
                        fnt_config_joueurs.afficher()
                        fnt_config_joueurs.desactiver_btn_supprimer_joueur()
                        mode_jeu = "moyenne"
                        nb_joueurs = 2

                    # Evénement du bouton 'Mode médiane'
                    elif fnt_accueil.get_btn_mediane().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Mode médiane' cliqué") # [DEBUG]
                        fnt_accueil.fermer()
                        fnt_accueil = None
                        fnt_config_joueurs = FntConfigJoueurs()
                        fnt_config_joueurs.afficher()
                        fnt_config_joueurs.desactiver_btn_supprimer_joueur()
                        mode_jeu = "médiane"
                        nb_joueurs = 2
                    
                    # Evénement du bouton 'Mode majorité absolue'
                    elif fnt_accueil.get_btn_majabs().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Mode moyenne absolue' cliqué") # [DEBUG]
                        fnt_accueil.fermer()
                        fnt_accueil = None
                        fnt_config_joueurs = FntConfigJoueurs()
                        fnt_config_joueurs.afficher()
                        fnt_config_joueurs.desactiver_btn_supprimer_joueur()
                        mode_jeu = "majorité absolue"
                        nb_joueurs = 2
                    
                    # Evénement du bouton 'Mode majorité relative'
                    elif fnt_accueil.get_btn_majrel().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Mode moyenne relative' cliqué") # [DEBUG]
                        fnt_accueil.fermer()
                        fnt_accueil = None
                        fnt_config_joueurs = FntConfigJoueurs()
                        fnt_config_joueurs.afficher()
                        fnt_config_joueurs.desactiver_btn_supprimer_joueur()
                        mode_jeu = "majorité relative"
                        nb_joueurs = 2

                    # Evénement du bouton 'Reprendre la partie'
                    elif fnt_accueil.get_btn_reprendre_partie().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Reprendre la partie' cliqué")
                        # Si aucune partie n'a été sauvegardée sur la machine
                        if sauvegarde == False:
                            print("[WARNING] : Aucune partie sauvegardée") # [DEBUG]
                        # Si une partie a été sauvegardée sur la machine
                        if sauvegarde == True:
                            mode_jeu = None
                            partie = Partie(mode_jeu, 0, fnt_jeu)
                            integrite_sauvegarde = partie.analyse_sauvegarde() # Analyse de l'intégrité de la sauvegarde
                            # Si la sauvegarde est intègre
                            if integrite_sauvegarde == 0:
                                print("[INFO] : L'intégrité de la sauvegarde a été vérifiée avec succès") # [DEBUG]
                                partie_finie, mode_jeu, tache_actuelle, joueur_actuel = partie.charger_sauvegarde() # Chargement de la sauvegarde
                                # Si la partie sauvegardée est terminée
                                if partie_finie == True:
                                    print("[WARNING] : La partie sauvegardée est terminée") # [DEBUG]
                                    messagebox.showinfo("Planning Poker : Information", "La partie sauvegardée est terminée.")
                                # Si la partie sauvegardée est n'est pas terminée alors elle est chargée
                                else:
                                    print("[INFO] : La partie a été reprise avec succès") # [DEBUG]
                                    fnt_accueil.fermer()
                                    fnt_accueil = None
                                    fnt_jeu = FntJeu(mode_jeu, Taches.taches[tache_actuelle - 1], Joueurs.joueurs[joueur_actuel])
                                    partie = Partie(mode_jeu, tache_actuelle, fnt_jeu)
                                    fnt_jeu.afficher()
                            # Si la sauvegarde est corrompue par des clés manquantes
                            elif integrite_sauvegarde == 1:
                                print("[WARNING] : La sauvegarde est corrompue ! Une ou plusieurs clés sont manquantes") # [DEBUG]
                                messagebox.showwarning("Planning Poker : Erreur", "La sauvegarde est corrompue ! Une ou plusieurs clés sont manquantes.")
                            # Si la sauvegarde est corrompue par une modification manuelle
                            elif integrite_sauvegarde == 2:
                                print("[WARNING] : La sauvegarde est corrompue ! La sauvegarde a été modifiée manuellement") # [DEBUG]
                                messagebox.showwarning("Planning Poker : Erreur", "La sauvegarde est corrompue ! La sauvegarde a été modifiée manuellement.")

                # Evénements de la fenêtre ConfigJoueurs
                elif fnt_config_joueurs is not None:
                    # Evènement du bouton 'Ajouter un joueur'
                    if fnt_config_joueurs.get_btn_ajouter_joueur().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Ajouter un joueur' cliqué") # [DEBUG]
                        if nb_joueurs < 4:
                            nb_joueurs += 1
                            print("[UPDATE] : Nombre de joueurs : " + str(nb_joueurs)) # [DEBUG]
                            fnt_config_joueurs.ajouter_bs_joueur()
                        elif nb_joueurs == 4:
                            nb_joueurs += 1
                            print("[UDPATE] : Nombre de joueurs : " + str(nb_joueurs)) # [DEBUG]
                            fnt_config_joueurs.ajouter_bs_joueur()
                            fnt_config_joueurs.desactiver_btn_ajouter_joueur()
                        else:
                            print("[WARNING] : Nombre de joueurs maximum atteint") # [DEBUG]
                    
                    # Evènement du bouton 'Supprimer un joueur'
                    elif fnt_config_joueurs.get_btn_supprimer_joueur().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Supprimer un joueur' cliqué") # [DEBUG]
                        if nb_joueurs > 3:
                            nb_joueurs -= 1
                            print("[UPDATE] : Nombre de joueurs : " + str(nb_joueurs)) # [DEBUG]
                            fnt_config_joueurs.supprimer_bs_joueur()
                        elif nb_joueurs == 3:
                            nb_joueurs -= 1
                            print("[UDPATE] : Nombre de joueurs : " + str(nb_joueurs)) # [DEBUG]
                            fnt_config_joueurs.supprimer_bs_joueur()
                            fnt_config_joueurs.desactiver_btn_supprimer_joueur()
                        else:
                            print("[WARNING] : Nombre de joueurs minimum atteint") # [DEBUG]
                
                    # Evènement du bouton 'Valider'
                    elif fnt_config_joueurs.get_btn_valider().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Valider' cliqué") # [DEBUG]
                        
                        Joueurs.joueurs = []
                        # Parcour de toutes les boîtes de saisie
                        for i, boite_saisie in enumerate(fnt_config_joueurs.get_bs_joueurs()):
                            # Création d'un nouveau joueur avec le numéro et le texte de la boîte de saisie comme nom
                            joueur = Joueurs(i+1, boite_saisie.get_texte())

                            # Ajout du joueur à la liste des joueurs
                            Joueurs.joueurs.append(joueur)

                        # Vérification si tous les joueurs ont un nom non vide
                        if all(joueur.nom for joueur in Joueurs.joueurs):
                            
                            print("[INFO] : Liste des joueurs :") # [DEBUG]
                            for joueur in Joueurs.joueurs:
                                print(joueur)
                            
                            fnt_config_joueurs.fermer()
                            fnt_config_joueurs = None
                            fnt_config_taches = FntConfigTaches()
                            fnt_config_taches.afficher()
                            Taches.taches = []
                            nb_taches = 0
                        else:
                            print("[WARNING] : Tous les joueurs doivent avoir un nom") # [DEBUG]
                            fnt_config_joueurs.afficher_msg_erreur("Attention : tous les joueurs doivent avoir un nom !")

                    # Evènement du bouton 'Retour'
                    elif fnt_config_joueurs.get_btn_retour().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Retour' cliqué") # [DEBUG]
                        confirmation = messagebox.askquestion("Planning Poker : Confirmation", "Êtes-vous sûr de vouloir retourner à l'accueil ? Toutes les données renseignées seront perdues !")
                        if confirmation == 'yes':
                            fnt_config_joueurs.fermer()
                            fnt_config_joueurs = None
                            fnt_accueil = FntAccueil()
                            fnt_accueil.afficher()
                            if not os.path.isfile('sauvegarde.json'):
                                sauvegarde = False
                                fnt_accueil.desactiver_btn_reprendre_partie()
                            else:
                                sauvegarde = True

                # Evénements de la fenêtre ConfigTaches
                elif fnt_config_taches is not None:
                    # Evènement du bouton 'Enregistrer cette tâche'
                    if fnt_config_taches.get_btn_enregistrer().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Enregistrer cette tache' cliqué") # [DEBUG]

                        titre = fnt_config_taches.get_bs_titre().get_texte()
                        description = fnt_config_taches.get_bs_description().get_texte()

                        # Vérification si le titre n'est pas vide
                        if titre:
                            # Vérification si la description est vide
                            if not description:
                                description = "Aucune description"  # Définition d'une description par défaut

                            # Enregistrement de la tâche
                            numero = len(Taches.taches) + 1
                            difficulte = None
                            tache = Taches(numero, titre, description, difficulte)
                            Taches.taches.append(tache)

                            # Incrémentation du nombre de tâches
                            nb_taches += 1

                            # Actualisation de l'affichage
                            fnt_config_taches.actualiser_bt_titre(nb_taches+1)
                            fnt_config_taches.actualiser_bt_description(nb_taches+1)
                            fnt_config_taches.reset_bs()
                            print(f"[INFO] : La tâche '{titre}' enregistrée avec succès") # [DEBUG]
                            
                            print("[INFO] : Liste des tâches :") # [DEBUG]
                            for tache in Taches.taches:
                                print(tache)
                        else:
                            print("[WARNING] : Le titre de la tâche ne peut pas être vide") # [DEBUG]
                            fnt_config_taches.afficher_msg_erreur("Attention : le titre de la tâche ne peut pas être vide !")

                    # Evènement du bouton 'Valider'
                    elif fnt_config_taches.get_btn_valider().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Valider' cliqué") # [DEBUG]
                        if nb_taches == 0:
                            fnt_config_taches.afficher_msg_erreur("Attention : aucune tâche n'a été enregistrée !")
                            print("[WARNING] : Aucune tâche enregistrée") # [DEBUG]
                        else:
                            fnt_config_taches.fermer()
                            fnt_config_taches = None
                            joueur_actuel = 0
                            tache_actuelle = 1
                            partie_finie = 0
                            fnt_jeu = FntJeu(mode_jeu, Taches.taches[tache_actuelle - 1], Joueurs.joueurs[joueur_actuel])
                            partie = Partie(mode_jeu, tache_actuelle, fnt_jeu)
                            fnt_jeu.afficher()

                    # Evènement du bouton 'Retour'
                    elif fnt_config_taches.get_btn_retour().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Retour' cliqué") # [DEBUG]
                        confirmation = messagebox.askquestion("Planning Poker : Confirmation", "Êtes-vous sûr de vouloir revenir en arrière ? Toutes les données renseignées seront perdues !")
                        if confirmation == 'yes':
                            fnt_config_taches.fermer()
                            fnt_config_taches = None
                            fnt_config_joueurs = FntConfigJoueurs()
                            fnt_config_joueurs.afficher()
                            nb_joueurs = 2
                            fnt_config_joueurs.desactiver_btn_supprimer_joueur()

                # Evénements de la fenêtre Jeu    
                elif fnt_jeu is not None:
                    # Evènement du plateau de cartes
                    for carte in fnt_jeu.liste_cartes:
                        if carte.est_clique(souris_x, souris_y):
                            # Si la partie n'est pas finie
                            if partie_finie == 0:
                                partie_finie = partie.jouer(carte)
                                # Si la partie est finie avec toutes les tâches traitées
                                if partie_finie == 1:
                                    print("[INFO] : La partie est terminée") # [DEBUG]
                                    fnt_jeu.affichage_fin_jeu(partie_finie)
                                # Si la partie est finie avec une pause café
                                elif partie_finie == 2:
                                    print("[INFO] : La partie a été mise en pause") # [DEBUG]
                                    fnt_jeu.affichage_fin_jeu(partie_finie)

                    # Evènement du bouton 'Quitter la partie'
                    if fnt_jeu.get_btn_quitter().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Quitter la partie' cliqué") # [DEBUG]
                        if partie_finie == 0:
                            confirmation = messagebox.askquestion("Planning Poker : Confirmation", "Êtes-vous sûr de vouloir quitter la partie ? Celle-ci ne sera pas enregistrée !")
                        else:
                            confirmation = 'yes'
                        if confirmation == 'yes':
                            fnt_jeu.fermer()
                            fnt_jeu = None
                            fnt_accueil = FntAccueil()
                            fnt_accueil.afficher()
                            if not os.path.isfile('sauvegarde.json'):
                                sauvegarde = False
                                fnt_accueil.desactiver_btn_reprendre_partie()
                            else:
                                sauvegarde = True
            
            # [EVENEMENT] : Touche du clavier enfoncée
            elif event.type == pygame.KEYDOWN:
                
                # Evènements de la fenêtre ConfigJoueurs
                if fnt_config_joueurs is not None:
                    # Parcour de toutes les boîtes de saisie
                    for i, boite_saisie in enumerate(fnt_config_joueurs.get_bs_joueurs()):
                        if boite_saisie.est_clique(souris_x, souris_y):
                            boite_saisie.evenement(event)
                            print("[UPDATE] Boite de saisie {} : ".format(i+1) + boite_saisie.get_texte()) # [DEBUG]
                
                # Evènements de la fenêtre ConfigTaches
                elif fnt_config_taches is not None:
                    # Evènement de la boîte de saisie 'Titre'
                    if fnt_config_taches.get_bs_titre().est_clique(souris_x, souris_y):
                        fnt_config_taches.get_bs_titre().evenement(event)
                        print("[UPDATE] Boite de saisie 'Titre' : " + fnt_config_taches.get_bs_titre().get_texte()) # [DEBUG]

                    # Evènement de la boîte de saisie 'Description' 
                    elif fnt_config_taches.get_bs_description().est_clique(souris_x, souris_y):
                        fnt_config_taches.get_bs_description().evenement(event)
                        print("[UPDATE] Boite de saisie 'Description' : " + fnt_config_taches.get_bs_description().get_texte()) # [DEBUG]

        pygame.display.flip()
    pygame.quit()