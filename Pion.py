class Pion():
    def __init__(self,x, y, color, canvas):
        self.color = color
        self.x = x
        self.y = y
        self.canvas = canvas
        self.oval = self.canvas.create_oval(self.x + 5, self.y + 5, self.x + 55, self.y + 55, fill=self.color)

    def possibilities(self, pionsBlancs, pionsNoirs, pion):
        currentColor = self.canvas.itemcget(self.oval, 'fill')
        if currentColor == "white":
            possiblity1 = [pion.x + 60, pion.y - 60]
            possiblity1a = [pion.x + 120, pion.y - 120]
            possiblity2 = [pion.x - 60, pion.y - 60]
            possiblity2a = [pion.x - 120, pion.y - 120]
        else:
            possiblity1 = [pion.x - 60, pion.y + 60]
            possiblity1a = [pion.x - 120, pion.y + 120]
            possiblity2 = [pion.x + 60, pion.y + 60]
            possiblity2a = [pion.x + 120, pion.y + 120]
        validPoss1 = True
        validPoss2 = True
        validPoss1a = False
        validPoss2a = False
        possiblities = []

        for pionsBlanc in pionsBlancs:
            if (possiblity1[0] >= 0):
                if (possiblity1[0] == pionsBlanc.x and possiblity1[1] == pionsBlanc.y):
                    validPoss1 = False
                    if (possiblity1a[0] >= 0 and possiblity1a[0] != pionsBlanc.x and possiblity1a[1] != pionsBlanc.y):
                        validPoss1a = True
            if (possiblity2[0] <= 540):
                if (possiblity2[0] == pionsBlanc.x and possiblity2[1] == pionsBlanc.y):
                    validPoss2 = False
                    if (possiblity2a[0] <= 540 and possiblity2a[0] != pionsBlanc.x and possiblity2a[1] != pionsBlanc.y):
                        validPoss2a = True
        for pionsNoir in pionsNoirs:
            if (possiblity1[0] >= 0):
                if (possiblity1[0] == pionsNoir.x and possiblity1[1] == pionsNoir.y):
                    validPoss1 = False
                    if (possiblity1a[0] >= 0 and possiblity1a[0] != pionsNoir.x and possiblity1a[1] != pionsNoir.y):
                        validPoss1a = True
            if (possiblity2[0] <= 540):
                if (possiblity2[0] == pionsNoir.x and possiblity2[1] == pionsNoir.y):
                    validPoss2 = False
                    if (possiblity2[0] <= 540 and possiblity2a[0] != pionsNoir.x and possiblity2a[1] != pionsNoir.y):
                        validPoss2a = True

        if validPoss1:
            possiblities.append(possiblity1)
        if validPoss2:
            possiblities.append(possiblity2)
        if validPoss1a:
            possiblities.append(possiblity1a)
        if validPoss2a:
            possiblities.append(possiblity2a)

        return possiblities

    def move(self, x, y):
        self.x = x
        self.y = y
        self.canvas.tag_raise(self.oval)
        self.canvas.coords(self.oval, self.x + 5, self.y + 5, self.x + 55, self.y + 55)

