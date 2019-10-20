from tkinter import *
from tkinter.messagebox import *

from Pion import Pion


class Dame:
    def __init__(self, canevas):
        self.canvas = canevas
        self.joueurBlanc = []  # Tableau contenant les pions plans
        self.joueurNoir = []  # Tableau contenant les pions plans
        self.nbPion = 20  # nombre de pions par joueur
        self.flag = 0  # flag = 0 si c'est le tour du joueur 1, flag = 1 si c'est celui du joueur 2
        self.possibilities = []
        self.selected = None
        self.eatPion = None
        self.winner = None
        self.currentPlayerLabel = None
        self.pionNoirLabel = None
        self.pionBlancLabel = None

    # Methode de création du damier
    def creerDamier(self):
        color = "white"
        x = 0
        y = 0
        self.flag = 0
        self.joueurBlanc = []
        self.joueurNoir = []
        self.selected = None
        self.deletePossibilities()
        self.winner = None
        self.eatPion = None
        for i in range(10):
            for j in range(10):
                self.canvas.create_rectangle(x, y, x + 60, y + 60, fill=color)
                if color == "brown":
                    if len(self.joueurNoir) < self.nbPion:
                        pion = Pion(x, y, "black", self.canvas)
                        self.joueurNoir.append(pion)
                    elif i == 4 or i == 5:
                        pass
                    elif len(self.joueurBlanc) < self.nbPion:
                        pion = Pion(x, y, "white", self.canvas)
                        self.joueurBlanc.append(pion)

                color = self.changeCaseColor(color)
                x += 60
            color = self.changeCaseColor(color)
            x = 0
            y += 60
            self.currentPlayer(self.currentPlayerLabel)
            self.setPions()

    # Methode permettant d'alterner les cases marron et blanche
    def changeCaseColor(self, color):
        if color == "white":
            return "brown"
        else:
            return "white"

    # Défini le label d'affichage du tour du joueur
    def setCurrentPlayerLabel(self, label):
        self.currentPlayerLabel = label

    # Affiche le joueur qui joue
    def currentPlayer(self, label):
        if self.flag == 0:
            label.config(text="Joueur 1")
        else:
            label.config(text="Joueur 2")

    # Vide la fenetre
    def clear(self):
        self.canvas.delete("all")

    # Réagis au clique sur le bouton gauche de la souris
    def pointeur(self, event):
        if self.winner is None:  # Si aucun joueur n'a gagné
            x = int(event.x / 60) * 60
            y = int(event.y / 60) * 60
            endTurn = False
            replay = False
            for p in self.possibilities:  # S'il y a déjà des possibilités
                if p[0] == x and p[1] == y:  # Si la possibilité correspond à la case séléctionné
                    self.deletePossibilities()
                    if (self.selected.y - 120 == y) or (self.selected.y + 120 == y):
                        for pion in self.eatPion:  # Défini le pion qui doit être mangé
                            if pion.y - 60 == y and pion.x - 60 == x:
                                self.eatPion = pion
                            if pion.y - 60 == y and pion.x + 60 == x:
                                self.eatPion = pion
                            if pion.y + 60 == y and pion.x + 60 == x:
                                self.eatPion = pion
                            if pion.y + 60 == y and pion.x - 60 == x:
                                self.eatPion = pion
                        self.selected.move(x, y)
                        if isinstance(self.eatPion, Pion):
                            self.eat(self.eatPion)
                            result = (self.selected.possibilities(self.joueurBlanc, self.joueurNoir, self.selected))
                            if result[0] and result[1]:  # Vérifie la possibilité de rejouer
                                for p2 in result[0]:
                                    print(p2, self.selected.y)
                                    if self.selected.y - p2[1] == 120 or self.selected.y - p2[
                                        1] == -120:  # Si il y a une possibilité de remanger
                                        replay = True
                                        self.possibilities = result[0]
                                        self.eatPion = result[1]
                    if not replay:
                        self.selected.move(x, y)
                        self.selected = None
                        self.eatPion = None
                        self.changeTurn()
                        endTurn = True
            self.deletePossibilities()
            if not endTurn:  # Vérifie les possibilités autour de la case selectionnée
                stop = False
                if self.flag == 0:
                    stop = self.getPossibilities(self.joueurBlanc, x, y)
                if self.flag == 1:
                    stop = self.getPossibilities(self.joueurNoir, x, y)
                for p in self.possibilities:  # Affiche les possibilités
                    self.canvas.create_rectangle(p[0], p[1], p[0] + 60, p[1] + 60, fill="gold")
                if not stop:
                    showinfo("Alerte", 'Ce n\'est pas votre pion ou il n\'y a pas de pion sur la case')
            # print(len(self.joueurNoir), len(self.joueurBlanc))
        else:
            showinfo('Victoire', 'Le joueur {0} a déjà gagné'.format(self.winner))

    # Methode qui récupère les possiblités
    def getPossibilities(self, pions, x, y):
        for i in range(len(pions)):
            if pions[i].x == x and pions[i].y == y:
                self.selected = pions[i]
                result = self.selected.possibilities(self.joueurBlanc, self.joueurNoir, self.selected)
                self.possibilities = result[0]
                self.eatPion = result[1]
                return True
        return False

    # Change le tour
    def changeTurn(self):
        if self.flag == 0:
            self.flag = 1
        else:
            self.flag = 0
        self.currentPlayer(self.currentPlayerLabel)

    # Manger le pion passé en paramètre
    def eat(self, pion):
        if pion.color == 'black':
            index = self.joueurNoir.index(pion)
            self.joueurNoir.pop(index)
            self.canvas.delete(pion.oval)
        if pion.color == 'white':
            index = self.joueurBlanc.index(pion)
            self.joueurBlanc.pop(index)
            self.canvas.delete(pion.oval)
        self.victory(pion)

    # Vérifie si personne n'a gagné
    def victory(self, pion):
        if pion.color == 'black':
            if len(self.joueurNoir) == 0:
                self.winner = "noir"
                showinfo('Victoire', 'Le joueur blanc a gagné')
        if pion.color == 'white':
            if len(self.joueurNoir) == 0:
                self.winner = "blanc"
                showinfo('Victoire', 'Le joueur noir a gagné')
        self.setPions()

    # Supprimer les possibilitées
    def deletePossibilities(self):
        for p in self.possibilities:
            self.canvas.create_rectangle(p[0], p[1], p[0] + 60, p[1] + 60, fill="brown")
        self.possibilities = []

    # Selectionne les labels du nombre de pions restants
    def setPionLabels(self, pionBlanc, pionNoir):
        self.pionBlancLabel = pionBlanc
        self.pionNoirLabel = pionNoir

    # Affiche le noombre de pions restant
    def setPions(self):
        self.pionBlancLabel.config(text="Joueur 1 : {0}".format(len(self.joueurBlanc)))
        self.pionNoirLabel.config(text="Joueur 2 : {0}".format(len(self.joueurNoir)))


# ------ Programme principal ------

# Création du widget principal ("maître") :
fen1 = Tk()

# Création des widgets "esclaves" :
can1 = Canvas(fen1, bg='dark grey', height=600, width=600)
can1.pack(side=LEFT)

player = Label(fen1)
player.pack()
pionRestant = Label(fen1, text="Pions restants")
pionRestant.pack()
pionBlanc = Label(fen1)
pionBlanc.pack()
pionNoir = Label(fen1)
pionNoir.pack()

# Creation du damier
d = Dame(can1)
d.setCurrentPlayerLabel(player)
d.setPionLabels(pionBlanc, pionNoir)
d.creerDamier()

effacer = Button(fen1, text='Effacer', command=d.clear)
effacer.pack()
creer = Button(fen1, text='Créer damier', command=d.creerDamier)
creer.pack()
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)

can1.bind("<Button-1>", d.pointeur)
fen1.mainloop()  # démarrage du réceptionnaire d'événement
fen1.destroy()  # destruction (fermeture) de la fenêtre
