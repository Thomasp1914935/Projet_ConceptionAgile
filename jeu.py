class Joueurs:
    joueurs = []  # Liste de classe pour stocker tous les joueurs

    # Méthode pour initialiser un joueur
    def __init__(self, numero, nom):
        self.numero = numero
        self.nom = nom

    # [DEBUG]
    def __repr__(self):
        return f"   Joueur {self.numero} : {self.nom}"
    
class Taches:
    taches = []  # Liste de classe pour stocker toutes les tâches

    # Méthode pour initialiser une tâche
    def __init__(self, numero, titre, description, difficulte):
        self.numero = numero
        self.titre = titre
        self.description = description
        self.difficulte = difficulte

    # [DEBUG]
    def __repr__(self):
        return f"Tâche {self.numero} :\n   Titre : {self.titre}\n   Description : {self.description}\n   Difficulté : {self.difficulte}"