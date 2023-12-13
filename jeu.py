class Joueurs:
    joueurs = []  # Liste de classe pour stocker tous les joueurs

    # Méthode pour initialiser un joueur
    def __init__(self, numero, nom):
        self.numero = numero
        self.nom = nom

    # [DEBUG]
    def __repr__(self):
        return f"Joueur {self.numero} : {self.nom}"