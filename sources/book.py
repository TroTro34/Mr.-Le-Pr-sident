"""
Module dédié au livre / menu paramètres.

Quand on clique sur le livre, on simule un mouvement de caméra :
la scène "vue de face" s'aplatit et s'envole vers le haut pendant
qu'un bureau "vu de dessus" apparaît en fondu, et le livre se déplace
de sa position de bouton jusqu'au centre de l'écran en grossissant,
pour devenir l'écran de menu (paramètres).

Ce module ne fait pas `import main` : il reçoit tout ce dont il a
besoin (chemin(), largeur, hauteur, la position du bouton livre) à la
construction. C'est main.py qui l'importe et qui pilote l'objet.
"""

import pygame

FERME = "ferme"
OUVERTURE = "ouverture"
OUVERT = "ouvert"
FERMETURE = "fermeture"


def _ease_out(t):
    """Accélère puis ralentit en douceur (0 -> 1)."""
    return 1 - (1 - t) ** 3


class Livre:
    DUREE_OUVERTURE = 40   # frames (~0.75 s à 60 fps)
    DUREE_FERMETURE = 40

    def __init__(self, chemin, largeur, hauteur, rect_bouton):
        """
        chemin          : la fonction chemin() de main.py (pour charger les images)
        largeur/hauteur : dimensions de l'écran
        rect_bouton     : pygame.Rect du bouton livre actuel (position de départ
                          de l'animation), ex: BookBouton.rect
        """
        self.largeur = largeur
        self.hauteur = hauteur

        self.image_livre = pygame.image.load(chemin("book.png")).convert_alpha()
        self.rect_depart = pygame.Rect(rect_bouton)

        # Taille/position du livre une fois posé sur le bureau, vu de dessus
        largeur_ouvert = int(largeur * 0.55)
        hauteur_ouvert = int(hauteur * 0.75)
        self.rect_arrivee = pygame.Rect(0, 0, largeur_ouvert, hauteur_ouvert)
        self.rect_arrivee.center = (largeur // 2, hauteur // 2)
        self.rect_menu = self.rect_arrivee  # repère pour main.py une fois le menu ouvert

        # Fond "bureau vu de dessus" : utilise bureau_dessus.png si dispo,
        # sinon génère un bureau en bois simple pour ne pas bloquer
        try:
            self.fond_dessus = pygame.image.load(chemin("bureau_dessus.png")).convert()
            self.fond_dessus = pygame.transform.scale(self.fond_dessus, (largeur, hauteur))
        except (pygame.error, FileNotFoundError):
            self.fond_dessus = self._generer_fond_bureau()

        self.etat = FERME
        self.chrono = 0
        self.snapshot = None  # capture de l'écran juste avant l'ouverture

    # ------------------------------------------------------------------
    def _generer_fond_bureau(self):
        """Bureau de secours si 'bureau_dessus.png' n'existe pas dans data/."""
        surface = pygame.Surface((self.largeur, self.hauteur))
        bois_clair = (92, 64, 42)
        bois_fonce = (74, 50, 32)
        surface.fill(bois_clair)
        for y in range(0, self.hauteur, 26):
            pygame.draw.rect(surface, bois_fonce, (0, y, self.largeur, 2))
        voile = pygame.Surface((self.largeur, self.hauteur), pygame.SRCALPHA)
        voile.fill((0, 0, 0, 60))
        surface.blit(voile, (0, 0))
        return surface

    # ------------------------------------------------------------------
    def clic_livre(self, snapshot_ecran):
        """À appeler quand le joueur clique sur le bouton livre.
        snapshot_ecran : ecran.copy() pris juste avant l'ouverture (la scène
        'vue de face' qu'on va animer en train de s'envoler)."""
        if self.etat == FERME:
            self.etat = OUVERTURE
            self.chrono = 0
            self.snapshot = snapshot_ecran.copy()

    def clic_fermer(self):
        """À appeler pour refermer le menu (bouton retour, touche Échap...)."""
        if self.etat == OUVERT:
            self.etat = FERMETURE
            self.chrono = 0

    def menu_actif(self):
        """True quand le livre est complètement ouvert : main.py peut alors
        dessiner les options de paramètres par-dessus et ignorer les clics du jeu."""
        return self.etat == OUVERT

    def transition_en_cours(self):
        return self.etat in (OUVERTURE, FERMETURE)

    # ------------------------------------------------------------------
    def _progression(self):
        """Fait avancer l'animation d'une frame et renvoie t (0 = fermé, 1 = ouvert)."""
        if self.etat == OUVERTURE:
            self.chrono += 1
            t = min(1.0, self.chrono / self.DUREE_OUVERTURE)
            if t >= 1.0:
                self.etat = OUVERT
            return _ease_out(t)

        if self.etat == FERMETURE:
            self.chrono += 1
            t = min(1.0, self.chrono / self.DUREE_FERMETURE)
            if t >= 1.0:
                self.etat = FERME
            return 1.0 - _ease_out(t)

        return 1.0 if self.etat == OUVERT else 0.0

    # ------------------------------------------------------------------
    def dessiner(self, ecran):
        """Anime et dessine le livre / la transition caméra. Ne fait rien si fermé."""
        if self.etat == FERME:
            return

        t = self._progression()

        # 1) La scène "de face" s'aplatit et s'envole vers le haut, en s'estompant
        if t < 1.0 and self.snapshot is not None:
            hauteur_vue = max(1, int(self.hauteur * (1 - 0.65 * t)))
            vue_aplatie = pygame.transform.scale(self.snapshot, (self.largeur, hauteur_vue))
            vue_aplatie.set_alpha(int(255 * (1 - t)))
            y = -int(self.hauteur * 0.5 * t)  # part vers le haut, comme une caméra qui monte
            ecran.blit(vue_aplatie, (0, y))

        # 2) Le bureau vu de dessus apparaît en fondu
        fond = self.fond_dessus.copy()
        fond.set_alpha(int(255 * t))
        ecran.blit(fond, (0, 0))

        # 3) Le livre se déplace de sa position bouton -> centre, en grossissant,
        #    et se redresse (vue de face inclinée -> vue de dessus bien droite)
        x = self.rect_depart.centerx + (self.rect_arrivee.centerx - self.rect_depart.centerx) * t
        y = self.rect_depart.centery + (self.rect_arrivee.centery - self.rect_depart.centery) * t
        w = self.rect_depart.width + (self.rect_arrivee.width - self.rect_depart.width) * t
        h = self.rect_depart.height + (self.rect_arrivee.height - self.rect_depart.height) * t

        base = pygame.transform.smoothscale(self.image_livre, (max(1, int(w)), max(1, int(h))))
        angle = 25 * (1 - t)  # incliné au départ, bien à plat une fois arrivé
        image = pygame.transform.rotate(base, angle)
        rect = image.get_rect(center=(x, y))
        ecran.blit(image, rect)
