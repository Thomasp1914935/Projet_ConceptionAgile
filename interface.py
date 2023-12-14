import os
import pygame
import textwrap

# Initialisation de toutes les bibliothèques Pygame et leurs modules associés
pygame.init()
pygame.font.init()

class Fenetre:
    # Méthode pour initialiser la fenêtre
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))

        # Charger l'image de l'icône
        chemin_script = os.path.dirname(__file__)
        chemin_icone = (chemin_script, 'ressources', 'icone.png')
        chemin_icone = os.path.join(os.path.sep, *chemin_icone)
        icone = pygame.image.load(chemin_icone)
        pygame.display.set_icon(icone)

    # Méthode pour définir le titre de la fenêtre
    def set_titre(self, titre):
        pygame.display.set_caption(titre)
    
    # Méthode pour définir la couleur de fond de la fenêtre
    def set_couleur_fond(self, couleur):
        self.fenetre.fill(couleur)

    # Méthode pour afficher/mettre à jour la fenêtre
    def afficher(self):
        pygame.display.flip()
    
    # Méthode pour fermer la fenêtre
    def fermer(self):
        pygame.display.quit()

class Bouton:
    # Méthode pour initialiser un bouton
    def __init__(self, x, y, largeur, hauteur, texte, taille_police, couleur_texte, couleur_bouton, fenetre):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.texte = texte
        self.taille_police = taille_police
        self.couleur_texte = couleur_texte
        self.couleur_bouton = couleur_bouton
        self.fenetre = fenetre

    # Méthode pour dessiner un bouton
    def dessiner(self):
        rayon = self.hauteur // 2
        pygame.draw.ellipse(self.fenetre, self.couleur_bouton, (self.x, self.y, 2*rayon, 2*rayon))  # Coin supérieur gauche
        pygame.draw.ellipse(self.fenetre, self.couleur_bouton, (self.x + self.largeur - 2*rayon, self.y, 2*rayon, 2*rayon))  # Coin supérieur droit
        pygame.draw.ellipse(self.fenetre, self.couleur_bouton, (self.x, self.y + self.hauteur - 2*rayon, 2*rayon, 2*rayon))  # Coin inférieur gauche
        pygame.draw.ellipse(self.fenetre, self.couleur_bouton, (self.x + self.largeur - 2*rayon, self.y + self.hauteur - 2*rayon, 2*rayon, 2*rayon))  # Coin inférieur droit
        pygame.draw.rect(self.fenetre, self.couleur_bouton, (self.x, self.y + rayon, self.largeur, self.hauteur - 2*rayon))  # Partie centrale verticale
        pygame.draw.rect(self.fenetre, self.couleur_bouton, (self.x + rayon, self.y, self.largeur - 2*rayon, self.hauteur))  # Partie centrale horizontale

        police = pygame.font.Font(None, self.taille_police)
        texte = police.render(self.texte, True, self.couleur_texte)
        self.fenetre.blit(texte, (self.x + (self.largeur - texte.get_width()) // 2, self.y + (self.hauteur - texte.get_height()) // 2))
    
    # Méthode pour vérifier si un bouton est survolé
    def est_survole(self, souris_x, souris_y):
        if self.x <= souris_x <= self.x + self.largeur and self.y <= souris_y <= self.y + self.hauteur:
            return True
        else:
            return False

    # Méthode pour vérifier si un bouton est cliqué
    def est_clique(self, x, y):
        return self.x <= x <= self.x + self.largeur and self.y <= y <= self.y + self.hauteur
    
class BoiteTexte:
    # Méthode pour initialiser une boîte de texte
    def __init__(self, x, y, texte, taille_police, couleur, texte_centre, fenetre):
        self.x = x
        self.y = y
        self.texte = texte
        self.taille_police = taille_police
        self.police = pygame.font.Font(None, self.taille_police)
        self.texte_surface = self.police.render(texte, True, couleur)
        self.couleur = couleur
        self.texte_centre = texte_centre
        self.fenetre = fenetre

    # Méthode pour dessiner une boîte de texte
    def dessiner(self):
        if self.texte_centre:
            x_centre = self.x - self.texte_surface.get_width() / 2
            pygame.draw.rect(self.fenetre, (255, 255, 255), (x_centre, self.y - self.texte_surface.get_height(), self.police.size(self.texte)[0], self.police.size(self.texte)[1]))
        else:
            x_centre = self.x
            pygame.draw.rect(self.fenetre, (255, 255, 255), (x_centre, self.y - self.texte_surface.get_height(), self.police.size(self.texte)[0], self.police.size(self.texte)[1]))
        self.fenetre.blit(self.texte_surface, (x_centre, self.y - self.texte_surface.get_height()))

    # Méthode pour obtenir la taille de la boîte de texte
    def get_taille(self):
        return self.texte_surface.get_size()

    # Méthode pour réinitialiser le texte d'une boîte de saisie
    def reset_texte(self):
        self.texte = ""  # Réinitialiser le contenu
        self.dessiner()  # Redessiner la boîte de saisie
    
class BoiteSaisie:
    # Méthode pour initialiser une boîte de saisie
    def __init__(self, x, y, largeur, hauteur, taille_police, couleur, max_caracteres, longueur_ligne, fenetre):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.couleur = couleur
        self.police = pygame.font.Font(None, taille_police)
        self.texte = ""
        self.max_caracteres = max_caracteres
        self.longueur_ligne = longueur_ligne
        self.fenetre = fenetre

    # Méthode pour dessiner une boîte de saisie
    def dessiner(self):
        # Dessiner un rectangle avec des bords arrondis
        pygame.draw.rect(self.fenetre, self.couleur, (self.x, self.y, self.largeur, self.hauteur), 2, border_radius=20)

        # Effacer l'ancien texte en dessinant un rectangle de la couleur d'arrière-plan
        pygame.draw.rect(self.fenetre, (255, 255, 255), (self.x + 10, self.y + 5, self.largeur - 20, self.hauteur - 10))

        # Dessiner le texte
        lines = textwrap.wrap(self.texte, self.longueur_ligne)  # Découper le texte en lignes
        y = self.y + 5
        for line in lines:
            texte_surface = self.police.render(line, True, (0, 0, 0))
            self.fenetre.blit(texte_surface, (self.x + 10, y))
            y += self.police.get_height()  # Passer à la ligne suivante

    # Méthode pour remplir une boîte de saisie
    def evenement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.texte = self.texte[:-1]
            else:
                if len(self.texte) < self.max_caracteres:
                    self.texte += event.unicode
        self.dessiner()

    # Méthode pour vérifier si un bouton est survolé
    def est_survole(self, souris_x, souris_y):
        if self.x <= souris_x <= self.x + self.largeur and self.y <= souris_y <= self.y + self.hauteur:
            return True
        else:
            return False

    # Méthode pour vérifier si une boîte de saisie est cliquée
    def est_clique(self, x, y):
        return self.x <= x <= self.x + self.largeur and self.y <= y <= self.y + self.hauteur

    # Méthode pour récupérer le texte d'une boîte de saisie
    def get_texte(self):
        return self.texte
    
    # Méthode pour réinitialiser le texte d'une boîte de saisie
    def reset_texte(self):
        self.texte = ""  # Réinitialiser le contenu
        self.dessiner()  # Redessiner la boîte de saisie