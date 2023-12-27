import pytest
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

from fenetres import FntJeu
from jeu import Joueurs, Taches, Cartes, Partie

def test_jouer():
    """
    Vérifie que le choix d'une carte par un joueur est correctement implémenté.
    Cela permet de vérifier en détails que la méthode jouer ajoute bien la carte à cartes_choisies et log_cartes_choisies, et incrémente bien joueur_actuel.
    """
    # Création des objets nécessaires pour l'état global
    mode = "strict"
    joueur1 = Joueurs(numero=1, nom="Joueur 1")
    joueur2 = Joueurs(numero=2, nom="Joueur 2")
    Joueurs.joueurs.append(joueur1)
    Joueurs.joueurs.append(joueur2)
    tache = Taches(numero=1, titre="Titre de la tâche", description="Description de la tâche", difficulte=None)
    Taches.taches.append(tache)
    fenetre = FntJeu(mode_jeu=mode, tache=tache, joueur=joueur1)
    carte = Cartes(nom_carte="0", position=(1,1), fenetre=fenetre)
    partie = Partie(mode=mode, tache_actuelle=tache.numero, fenetre=fenetre)

    # Vérification que la partie est correctement initialisée
    assert partie.mode == "strict"
    assert partie.joueur_actuel == 0
    assert partie.cartes_choisies == []
    assert partie.log_cartes_choisies == []
    assert partie.tache_actuelle == 1
    assert partie.premier_tour == True
    assert partie.partie_finie == False
    assert partie.fenetre == fenetre

    # Vérification que self.tache_actuelle est bien inférieur ou égal à len(Taches.taches)
    assert partie.tache_actuelle <= len(Taches.taches)

    # Joue la carte
    resultat = partie.jouer(carte)

    # Vérification que la carte a été ajoutée à cartes_choisies et log_cartes_choisies
    assert carte in partie.cartes_choisies
    assert carte in partie.log_cartes_choisies

    # Vérification que le joueur actuel a été incrémenté
    assert partie.joueur_actuel == 1

    # Vérification que le résultat est celui attendu
    assert resultat == 0

def test_fin_tour():
    """
    Vérifie que la règle de fin de tour choisie est correctement implémentée.
    Cela permet de vérifier en détails que la méthode fin_tour met bien à jour la difficulté de la tâche et tache_actuelle, et réinitialise bien premier_tour.
    """
    # Création des objets nécessaires pour l'état global
    mode = "strict" # Paramètre à changer en fonction du test voulu
    joueur1 = Joueurs(numero=1, nom="Joueur 1")
    joueur2 = Joueurs(numero=2, nom="Joueur 2")
    Joueurs.joueurs.append(joueur1)
    Joueurs.joueurs.append(joueur2)
    tache = Taches(numero=1, titre="Titre de la tâche", description="Description de la tâche", difficulte=None)
    Taches.taches.append(tache)
    fenetre = FntJeu(mode_jeu=mode, tache=tache, joueur=joueur1)
    carte0 = Cartes(nom_carte="0", position=(0,0), fenetre=fenetre)
    carte1 = Cartes(nom_carte="1", position=(1,1), fenetre=fenetre)
    carte2 = Cartes(nom_carte="2", position=(2,2), fenetre=fenetre)
    carte3 = Cartes(nom_carte="3", position=(3,3), fenetre=fenetre)
    carte5 = Cartes(nom_carte="5", position=(5,5), fenetre=fenetre)
    carte8 = Cartes(nom_carte="8", position=(8,8), fenetre=fenetre)
    carte13 = Cartes(nom_carte="13", position=(13,13), fenetre=fenetre)
    carte20 = Cartes(nom_carte="20", position=(20,20), fenetre=fenetre)
    carte40 = Cartes(nom_carte="40", position=(40,40), fenetre=fenetre)
    carte100 = Cartes(nom_carte="100", position=(100,100), fenetre=fenetre)
    partie = Partie(mode=mode, tache_actuelle=tache.numero, fenetre=fenetre)

    # Joue les cartes
    partie.jouer(carte0) # Paramètre à changer en fonction du test voulu
    partie.jouer(carte0) # Paramètre à changer en fonction du test voulu

    # Vérification que fin_tour retourne True
    assert partie.fin_tour() == True

    # Vérification que la difficulté de la tâche a été mise à jour
    assert Taches.taches[0].difficulte == 0 # Paramètre à changer en fonction du test voulu

    # Vérification que tache_actuelle a été incrémenté
    assert partie.tache_actuelle == 2

    # Vérification que premier_tour est toujours True
    assert partie.premier_tour == True

def test_fin_partie():
    """
    Vérifie que la méthode fin_partie réinitialise correctement les attributs de l'objet Partie.
    Cela permet de vérifier en détails que la méthode fin_partie réinitialise bien les attributs de l'objet Partie.
    """
    # Création des objets nécessaires pour l'état global
    mode = "strict"
    joueur1 = Joueurs(numero=1, nom="Joueur 1")
    joueur2 = Joueurs(numero=2, nom="Joueur 2")
    Joueurs.joueurs.append(joueur1)
    Joueurs.joueurs.append(joueur2)
    tache = Taches(numero=1, titre="Titre de la tâche", description="Description de la tâche", difficulte=None)
    Taches.taches.append(tache)
    fenetre = FntJeu(mode_jeu=mode, tache=tache, joueur=joueur1)
    partie = Partie(mode=mode, tache_actuelle=tache.numero, fenetre=fenetre)

    # Définition des attributs de l'objet Partie
    partie.partie_finie = True
    partie.joueur_actuel = joueur1
    partie.cartes_choisies = ["carte1", "carte2"]
    partie.log_cartes_choisies = ["carte1", "carte2"]
    partie.tache_actuelle = 1

    # Appel de la méthode fin_partie
    partie.fin_partie()

    # Vérification que les attributs de l'objet Partie ont été correctement réinitialisés
    assert partie.joueur_actuel is None
    assert partie.cartes_choisies == []
    assert partie.log_cartes_choisies == []
    assert partie.tache_actuelle is None