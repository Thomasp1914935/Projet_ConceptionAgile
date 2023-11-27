class Joueur:
    def __init__(self, numero, nom):
        self.numero = numero
        self.nom = nom

    def __repr__(self):
        return f"Joueur {self.numero} : {self.nom}"