class Pion():
    def __init__(self,x, y, color, canvas):
        self.color = color
        self.x = x
        self.y = y
        self.canvas = canvas
        self.oval = self.canvas.create_oval(self.x + 5, self.y + 5, self.x + 55, self.y + 55, fill=self.color)



    def move(self, x, y):
        self.x = x
        self.y = y
        self.can.coords(self.oval, self.x + 5, self.y + 5, self.x + 55, self.y + 55)




