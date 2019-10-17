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
        validPoss1 = True
        validPoss2 = True
        possiblities = []

        for pionsBlanc in pionsBlancs:
            if (possiblity1[0] >= 0):
                if (possiblity1[0] == pionsBlanc.x and possiblity1[1] == pionsBlanc.y):
                    validPoss1 = False
            if (possiblity2[0] <= 540):
                if (possiblity2[0] == pionsBlanc.x and possiblity2[1] == pionsBlanc.y):
                    validPoss2 = False
        for pionsNoir in pionsNoirs:
            if (possiblity1[0] >= 0):
                if (possiblity1[0] == pionsNoir.x and possiblity1[1] == pionsNoir.y):
                    validPoss1 = False
            if (possiblity2[0] <= 540):
                if (possiblity2[0] == pionsNoir.x and possiblity2[1] == pionsNoir.y):
                    validPoss2 = False

        if validPoss1:
            possiblities.append(possiblity1)
        if validPoss2:
            possiblities.append(possiblity2)

        return possiblities

    def move(self, x, y):
        self.x = x
        self.y = y
        self.can.coords(self.oval, self.x + 5, self.y + 5, self.x + 55, self.y + 55)




