class Pion():
    def __init__(self,x, y, color, canvas):
        self.color = color
        self.x = x
        self.y = y
        self.canvas = canvas
        self.oval = self.canvas.create_oval(self.x + 5, self.y + 5, self.x + 55, self.y + 55, fill=self.color)

    def possibilities(self, pionsBlancs, pionsNoirs, pion):
        possiblity1 = [pion.x+60, pion.y-60]
        possiblity2 = [pion.x-60, pion.y-60]
        xmin = pion.x-60
        xmax = pion.x+60
        ymin = pion.y-60
        ymax = pion.y+60
        possiblities = []

        for pionsBlanc in pionsBlancs:
            if (pionsBlanc.x >= xmin and pionsBlanc.x <= xmax and pionsBlanc.y >= ymin and pionsBlanc.y <= ymax):
                if (possiblity1[0] >= 0):
                    if (possiblity1[0] != pionsBlanc.x and  possiblity1[1] != pionsBlanc.y):
                        if possiblity1 not in possiblities:
                            possiblities.append(possiblity1)
                if (possiblity2[0] <= 540):
                    if (possiblity2[0] != pionsBlanc.x and  possiblity2[1] != pionsBlanc.y):
                        if possiblity2 not in possiblities:
                            possiblities.append(possiblity2)
        for pionsNoir in pionsNoirs:
            if (pionsNoir.x >= xmin and pionsNoir.x <= xmax and pionsNoir.y >= ymin and pionsNoir.y <= ymax):
                if (possiblity1[0] >= 0):
                    if (possiblity1[0] != pionsNoir.x and  possiblity1[1] != pionsNoir.y):
                        if possiblity1 not in possiblities:
                            possiblities.append(possiblity1)
                if (possiblity2[0] <= 540):
                    if (possiblity2[0] != pionsNoir.x and  possiblity2[1] != pionsNoir.y):
                        if possiblity2 not in possiblities:
                            possiblities.append(possiblity2)

        return possiblities

    def move(self, x, y):
        self.x = x
        self.y = y
        self.can.coords(self.oval, self.x + 5, self.y + 5, self.x + 55, self.y + 55)




