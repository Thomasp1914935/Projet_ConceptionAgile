import pandas as pd
import numpy as np
import tkinter as tk

# Créer la fenêtre principale
fenetre_accueil = tk.Tk()
fenetre_accueil.geometry ( '600x200' )

# Créer un bouton
bouton_lancer_partie = tk.Button(fenetre_accueil, text="Lancer la partie")
bouton_lancer_partie.pack()

# Définir la fonction appelée lorsque le bouton est cliqué
def lancer_partie():
    fenetre_accueil.withdraw()        # Fermer la fenêtre principale
    fenetre_config_partie.deiconify() # Ouvrir la fenêtre secondaire
    fenetre_config_partie.geometry ( '600x200' )

# Attacher la fonction au bouton
bouton_lancer_partie.config(command=lancer_partie)

# Créer la fenêtre secondaire
fenetre_config_partie = tk.Toplevel(fenetre_accueil)

# Créer un champ de texte
champ_texte = tk.Entry(fenetre_config_partie)
champ_texte.pack()

# Créer un widget Label
label_message = tk.Label(fenetre_config_partie, text="")
label_message.pack()



# Attacher la fonction de validation au champ de texte
champ_texte.config(validate="key", validatecommand=(champ_texte, "validate"))

# Créer un bouton
bouton_valider = tk.Button(fenetre_config_partie, text="Valider")
bouton_valider.pack()

# Définir la fonction de validation
def valider(entree):
    try:
        nb_joueurs = int(entree.get())
        return nb_joueurs >= 2 and nb_joueurs <= 10
    except ValueError:
        return False

# Définir la fonction appelée lorsque le bouton est cliqué
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

    # Fermer la fenêtre principale
    fenetre_accueil.destroy()


# Attacher la fonction au bouton
bouton_valider.config(command=valider_joueurs)

# Afficher la fenêtre principale
fenetre_accueil.mainloop()

