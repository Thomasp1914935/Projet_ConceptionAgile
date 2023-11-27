import tkinter as tk

class FenetreAccueil(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Planning Poker - Accueil")
        self.geometry("500x300")

        # Bouton pour ouvrir la fenêtre Joueur
        self.btn_joueurs = tk.Button(self, text="Lancer une partie", command=self.ouvrir_fenetre_joueurs)
        self.btn_joueurs.pack()

    def ouvrir_fenetre_joueurs(self):
        self.fenetre_joueurs = FenetreJoueurs()
        self.fenetre_joueurs.mainloop()

class FenetreJoueurs(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Paramètres de la partie - Joueurs")
        self.geometry("500x300")

        # Liste des noms des joueurs
        self.noms_joueurs = []

        # Bouton pour ajouter un joueur
        self.btn_ajouter = tk.Button(self, text="Ajouter un joueur", command=self.ajouter_joueur)
        self.btn_ajouter.pack()

        # Crée les paramètres des deux premiers joueurs
        nom_joueur1 = tk.Entry(self)
        nom_joueur2 = tk.Entry(self)

        # Affiche les paramètres des deux premiers joueurs
        nom_joueur1.pack()
        nom_joueur2.pack()

        # Ajoute l'entrée à la liste
        self.noms_joueurs.append(nom_joueur1)
        self.noms_joueurs.append(nom_joueur2)

    def ajouter_joueur(self):
        """
        Ajoute un joueur à la fenêtre.
        """

        # Crée une nouvelle entrée
        nom_joueur = tk.Entry(self)
        nom_joueur.pack()

        # Ajoute l'entrée à la liste
        self.noms_joueurs.append(nom_joueur)

        # Crée un bouton pour supprimer le joueur
        if len(self.noms_joueurs) >= 3:
            btn_supprimer = tk.Button(self, text="Supprimer", command=lambda: self.supprimer_joueur(nom_joueur))
            btn_supprimer.pack()

        # Si le nombre de joueurs est atteint, désactive le bouton d'ajout
        if len(self.noms_joueurs) >= 10:
            self.btn_ajouter.config(state=tk.DISABLED)

    def supprimer_joueur(self, nom_joueur):
        """
        Supprime un joueur de la fenêtre.

        Args:
            entree: L'entrée contenant le nom du joueur à supprimer.
        """

        # Supprime l'entrée de la liste
        self.noms_joueurs.remove(nom_joueur)

        # Supprime l'entrée de la fenêtre
        nom_joueur.destroy()

        # Recherche le bouton supprimé associé à l'entrée
        btn_supprimer = None
        for widget in self.children.values():
            if isinstance(widget, tk.Button):
                btn_supprimer = widget

        # Supprime le bouton de la fenêtre
        if btn_supprimer is not None:
            btn_supprimer.destroy()

        # Si le nombre de joueurs est inférieur à 10, réactive le bouton d'ajout
        if len(self.noms_joueurs) < 10:
            self.btn_ajouter.config(state=tk.NORMAL)

    def ouvrir_fenetre_taches(self):
        """
        Vérifie si le nombre de joueurs est compris entre 2 et 10.

        Args:
            entree: L'entrée contenant le nombre de joueurs.

        Returns:
            True si le nombre de joueurs est valide et change de fenêtre, False sinon.
        """
        try:
            nb_joueurs = int(self.entree_joueurs.get())
            if nb_joueurs >= 2 and nb_joueurs <= 10:
                self.fenetre_taches = FenetreTaches()
                self.fenetre_taches.mainloop()
                return True
            else:
                # messagebox.showerror("Erreur", "Le nombre de joueurs doit être compris entre 2 et 10.")
                return False
        except ValueError:
            return False
        
class FenetreTaches(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Paramètres de la partie - Tâches")
        self.geometry("500x300")

    def mainloop(self):
        super().mainloop()