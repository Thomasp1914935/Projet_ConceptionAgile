import pandas as pd
import numpy as np
import tkinter as tk

# Créer la fenêtre principale
fenêtre = tk.Tk()

# Créer un bouton
bouton = tk.Button(fenêtre, text="Lancer la partie")
bouton.pack()

# Définir la fonction appelée lorsque le bouton est cliqué
def lancer_partie():
    print("La partie a été lancée !")

# Attacher la fonction au bouton
bouton.config(command=lancer_partie)

# Afficher la fenêtre
fenêtre.mainloop()

# Spécifier le nombre de joueurs
nb_joueurs = 4

# Créer un DataFrame de taille `nb_joueurs`
df = pd.DataFrame(columns=['carte'], index=[f'Joueur {i}' for i in range(nb_joueurs)])

# Initialiser toutes les valeurs à 0
df['carte'] = np.nan

print(df)