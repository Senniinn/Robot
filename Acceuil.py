import webbrowser
from tkinter import *

from Dame import Dame


def lauchGame():
    fen1 = Tk()
    root.destroy()
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
    d = Dame(can1)
    d.setCurrentPlayerLabel(player)
    d.setPionLabels(pionBlanc, pionNoir)
    d.creerDamier()
    effacer = Button(fen1, text='Effacer', command=d.creerDamier)
    effacer.pack()
    bou1 = Button(fen1, text='Quitter', command=fen1.quit)
    bou1.pack(side=BOTTOM)
    can1.bind("<Button-1>", d.pointeur)
    fen1.mainloop()
    fen1.destroy()


def rules():
    webbrowser.open("http://www.ffjd.fr/Web/index.php?page=reglesdujeu")


root = Tk()
boutcre = Button(root, text='Jouer', command=lauchGame, anchor="center", bg='green', padx=20, pady=20)
boutcre.pack(side=TOP, anchor=W, fill=X, expand=YES)
boutrules = Button(root, text='Régles', command=rules, anchor="center", bg='blue', padx=20, pady=20)
boutrules.pack(side=TOP, anchor=W, fill=X, expand=YES)
bouquit = Button(root, text='Quitter', anchor="center", bg='red', padx=20, pady=20, command=root.quit)
bouquit.pack(side=TOP, anchor=W, fill=X, expand=YES)
root.geometry("500x200+150+0")
root.mainloop()  # démarrage du réceptionnaire d'événement
root.destroy()
