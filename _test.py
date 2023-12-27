import pytest
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

from fenetres import FntJeu
from jeu import Joueurs, Taches, Cartes, Partie

def test_jouer():
    # Créer les objets nécessaires pour l'état global
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

    # Vérifier que la partie est correctement initialisée
    assert partie.mode == "strict"
    assert partie.joueur_actuel == 0
    assert partie.cartes_choisies == []
    assert partie.log_cartes_choisies == []
    assert partie.tache_actuelle == 1
    assert partie.premier_tour == True
    assert partie.partie_finie == False
    assert partie.fenetre == fenetre

    # Vérifier que self.tache_actuelle est bien inférieur ou égal à len(Taches.taches)
    assert partie.tache_actuelle <= len(Taches.taches)

    # Jouer la carte
    resultat = partie.jouer(carte)

    # Vérifier que la carte a été ajoutée à cartes_choisies et log_cartes_choisies
    assert carte in partie.cartes_choisies
    assert carte in partie.log_cartes_choisies

    # Vérifier que le joueur actuel a été incrémenté
    assert partie.joueur_actuel == 1

    # Vérifier que le résultat est celui attendu
    assert resultat == 0

def test_fin_tour():
    # Créer les objets nécessaires pour l'état global
    mode = "strict"
    joueur1 = Joueurs(numero=1, nom="Joueur 1")
    joueur2 = Joueurs(numero=2, nom="Joueur 2")
    Joueurs.joueurs.append(joueur1)
    Joueurs.joueurs.append(joueur2)
    tache = Taches(numero=1, titre="Titre de la tâche", description="Description de la tâche", difficulte=None)
    Taches.taches.append(tache)
    fenetre = FntJeu(mode_jeu=mode, tache=tache, joueur=joueur1)
    carte1 = Cartes(nom_carte="0", position=(1,1), fenetre=fenetre)
    carte2 = Cartes(nom_carte="0", position=(1,1), fenetre=fenetre)
    partie = Partie(mode=mode, tache_actuelle=tache.numero, fenetre=fenetre)

    # Jouer les cartes
    partie.jouer(carte1)
    partie.jouer(carte2)

    # Vérifier que fin_tour retourne True
    assert partie.fin_tour() == True

    # Vérifier que la difficulté de la tâche a été mise à jour
    assert Taches.taches[0].difficulte == 0

    # Vérifier que tache_actuelle a été incrémenté
    assert partie.tache_actuelle == 2

    # Vérifier que premier_tour est toujours True
    assert partie.premier_tour == True