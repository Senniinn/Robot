from tkinter import *
from tkinter.messagebox import *


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
        self.joueurBlanc = []
        self.joueurNoir = []
        for i in range(10):
            for j in range(10):
                self.canvas.create_rectangle(x, y, x + 60, y + 60, fill=color)
                if color == "brown":
                    if len(self.joueurNoir) < self.nbPion:
                        oval = self.canvas.create_oval(x + 5, y + 5, x + 55, y + 55, fill="black")
                        self.joueurNoir.append([oval, x, y])
                    elif i == 4 or i == 5:
                        pass
                    elif len(self.joueurBlanc) < self.nbPion:
                        oval = self.canvas.create_oval(x + 5, y + 5, x + 55, y + 55, fill="white")
                        self.joueurBlanc.append([oval, x, y])

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

    def move(self, x, y):
        newx = x * 60
        newy = y * 60
        if self.flag == 0:
            self.canvas.tag_raise(self.joueurBlanc[0][0])
            self.canvas.itemconfigure(self.joueurBlanc[0][0], fill="green")
            self.canvas.coords(self.joueurBlanc[0][0], newx + 5, newy + 5, newx + 55, newy + 55)
            print(self.joueurBlanc[0])
            self.joueurBlanc[0] = [self.joueurBlanc[0], newx, newy]
        else:
            self.canvas.tag_raise(self.joueurNoir[0][0])
            self.canvas.itemconfigure(self.joueurNoir[0][0], fill="pink")
            self.canvas.coords(self.joueurNoir[0][0], newx + 5, newy + 5, newx + 55, newy + 55)
            self.joueurNoir[0] = [self.joueurNoir[0], newx, newy]
        self.changeTurn()
        print(self.joueurBlanc[0])

    def pointeur(self, event):
        self.move(int(event.x / 60), int(event.y / 60))

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
creer = Button(fen1, text='Créer damier', command=d.move)
creer.pack()

bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)

can1.bind("<Button-1>", d.pointeur)
fen1.mainloop()  # démarrage du réceptionnaire d'événement
fen1.destroy()  # destruction (fermeture) de la fenêtre
