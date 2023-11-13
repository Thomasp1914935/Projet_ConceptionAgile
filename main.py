import pandas as pd
import numpy as np
import tkinter as tk

# Créer la fenêtre principale
fenetre_accueil = tk.Tk()

# Créer un bouton
bouton_lancer_partie = tk.Button(fenetre_accueil, text="Lancer la partie")
bouton_lancer_partie.pack()

# Définir la fonction appelée lorsque le bouton est cliqué
def lancer_partie():
    fenetre_accueil.withdraw()        # Fermer la fenêtre principale
    fenetre_config_partie.deiconify() # Ouvrir la fenêtre secondaire

# Attacher la fonction au bouton
bouton_lancer_partie.config(command=lancer_partie)

# Créer la fenêtre secondaire
fenetre_config_partie = tk.Toplevel(fenetre_accueil)

# Créer un champ de texte
champ_texte = tk.Entry(fenetre_config_partie)
champ_texte.pack()

# Définir la fonction de validation
def valider(entree):
    try:
        int(entree.get())
        return True
    except ValueError:
        return False

# Attacher la fonction de validation au champ de texte
champ_texte.config(validate="key", validatecommand=(champ_texte, "validate"))

# Créer un bouton
bouton_valider = tk.Button(fenetre_config_partie, text="Valider")
bouton_valider.pack()

# Définir la fonction appelée lorsque le bouton est cliqué
def valider_joueurs():
    # Récupérer le nombre de joueurs
    global nb_joueurs
    nb_joueurs = int(champ_texte.get())

    # Créer un DataFrame de taille `nb_joueurs`
    df = pd.DataFrame(columns=['carte'], index=[f'Joueur {i}' for i in range(nb_joueurs)])

    # Initialiser toutes les valeurs à NaN
    df['carte'] = np.nan

    print(df)

    # Fermer la fenêtre secondaire
    fenetre_config_partie.withdraw()

# Attacher la fonction au bouton
bouton_valider.config(command=valider_joueurs)

# Afficher la fenêtre principale
fenetre_accueil.mainloop()