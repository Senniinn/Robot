class Pion():
    def __init__(self,x, y, color, canvas):
        self.color = color
        self.x = x
        self.y = y
        self.canvas = canvas
        self.oval = self.canvas.create_oval(self.x + 5, self.y + 5, self.x + 55, self.y + 55, fill=self.color)

    def possibilities(self, pionsBlancs, pionsNoirs, pion):

##########  DECLARATION DES VARRIBLES  ##########

        if pion.color == "white":
            possiblity1 = [pion.x + 60, pion.y - 60] #Avancer de vers la droite
            possiblity1a = [pion.x + 120, pion.y - 120] #Manger vers la droire
            possiblity2 = [pion.x - 60, pion.y - 60] #Avancer de vers la gauche
            possiblity2a = [pion.x - 120, pion.y - 120] #Manger vers la gauche
        else:
            possiblity1 = [pion.x - 60, pion.y + 60] #Avancer de vers la gauche
            possiblity1a = [pion.x - 120, pion.y + 120] #Manger vers la gauche
            possiblity2 = [pion.x + 60, pion.y + 60] #Avancer de vers la droite
            possiblity2a = [pion.x + 120, pion.y + 120] #Manger vers la droite

        validPoss1 = True
        validPoss2 = True
        validPoss1a = False
        validPoss2a = False
        possiblities = [] # Tableau qui va contenir les différentes possibilité d'un pion
        pionDown = None


##########  CHECK DES DEPLACEMENTS ##########

       # Checks des pions blanc       qu'on soit un pion noir ou blanc
        for pionsBlanc in pionsBlancs:
            if possiblity1[0] >= 0 and possiblity1[0] == pionsBlanc.x and possiblity1[1] == pionsBlanc.y: #Check si un pion blanc est a droite
                validPoss1 = False
                if pion.color != pionsBlanc.color: #Si on est un pion noir
                    validPoss1a = True             #Possibilité de manger vers la droite passe a vrai  ==> Voir plus bas
                    pionDown = pionsBlanc          #Le pion manger sera donc un pion blanc

            if possiblity2[0] <= 540 and possiblity2[0] == pionsBlanc.x and possiblity2[1] == pionsBlanc.y: #Check si un pion blanc est a gauche
                validPoss2 = False
                if pion.color != pionsBlanc.color:
                    validPoss2a = True
                    pionDown = pionsBlanc


        # Checks des pions Noirs      qu'on soit un pion noir ou blanc              Même raisonnement que plus haut
        for pionsNoir in pionsNoirs:
            if possiblity1[0] >= 0 and possiblity1[0] == pionsNoir.x and possiblity1[1] == pionsNoir.y:
                validPoss1 = False
                if pion.color != pionsNoir.color: # Si on est un blanc
                    validPoss1a = True
                    pionDown = pionsNoir

            if possiblity2[0] <= 540 and possiblity2[0] == pionsNoir.x and possiblity2[1] == pionsNoir.y:
                validPoss2 = False
                if pion.color != pionsNoir.color: # Si on est un blanc
                    validPoss2a = True
                    pionDown = pionsNoir

##########  CHECK SI ON PEUT MANGER UN PION ##########

        if validPoss1a:  #La possibilité est vraie, elle deviendra fausse a la fin si, on trouve un pion sur cette case
            for pionsBlanc in pionsBlancs:
                if possiblity1a[0] >= 0 and possiblity1a[0] == pionsBlanc.x and possiblity1a[1] == pionsBlanc.y:
                    validPoss1a = False
                    pionDown = None
            for pionsNoir in pionsNoirs: #Même raisonnement pour un pion noir
                if possiblity1a[0] >= 0 and possiblity1a[0] == pionsNoir.x and possiblity1a[1] == pionsNoir.y:
                    validPoss1a = False
                    pionDown = None
        if validPoss2a: #Même raisonnement mais pour la possibilité deux, à savoir le déplacement vers la gauche
            for pionsBlanc in pionsBlancs:
                if possiblity2a[0] <= 540 and possiblity2a[0] == pionsBlanc.x and possiblity2a[1] == pionsBlanc.y:
                    validPoss2a = False
                    pionDown = None
            for pionsNoir in pionsNoirs:
                if possiblity2[0] <= 540 and possiblity2a[0] == pionsNoir.x and possiblity2a[1] == pionsNoir.y:
                    validPoss2a = False
                    pionDown = None


# Passage des possibilités au tableau.
        if validPoss1:
            possiblities.append(possiblity1)
        if validPoss2:
            possiblities.append(possiblity2)
        if validPoss1a:
            possiblities.append(possiblity1a)
        if validPoss2a:
            possiblities.append(possiblity2a)

        return [possiblities, pionDown] #Retour des différentes possibilité et du pion manger.

    def move(self, x, y):
        self.x = x
        self.y = y
        self.canvas.tag_raise(self.oval)
        self.canvas.coords(self.oval, self.x + 5, self.y + 5, self.x + 55, self.y + 55)

