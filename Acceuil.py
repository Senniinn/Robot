from tkinter import *

from Dame import Dame


def lauchGame():
    fen1=Tk()
    can1 = Canvas(fen1, bg='dark grey', height=600, width=600)
    can1.pack(side=LEFT)
    d = Dame(can1)
    d.creerDamier()
    root.quit()
    fen1.mainloop()
    fen1.destroy()


root = Tk()
creer = Button(root, text='Jouer', anchor="center",bg='green',padx=20,pady=20 ,command=lauchGame())
creer.pack()
bou1 = Button(root, text='Quitter',anchor="center",bg='red',padx=20,pady=20, command=root.quit)
bou1.pack()
root.geometry("800x600+300+0")



root.mainloop()  # démarrage du réceptionnaire d'événement
root.destroy()
