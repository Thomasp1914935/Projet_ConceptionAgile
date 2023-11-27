import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np

from jeu import joueur

def valider(entree):
    try:
        nb_joueurs = int(entree.get())
        return nb_joueurs >= 2 and nb_joueurs <= 10
    except ValueError:
        return False

def valider_joueurs():
    # Récupérer le nombre de joueurs
    global nb_joueurs
    nb_joueurs = int(champ_texte.get())

    # Vérifier que le nombre de joueurs est valide
    if not valider(champ_texte):
        message_erreur = "Le nombre de joueurs doit être compris entre 2 et 10."
        label_message.config(text=message_erreur)
        champ_texte.config(bg="red")
        return

    # Créer un DataFrame de taille `nb_joueurs`
    df = pd.DataFrame(columns=['carte'], index=[f'Joueur {i}' for i in range(nb_joueurs)])

    # Initialiser toutes les valeurs à NaN
    df['carte'] = np.nan

    print(df)

    # Fermer la fenêtre secondaire
    fenetre_config_partie.withdraw()

    # Appeler la fonction pour afficher les noms des joueurs
    afficher_noms_joueurs()


def afficher_noms_joueurs():
    # Créer une nouvelle fenêtre
    fenetre_noms_joueurs = tk.Toplevel(fenetre_accueil)

    # Créer un Label pour chaque joueur
    labels_joueurs = [tk.Label(fenetre_noms_joueurs, text=f"Joueur {i} : ") for i in range(nb_joueurs)]

    # Créer un Entry pour chaque joueur
    entries_joueurs = [tk.Entry(fenetre_noms_joueurs) for _ in range(nb_joueurs)]

    # Placer les Labels et les Entries dans la fenêtre
    for i in range(nb_joueurs):
        labels_joueurs[i].grid(row=i, column=0)
        entries_joueurs[i].grid(row=i, column=1)

        


    # Afficher la fenêtre
    fenetre_noms_joueurs.mainloop()


# Créer la fenêtre principale
fenetre_accueil = tk.Tk()
fenetre_accueil.geometry('600x200')

# Créer un bouton
bouton_lancer_partie = tk.Button(fenetre_accueil, text="Lancer la partie")
bouton_lancer_partie.pack()

# Définir la fonction appelée lorsque le bouton est cliqué
def lancer_partie():
    fenetre_accueil.withdraw()        # Fermer la fenêtre principale
    fenetre_config_partie.deiconify() # Ouvrir la fenêtre secondaire
    fenetre_config_partie.geometry('600x200')

# Attacher la fonction au bouton
bouton_lancer_partie.config(command=lancer_partie)

# Créer la fenêtre secondaire
fenetre_config_partie = tk.Toplevel(fenetre_accueil)

# Créer un champ de texte
champ_texte = tk.Entry(fenetre_config_partie)
champ_texte.pack()

# Créer un Label
label_message = tk.Label(fenetre_config_partie, text="")
label_message.pack()

# Créer un bouton
bouton_valider = tk.Button(fenetre_config_partie, text="Valider", command=valider_joueurs)
bouton_valider.pack()

# Lancement de l'application
fenetre_accueil.mainloop()