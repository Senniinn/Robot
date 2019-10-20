from tkinter import *
from tkinter.messagebox import *

from Pion import Pion


class Dame:
    def __init__(self, canevas):
        self.canvas = canevas
        self.joueurBlanc = []
        self.joueurNoir = []
        self.nbPion = 20
        self.flag = 0
        self.possibilities = []
        self.selected = None
        self.eatPion = None
        self.winner = None

    def creerDamier(self):
        color = "white"
        x = 0
        y = 0
        self.flag = 0
        self.joueurBlanc = []
        self.joueurNoir = []
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

    def changeCaseColor(self, color):
        if color == "white":
            return "brown"
        else:
            return "white"

    def clear(self):
        self.canvas.delete("all")

    def pointeur(self, event):
        if self.winner is None:
            x = int(event.x / 60) * 60
            y = int(event.y / 60) * 60
            endTurn = False

            for p in self.possibilities:
                if p[0] == x and p[1] == y:
                    self.deletePossibilities()
                    if (self.selected.y - 120 == y) or (self.selected.y + 120 == y):
                        if isinstance(self.eatPion, Pion):
                            self.eat(self.eatPion)
                    self.selected.move(x, y)
                    self.selected = None
                    self.eatPion = None
                    self.changeTurn()
                    endTurn = True

            self.deletePossibilities()
            if not endTurn:
                stop = False
                if self.flag == 0:
                    stop = self.getPossibilities(self.joueurBlanc, x, y)
                if self.flag == 1:
                    stop = self.getPossibilities(self.joueurNoir, x, y)
                for p in self.possibilities:
                    self.canvas.create_rectangle(p[0], p[1], p[0] + 60, p[1] + 60, fill="gold")
                if not stop:
                    showinfo("Alerte", 'Ce n\'est pas votre pion ou il n\'y a pas de pion sur la case')
            # print(len(self.joueurNoir), len(self.joueurBlanc))
        else:
            showinfo('Victoire', 'Le joueur {0} a déjà gagné'.format(self.winner))

    def getPossibilities(self, pions, x, y):
        for i in range(len(pions)):
            if pions[i].x == x and pions[i].y == y:
                self.selected = pions[i]
                result = self.selected.possibilities(self.joueurBlanc, self.joueurNoir, self.selected)
                self.possibilities = result[0]
                self.eatPion = result[1]
                return True
        return False

    def changeTurn(self):
        if self.flag == 0:
            self.flag = 1
        else:
            self.flag = 0

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

    def victory(self, pion):
        if pion.color == 'black':
            if len(self.joueurNoir) == 0:
                self.winner = "noir"
                showinfo('Victoire', 'Le joueur blanc a gagné')
        if pion.color == 'white':
            if len(self.joueurNoir) == 0:
                self.winner = "blanc"
                showinfo('Victoire', 'Le joueur noir a gagné')

    def deletePossibilities(self):
        for p in self.possibilities:
            self.canvas.create_rectangle(p[0], p[1], p[0] + 60, p[1] + 60, fill="brown")
        self.possibilities = []


# ------ Programme principal ------

# Création du widget principal ("maître") :
fen1 = Tk()

# Création des widgets "esclaves" :
can1 = Canvas(fen1, bg='dark grey', height=600, width=600)
can1.pack(side=LEFT)

# Creation du damier
d = Dame(can1)
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
