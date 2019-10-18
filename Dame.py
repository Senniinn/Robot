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

    # def move(self, pion):
    #     newx = pion.x
    #     newy = pion.y
    #     if self.flag == 0:
    #         self.canvas.tag_raise(pion.oval)
    #         self.canvas.itemconfigure(pion.oval, fill="green")
    #         self.canvas.coords(pion.oval, newx + 5, newy + 5, newx + 55, newy + 55)
    #         pion.x = newx
    #         pion.y = newy
    #         print(pion.oval, newx, pion.x, newy, pion.y)
    #     else:
    #         self.canvas.tag_raise(pion.oval)
    #         self.canvas.itemconfigure(pion.oval, fill="pink")
    #         self.canvas.coords(pion.oval, newx + 5, newy + 5, newx + 55, newy + 55)
    #         pion.x = newx
    #         pion.y = newy
    #     self.changeTurn()

    def pointeur(self, event):
        x = int(event.x / 60) * 60
        y = int(event.y / 60) * 60
        endTurn = False
        for p in self.possibilities:
            if p[0] == x and p[1] == y:
                self.deletePossibilities()
                if (self.selected.y - 120 == y and self.selected.color == "white") or (
                        self.selected.y + 120 == y and self.selected.color == "black"):
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
                for i in range(len(self.joueurBlanc)):
                    if self.joueurBlanc[i].x == x and self.joueurBlanc[i].y == y:
                        result = self.getPossibilities(self.joueurBlanc[i])
                        if result[1] is not None:
                            print(result[1].color, result[1].x, result[1].y)
                        self.possibilities = result[0]
                        self.eatPion = result[1]
                        stop = True
            if self.flag == 1:
                for i in range(len(self.joueurNoir)):
                    if self.joueurNoir[i].x == x and self.joueurNoir[i].y == y:
                        result = self.getPossibilities(self.joueurNoir[i])
                        self.possibilities = result[0]
                        if result[1] is not None:
                            print(result[1].color, result[1].x, result[1].y)
                        self.eatPion = result[1]
                        stop = True
            for p in self.possibilities:
                self.canvas.create_rectangle(p[0], p[1], p[0] + 60, p[1] + 60, fill="gold")
            if not stop:
                showinfo("Alerte", 'Ce n\'est pas votre pion ou il n\'y a pas de pion sur la case')
        # print(len(self.joueurNoir), len(self.joueurBlanc))

    def getPossibilities(self, pion):
        self.selected = pion
        return pion.possibilities(self.joueurBlanc, self.joueurNoir, pion)

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
