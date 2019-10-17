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
        stop = False
        for i in range(self.nbPion):
            if self.flag == 0 and self.joueurBlanc[i].x == x and self.joueurBlanc[i].y == y:
                self.joueurBlanc[i].possibilites(self.joueurBlanc, self.joueurNoir, self.joueurBlanc[i])
                stop = True
                break
            elif self.flag == 1 and self.joueurNoir[i].x == x and self.joueurNoir[i].y == y:
                self.joueurBlanc[i].possibilites(self.joueurBlanc, self.joueurNoir, self.joueurNoir[i])
                stop = True
                break
        if not stop:
            showinfo("Alrte", 'Ce n\'est pas votre pion ou il n\'y a pas de pion sur la case')

    def changeTurn(self):
        if self.flag == 0:
            self.flag = 1
        else:
            self.flag = 0


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
