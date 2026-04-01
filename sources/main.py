#Projet : Mr.Le Président
#Auteurs: Maxence Tropia-Party, Apolline Bec, Laura Leonor

import pygame
import random
import os


BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def chemin(fichier):
    return os.path.join(BASE, "data", fichier)

pygame.init()

Arme = 100
Population = 100
eco = 100
envi = 100
ImpacteJauge = 20

info = pygame.display.Info()
largeur = info.current_w
hauteur = info.current_h
ecran = pygame.display.set_mode((largeur, hauteur))
background = pygame.image.load(chemin("Background.jpeg")).convert()
background = pygame.transform.scale(background, (largeur, hauteur))
pygame.display.set_caption("Mr.President")
icon = pygame.image.load(chemin("Logo.jpg")).convert_alpha()
pygame.display.set_icon(icon)
close = False

ChoixHistoire = {
    "Question1": False,
    "Question2": False,
    "Question3": False,
    "Question4": False,
    "Question5": False,
}

timerType = pygame.time.Clock()

FinListe = []
Prentation = []
Happen = []
StartDialogue = []
TextSpe = []
finJeu = []


def charger_fichier(nom, liste):
    with open(chemin(nom), "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            liste.append(ligne.strip())


charger_fichier("histoire.txt", Prentation)
charger_fichier("question.txt", Happen)
charger_fichier("intro.txt", StartDialogue)
charger_fichier("Fins.txt", FinListe)
charger_fichier("textspe.txt", TextSpe)
charger_fichier("FinJEU.txt", finJeu)

randomP = random.randint(0, len(Happen) - 1)
startIndex = 1
WitchDialogue = StartDialogue[0]
QuestionNumbers = 0
counter = 0
speed = 1
ancient = 0

AvantGame = False
Done = False
Start = False
Question = False
Pres = False


NbQavantSpe = 6
NbGenAvantPartie2 = 3
choix_assistant = 0
generationCount = 0
FinJeu = False
IndexFin = -1
Partie1Active = False
NombreTextSpe = 0
TextSpeIndex = 0
SuiteTextSpe = False
QuestionSpe = False

GameOver = False
gameOverText = ""
gameOverCounter = 0
gameOverDone = False

gameOverSpeed = 2
fadeOutDuration = 75
fadeOutCounter = 0
fadeOutDone = False

gameOverEndTime = None

yesImage = pygame.image.load(chemin("vraiYES.png")).convert_alpha()
noImage = pygame.image.load(chemin("vraiNON.png")).convert_alpha()

General           = list(range(9,  18))
MinistrEnvi       = list(range(0,  9))
MinistrFinance    = list(range(18, 27))
MinistrPopulation = list(range(27, 36))


# --- Choix du personnage à afficher selon le dialogue actuel ---
def personnages():
    global choix_assistant

    if WitchDialogue in (StartDialogue[0], StartDialogue[1]):
        return None

    if WitchDialogue in TextSpe:
        indices_assistant = [33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 59, 60, 66, 67, 68]
        if WitchDialogue in [TextSpe[i] for i in indices_assistant if i < len(TextSpe)]:
            fichier = chemin("Assistant.png")
        else:
            fichier = chemin("Général.png")

    elif WitchDialogue in StartDialogue:
        choix_assistant = random.randint(0, 2)
        fichier = chemin("Assistant2.png") if choix_assistant == 0 else chemin("Assistant.png")

    elif WitchDialogue in [Happen[i] for i in General if i < len(Happen)]:
        fichier = chemin("Général2.png")
    elif WitchDialogue in [Prentation[i] for i in General if i < len(Prentation)]:
        fichier = chemin("Général.png")

    elif WitchDialogue in [Happen[i] for i in MinistrEnvi if i < len(Happen)]:
        fichier = chemin("Assistant2.png") if choix_assistant == 1 else chemin("Ecologie2.png")
    elif WitchDialogue in [Prentation[i] for i in MinistrEnvi if i < len(Prentation)]:
        choix_assistant = random.randint(0, 2)
        fichier = chemin("Assistant.png") if choix_assistant == 1 else chemin("Ecologie.png")

    elif WitchDialogue in [Happen[i] for i in MinistrFinance if i < len(Happen)]:
        fichier = chemin("Assistant2.png") if choix_assistant == 1 else chemin("Finance2.png")
    elif WitchDialogue in [Prentation[i] for i in MinistrFinance if i < len(Prentation)]:
        choix_assistant = random.randint(0, 2)
        fichier = chemin("Assistant.png") if choix_assistant == 1 else chemin("Finance.png")

    elif WitchDialogue in [Happen[i] for i in MinistrPopulation if i < len(Happen)]:
        fichier = chemin("Assistant2.png") if choix_assistant == 1 else chemin("Population2.png")
    elif WitchDialogue in [Prentation[i] for i in MinistrPopulation if i < len(Prentation)]:
        choix_assistant = random.randint(0, 2)
        fichier = chemin("Assistant.png") if choix_assistant == 1 else chemin("Population.png")

    elif WitchDialogue in Prentation:
        fichier = chemin("Assistant.png")

    else:
        return None

    img = pygame.image.load(fichier).convert_alpha()
    max_h = int(hauteur * 0.55)
    ratio = max_h / img.get_height()
    new_w = int(img.get_width() * ratio)
    return pygame.transform.scale(img, (new_w, max_h))


# --- Taille de la police selon la longueur du dialogue ---
def size():
    global WitchDialogue, Start
    taille = 22
    if Start and len(WitchDialogue) > 110:
        taille = 20
    return taille


# --- Découpe un texte long en plusieurs lignes ---
def wrap_text(texte, font, max_width):
    mots = texte.split(" ")
    lignes = []
    ligne_courante = ""
    for mot in mots:
        test = ligne_courante + (" " if ligne_courante else "") + mot
        if font.size(test)[0] <= max_width:
            ligne_courante = test
        else:
            if ligne_courante:
                lignes.append(ligne_courante)
            ligne_courante = mot
    if ligne_courante:
        lignes.append(ligne_courante)
    return lignes


# --- Affiche la boîte de dialogue semi-transparente en bas ---
def boxe():
    surface = pygame.Surface((largeur, 300), pygame.SRCALPHA)
    surface.fill((0, 0, 0, 160))
    ecran.blit(surface, (0, 780))


# --- Fondu noir progressif avant l'écran de mort ---
def afficher_fadeout():
    global fadeOutCounter, fadeOutDone

    fadeOutCounter += 1
    alpha_noir = min(255, int((fadeOutCounter / fadeOutDuration) * 255))

    ecran.blit(background, (0, 0))
    boxe()
    font = pygame.font.Font(chemin("Capture it.ttf"), size())
    snip = font.render(WitchDialogue[0:counter // speed], True, (0, 0, 0))
    ecran.blit(snip, (30, 820))

    voile = pygame.Surface((largeur, hauteur))
    voile.fill((0, 0, 0))
    voile.set_alpha(alpha_noir)
    ecran.blit(voile, (0, 0))

    if fadeOutCounter >= fadeOutDuration:
        fadeOutDone = True


# --- Écran de mort par jauge (texte défilant sur fond noir) ---
def afficher_game_over():
    global gameOverCounter, gameOverEndTime

    ecran.fill((0, 0, 0))

    if gameOverCounter < gameOverSpeed * len(gameOverText):
        gameOverCounter += 1

    font_go = pygame.font.Font(chemin("Capture it.ttf"), 30)
    texte_affiche = gameOverText[0:gameOverCounter // gameOverSpeed]

    marge = 200
    lignes = wrap_text(texte_affiche, font_go, largeur - marge * 2)

    total_chars = gameOverSpeed * len(gameOverText)
    alpha = min(255, int((gameOverCounter / total_chars) * 255)) if total_chars > 0 else 255

    hauteur_ligne = font_go.get_linesize() + 8
    total_hauteur = len(lignes) * hauteur_ligne
    y_depart = (hauteur - total_hauteur) // 2

    for i, ligne in enumerate(lignes):
        surf_ligne = font_go.render(ligne, True, (255, 255, 255))
        surf_ligne.set_alpha(alpha)
        rect_ligne = surf_ligne.get_rect(center=(largeur // 2, y_depart + i * hauteur_ligne))
        ecran.blit(surf_ligne, rect_ligne)

    if gameOverCounter >= gameOverSpeed * len(gameOverText):
        if gameOverEndTime is None:
            gameOverEndTime = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - gameOverEndTime >= 3000:
            gameOverEndTime = None
            restart()


# --- Écran de fin narrative (texte selon l'index de fin atteint) ---
def fin():
    global fadeOutCounter, fadeOutDone, gameOverText, gameOverCounter

    indices_fin = [55, 57, 60, 48, 68, 72, 75, 79, 104, 112, 126, 135]

    if gameOverText == "":
        if IndexFin in indices_fin:
            gameOverText = finJeu[indices_fin.index(IndexFin)]
        else:
            gameOverText = "Fin."
        gameOverCounter = 0
        pygame.time.wait(1500)

    if not fadeOutDone:
        afficher_fadeout()
    else:
        afficher_game_over()



def restart():
    global Arme, Population, eco, envi, GameOver, FinJeu, gameOverText
    global gameOverCounter, gameOverDone, fadeOutCounter, gameOverEndTime
    global fadeOutDone, Start, Pres, Question, QuestionNumbers, counter
    global Done, startIndex, AvantGame, generationCount, NombreTextSpe
    global TextSpeIndex, SuiteTextSpe, QuestionSpe, Partie1Active, IndexFin
    global ancient, randomP, WitchDialogue

    Arme = 100; Population = 100; eco = 100; envi = 100
    GameOver = False; FinJeu = False
    gameOverText = ""; gameOverCounter = 0; gameOverDone = False
    fadeOutCounter = 0; fadeOutDone = False
    gameOverEndTime = None
    Start = False; Pres = False; Question = False
    QuestionNumbers = 0; counter = 0; Done = False
    startIndex = 1; AvantGame = False
    generationCount = 0; NombreTextSpe = 0; TextSpeIndex = 0
    SuiteTextSpe = False; QuestionSpe = False
    Partie1Active = False; IndexFin = -1
    ancient = 0; randomP = random.randint(0, len(Happen) - 1)
    WitchDialogue = StartDialogue[0]
    for k in ChoixHistoire: ChoixHistoire[k] = False




# --- Écran de menu principal ---
def menu():
    ecran.fill((0, 0, 0))
    font = pygame.font.Font(chemin("Capture it.ttf"), 50)
    titre = font.render("Mr. President", True, (255, 255, 255))
    ecran.blit(titre, (largeur // 2 - titre.get_width() // 2, 300))
    sous_titre = font.render("Cliquez pour commencer", True, (200, 200, 200))
    ecran.blit(sous_titre, (largeur // 2 - sous_titre.get_width() // 2, 500))


def choixSpe(clic_oui, clic_non):
    global QuestionSpe, NombreTextSpe, QuestionNumbers, SuiteTextSpe, Question

    if clic_oui:
        if NombreTextSpe == 2:
            ChoixHistoire["Question2"] = True
        elif NombreTextSpe == 3:
            ChoixHistoire["Question3"] = True
        elif NombreTextSpe == 4:
            ChoixHistoire["Question4"] = True
        elif NombreTextSpe == 5:
            ChoixHistoire["Question5"] = True
        elif NombreTextSpe == 6:
            ChoixHistoire["Question4"] = True
        elif NombreTextSpe == 8:
            ChoixHistoire["Question2"] = True
        elif NombreTextSpe == 9:
            ChoixHistoire["Question3"] = True
        QuestionSpe = False
        Question = False
        QuestionNumbers = 0
        if NombreTextSpe == 6:
            SuiteTextSpe = True
            textspecial()
        else:
            SuiteTextSpe = False
            text()

    elif clic_non:
        if NombreTextSpe == 2:
            ChoixHistoire["Question2"] = False
        elif NombreTextSpe == 3:
            ChoixHistoire["Question3"] = False
        elif NombreTextSpe == 4:
            ChoixHistoire["Question4"] = False
        elif NombreTextSpe == 5:
            ChoixHistoire["Question5"] = False
        elif NombreTextSpe == 6:
            ChoixHistoire["Question4"] = False
        elif NombreTextSpe == 8:
            ChoixHistoire["Question2"] = False
        elif NombreTextSpe == 9:
            ChoixHistoire["Question3"] = False
        QuestionSpe = False
        Question = False
        QuestionNumbers = 0
        if NombreTextSpe == 6:
            SuiteTextSpe = True
            textspecial()
        else:
            SuiteTextSpe = False
            text()


# --- Gestion des choix normaux (jauges) ---
def choixjoueur(clic_oui, clic_non):
    global Arme, Population, eco, envi
    global Question, ancient, SuiteTextSpe, QuestionNumbers, ImpacteJauge
    global generationCount

    if clic_oui and not SuiteTextSpe:
        if ancient in [0, 1, 2]:
            envi += ImpacteJauge; Arme -= ImpacteJauge
        elif ancient in [3, 4, 5]:
            envi += ImpacteJauge; eco -= ImpacteJauge
        elif ancient in [6, 7, 8]:
            envi += ImpacteJauge; Population -= ImpacteJauge
        elif ancient in [9, 10, 11]:
            Arme += ImpacteJauge; Population -= ImpacteJauge
        elif ancient in [12, 13, 14]:
            Arme += ImpacteJauge; eco -= ImpacteJauge
        elif ancient in [15, 16, 17]:
            Arme += ImpacteJauge; envi -= ImpacteJauge
        elif ancient in [18, 19, 20]:
            eco += ImpacteJauge; Arme -= ImpacteJauge
        elif ancient in [21, 22, 23]:
            eco += ImpacteJauge; Population -= ImpacteJauge
        elif ancient in [24, 25, 26]:
            eco += ImpacteJauge; envi -= ImpacteJauge
        elif ancient in [27, 28, 29]:
            Population += ImpacteJauge; Arme -= ImpacteJauge
        elif ancient in [30, 31, 32]:
            Population += ImpacteJauge; eco -= ImpacteJauge
        elif ancient in [33, 34, 35]:
            Population += ImpacteJauge; envi -= ImpacteJauge
        Question = False
        QuestionNumbers += 1
        print(f"[OUI] Arme={Arme} | Population={Population} | Eco={eco} | Environnement={envi}")
        text()

    elif clic_non and not SuiteTextSpe:
        if ancient in [0, 1, 2]:
            envi -= ImpacteJauge; Arme += ImpacteJauge
        elif ancient in [3, 4, 5]:
            envi -= ImpacteJauge; eco += ImpacteJauge
        elif ancient in [6, 7, 8]:
            envi -= ImpacteJauge; Population += ImpacteJauge
        elif ancient in [9, 10, 11]:
            Arme -= ImpacteJauge; Population += ImpacteJauge
        elif ancient in [12, 13, 14]:
            Arme -= ImpacteJauge; eco += ImpacteJauge
        elif ancient in [15, 16, 17]:
            Arme -= ImpacteJauge; envi += ImpacteJauge
        elif ancient in [18, 19, 20]:
            eco -= ImpacteJauge; Arme += ImpacteJauge
        elif ancient in [21, 22, 23]:
            eco -= ImpacteJauge; Population += ImpacteJauge
        elif ancient in [24, 25, 26]:
            eco -= ImpacteJauge; envi += ImpacteJauge
        elif ancient in [27, 28, 29]:
            Population -= ImpacteJauge; Arme += ImpacteJauge
        elif ancient in [30, 31, 32]:
            Population -= ImpacteJauge; eco += ImpacteJauge
        elif ancient in [33, 34, 35]:
            Population -= ImpacteJauge; envi += ImpacteJauge
        Question = False
        QuestionNumbers += 1
        print(f"[NON] Arme={Arme} | Population={Population} | Eco={eco} | Environnement={envi}")
        text()

    if QuestionNumbers == NbQavantSpe and not FinJeu:
        generationCount += 1
        Question = False
        SuiteTextSpe = True
        textspecial()


# --- Vérifie si une jauge est à 0 et déclenche le game over ---
def VerifierFinDePartie():
    global Arme, Population, eco, envi, GameOver, gameOverText, gameOverCounter, gameOverDone

    texte = None
    if Arme <= 0:
        texte = FinListe[2]
    elif Population <= 0:
        texte = FinListe[0]
    elif envi <= 0:
        texte = FinListe[1]
    elif eco <= 0:
        texte = FinListe[3]

    if texte and not GameOver:
        GameOver = True
        gameOverText = texte
        gameOverCounter = 0
        gameOverDone = False


# --- Gère les arcs narratifs spéciaux (Partie 1, Partie 2) ---
def textspecial():
    global WitchDialogue, QuestionNumbers, TextSpeIndex, counter, Done, eco
    global SuiteTextSpe, Question, NombreTextSpe, QuestionSpe, FinJeu, Partie1Active, IndexFin

    if FinJeu:
        SuiteTextSpe = False
        return

    q2 = ChoixHistoire["Question2"]
    q3 = ChoixHistoire["Question3"]
    q4 = ChoixHistoire["Question4"]
    q5 = ChoixHistoire["Question5"]

    index_depart = None

    if NombreTextSpe == 0:
        index_depart = 0

    elif NombreTextSpe == 1:
        if Arme >= 120:
            Partie1Active = True
            index_depart = 7
        else:
            NombreTextSpe += 1
            return textspecial()

    elif NombreTextSpe == 2:
        if Partie1Active:
            index_depart = 17 if q2 else 38
        else:
            NombreTextSpe += 1
            return textspecial()

    elif NombreTextSpe == 3:
        if Partie1Active:
            if q2 and q3:
                index_depart = 23
            elif q2 and not q3:
                index_depart = 28
            elif not q2 and q3:
                index_depart = 50
            else:
                index_depart = 46
        else:
            NombreTextSpe += 1
            return textspecial()

    elif NombreTextSpe == 4:
        if Partie1Active:
            if q2 and q3:
                index_depart = 55 if q4 else 57
            elif q2 and not q3:
                index_depart = 33
            elif not q2 and q3:
                index_depart = 66 if q4 else 70
            else:
                NombreTextSpe += 1
                return textspecial()
        else:
            NombreTextSpe += 1
            return textspecial()

    elif NombreTextSpe == 5:
        if Partie1Active and q2 and not q3:
            index_depart = 59 if q5 else 62
        else:
            NombreTextSpe += 1
            return textspecial()

    elif NombreTextSpe == 6:
        if Partie1Active and q2 and not q3 and not q5:
            index_depart = 77 if q4 else 74
        else:
            NombreTextSpe += 1
            return textspecial()

    elif NombreTextSpe == 7:
        if generationCount >= NbGenAvantPartie2:
            index_depart = 81
            ChoixHistoire["Question2"] = False
            ChoixHistoire["Question3"] = False
        else:
            SuiteTextSpe = False
            QuestionNumbers = 0
            Question = False
            return text()

    elif NombreTextSpe == 8:
        if not q2:
            index_depart = 114
        else:
            index_depart = 93

    elif NombreTextSpe == 9:
        if q2 and not q3 and TextSpeIndex >= 110:
            NombreTextSpe += 1
            return textspecial()

        if q2 and q3:
            index_depart = 99
        elif q2 and not q3:
            index_depart = 106
        elif not q2 and q3:
            index_depart = 121
        else:
            index_depart = 129

    elif NombreTextSpe == 10:
        if q2 and not q3:
            index_depart = 110
        else:
            SuiteTextSpe = False
            NombreTextSpe += 1
            QuestionNumbers = 0
            Question = False
            return text()

    else:
        SuiteTextSpe = False
        NombreTextSpe += 1
        QuestionNumbers = 0
        Question = False
        return text()

    if index_depart is not None and TextSpeIndex < index_depart:
        TextSpeIndex = index_depart

    WitchDialogue = TextSpe[TextSpeIndex]
    TextSpeIndex += 1
    counter = 0
    Done = False

    dernieres_lignes_fins = [55, 57, 60, 48, 68, 72, 75, 79, 104, 112, 126, 135]

    if (TextSpeIndex - 1) in dernieres_lignes_fins:
        FinJeu = True
        IndexFin = TextSpeIndex - 1

    if WitchDialogue.strip().endswith("?"):
        QuestionSpe = True

    if TextSpeIndex >= len(TextSpe) or TextSpe[TextSpeIndex] == "":
        SuiteTextSpe = False
        NombreTextSpe += 1
        Question = False
        QuestionNumbers = 0

    return WitchDialogue


# --- Avance dans les dialogues normaux (intro + cycles présentation/question) ---
def text():
    global SuiteTextSpe, TextSpeIndex, WitchDialogue, Start, randomP, counter
    global Done, Question, startIndex, Pres, ancient, QuestionNumbers, TextSpe

    if not Start:
        WitchDialogue = StartDialogue[startIndex]
        counter = 0
        Done = False
        startIndex += 1
        if startIndex == len(StartDialogue):
            Start = True

    elif Start:
        if not Pres and QuestionNumbers != NbQavantSpe:
            Pres = True
            WitchDialogue = Prentation[randomP]
            ancient = randomP
            counter = 0
            Done = False

        elif Pres and QuestionNumbers != NbQavantSpe:
            Pres = False
            Question = True
            WitchDialogue = Happen[ancient]
            counter = 0
            Done = False

    return WitchDialogue


# --- Gère tous les événements clavier/souris ---
def gerer_evenements():
    global close, AvantGame, counter, Done, randomP

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            close = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            close = True

        if not AvantGame:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                AvantGame = True
                ecran.fill((0, 0, 0))
                counter = 0
            continue

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if GameOver or FinJeu:

                continue

            randomP = random.choice([i for i in range(len(Prentation)) if i != ancient])

            if QuestionSpe:
                if not Done:
                    counter = len(WitchDialogue) * speed
                    Done = True
                continue

            if SuiteTextSpe:
                if not Done:
                    counter = len(WitchDialogue) * speed
                    Done = True
                else:
                    textspecial()
                continue

            if not Done:
                counter = len(WitchDialogue) * speed
                Done = True
            elif not Question:
                text()


# --- Rendu du jeu (personnage, texte, boutons) ---
def rendu_jeu():
    global counter, Done, img_perso

    if WitchDialogue not in (StartDialogue[0], StartDialogue[1]):
        ecran.blit(background, (0, 0))

    boxe()

    if counter == 0:
        img_perso = personnages()
    if img_perso is not None:
        x_perso = (largeur - img_perso.get_width()) // 2
        y_perso = (hauteur - img_perso.get_height()) // 3.8
        ecran.blit(img_perso, (x_perso, y_perso))

    if counter < speed * len(WitchDialogue):
        counter += 1
    else:
        Done = True

    font = pygame.font.Font(chemin("Capture it.ttf"), size())
    snip = font.render(WitchDialogue[0:counter // speed], True, (255, 255, 255))
    ecran.blit(snip, (30, 820))

    if Start and Done and Question:
        clic_oui = yesButton.draw()
        clic_non = noButton.draw()
        if not SuiteTextSpe:
            choixjoueur(clic_oui, clic_non)

    if Done and QuestionSpe:
        clic_oui = yesButton.draw()
        clic_non = noButton.draw()
        choixSpe(clic_oui, clic_non)

    VerifierFinDePartie()


class Button:
    def __init__(self, x, y, w, h, image):
        self.image = pygame.transform.scale(image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.image.set_alpha(200)
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True
        else:
            self.image.set_alpha(255)

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        ecran.blit(self.image, self.rect)
        return action


yesButton = Button(largeur * 0.05, 620, 180, 180, yesImage)
noButton = Button(largeur * 0.85, 620, 180, 180, noImage)
img_perso = None

# --- Boucle principale ---
while not close:

    gerer_evenements()

    if not AvantGame:
        menu()
    elif GameOver:
        if not fadeOutDone:
            afficher_fadeout()
        else:
            afficher_game_over()
    elif FinJeu and Done:
        fin()
    else:
        rendu_jeu()

    pygame.display.flip()
    timerType.tick(60)

pygame.quit()