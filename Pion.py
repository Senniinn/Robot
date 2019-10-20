class Pion():
    def __init__(self, x, y, color, canvas):
        self.color = color
        self.x = x
        self.y = y
        self.canvas = canvas
        self.oval = self.canvas.create_oval(self.x + 5, self.y + 5, self.x + 55, self.y + 55, fill=self.color)

    def possibilities(self, pionsBlancs, pionsNoirs, pion):

        ##########  DECLARATION DES VARRIBLES  ##########   60 = une unité

        if pion.color == "white":
            possiblity1 = [pion.x + 60, pion.y - 60]  # Avancer de vers la droite
            possiblity2 = [pion.x - 60, pion.y - 60]  # Avancer de vers la gauche
            possiblity1a = [pion.x + 120, pion.y - 120]  # Manger vers la droite
            possiblity2a = [pion.x - 120, pion.y - 120]  # Manger vers la gauche

            possiblity3 = [pion.x + 60, pion.y + 60]  # Check derriere a droite
            possiblity4 = [pion.x - 60, pion.y + 60]  # Check derriere a gauche
            possiblity3a = [pion.x + 120, pion.y + 120]  # Manger derriere a droite
            possiblity4a = [pion.x - 120, pion.y + 120]  # Manger derriere a gauche
        else:
            possiblity1 = [pion.x - 60, pion.y + 60]  # Avancer de vers la gauche
            possiblity2 = [pion.x + 60, pion.y + 60]  # Avancer de vers la droite
            possiblity1a = [pion.x - 120, pion.y + 120]  # Manger vers la gauche
            possiblity2a = [pion.x + 120, pion.y + 120]  # Manger vers la droite

            possiblity3 = [pion.x + 60, pion.y - 60]  # Check derriere a droite
            possiblity4 = [pion.x - 60, pion.y - 60]  # Check derriere a gauche
            possiblity3a = [pion.x + 120, pion.y - 120]  # Manger derriere a droite
            possiblity4a = [pion.x - 120, pion.y - 120]  # Manger derriere a gauche

        validPoss1 = True
        validPoss2 = True
        validPoss1a = False
        validPoss2a = False

        validPoss3 = True
        validPoss4 = True
        validPoss3a = False
        validPoss4a = False
        possiblities = []  # Tableau qui va contenir les différentes possibilité d'un pion
        pionDown = None

        # print("pos1",possiblity1)
        # print("pos2",possiblity2)
        # print("pos3",possiblity3)
        # print("pos4",possiblity4)
        # print("pos1a",possiblity1a)
        # print("pos2a",possiblity2a)
        # print("pos3a",possiblity3a)
        # print("pos4a",possiblity4a)

        ##########  CHECK DES DEPLACEMENTS ##########
        # Checks des pions blanc       qu'on soit un pion noir ou blanc
        for pionsBlanc in pionsBlancs:
            if possiblity1[0] <= 540 and possiblity1[0] == pionsBlanc.x and possiblity1[1] == pionsBlanc.y:  # Check si un pion blanc est a droite
                validPoss1 = False
                if 0 <= possiblity1a[1] <= 540 and pion.color != pionsBlanc.color:  # Si on est un pion noir
                    validPoss1a = True  # Possibilité de manger vers la droite passe a vrai  ==> Voir plus bas
                    pionDown = self.setPionDown(pionDown, pionsBlanc)  # Le pion manger sera donc un pion blanc

            if possiblity2[0] >= 0 and possiblity2[0] == pionsBlanc.x and possiblity2[1] == pionsBlanc.y:  # Check si un pion blanc est a gauche
                validPoss2 = False
                if 0 <= possiblity2a[1] <= 540 and pion.color != pionsBlanc.color:
                    validPoss2a = True
                    pionDown = self.setPionDown(pionDown, pionsBlanc)

            if possiblity3[0] <= 540 and possiblity3[0] == pionsBlanc.x and possiblity3[1] == pionsBlanc.y:  # Check si un pion blanc est derriere a droite
                if 0 <= possiblity3a[1] <= 540 and pion.color != pionsBlanc.color:
                    validPoss3a = True
                    pionDown = self.setPionDown(pionDown, pionsBlanc)

            if possiblity4[0] >= 0 and possiblity4[0] == pionsBlanc.x and possiblity4[1] == pionsBlanc.y:  # Check si un pion blanc est derriere a gauche
                if 0 <= possiblity4a[1] <= 540 and pion.color != pionsBlanc.color:
                    validPoss4a = True
                    pionDown = self.setPionDown(pionDown, pionsBlanc)

        # Checks des pions Noirs      qu'on soit un pion noir ou blanc              Même raisonnement que plus haut
        for pionsNoir in pionsNoirs:
            if possiblity1[0] <= 540 and possiblity1[0] == pionsNoir.x and possiblity1[1] == pionsNoir.y:
                validPoss1 = False
                if 0 <= possiblity1a[1] <= 540 and pion.color != pionsNoir.color:  # Si on est un blanc
                    validPoss1a = True
                    pionDown = self.setPionDown(pionDown, pionsNoir)

            if possiblity2[0] >= 0 and possiblity2[0] == pionsNoir.x and possiblity2[1] == pionsNoir.y:
                validPoss2 = False
                if 0 <= possiblity2a[1] <= 540 and pion.color != pionsNoir.color:  # Si on est un blanc
                    validPoss2a = True
                    pionDown = self.setPionDown(pionDown, pionsNoir)

            if possiblity3[0] <= 540 and possiblity3[0] == pionsNoir.x and possiblity3[1] == pionsNoir.y:
                if 0 <= possiblity3a[1] <= 540 and pion.color != pionsNoir.color:
                    validPoss3a = True
                    pionDown = self.setPionDown(pionDown, pionsNoir)

            if possiblity4[0] >= 0 and possiblity4[0] == pionsNoir.x and possiblity4[1] == pionsNoir.y:
                if 0 <= possiblity4a[1] <= 540 and pion.color != pionsNoir.color:
                    validPoss4a = True
                    pionDown = self.setPionDown(pionDown, pionsNoir)



        ##########  CHECK SI ON PEUT MANGER UN PION ##########

        if validPoss1a:  # La possibilité est vraie, elle deviendra fausse a la fin si, on trouve un pion sur cette case
            for pionsBlanc in pionsBlancs:
                if possiblity1a[0] == pionsBlanc.x and possiblity1a[1] == pionsBlanc.y:
                    validPoss1a = False
            for pionsNoir in pionsNoirs:  # Même raisonnement pour un pion noir
                if possiblity1a[0] == pionsNoir.x and possiblity1a[1] == pionsNoir.y:
                    validPoss1a = False
        if validPoss2a:  # Même raisonnement mais pour la possibilité deux, à savoir le déplacement vers la gauche
            for pionsBlanc in pionsBlancs:
                if possiblity2a[0] == pionsBlanc.x and possiblity2a[1] == pionsBlanc.y:
                    validPoss2a = False
            for pionsNoir in pionsNoirs:
                if possiblity2a[0] >= 0 and possiblity2a[0] == pionsNoir.x and possiblity2a[1] == pionsNoir.y:
                    validPoss2a = False
        if validPoss3a:
            for pionsBlanc in pionsBlancs:
                if possiblity3a[0] == pionsBlanc.x and possiblity3a[1] == pionsBlanc.y:
                    validPoss3a = False
            for pionsNoir in pionsNoirs:
                if possiblity3a[0] == pionsNoir.x and possiblity3a[1] == pionsNoir.y:
                    validPoss3a = False
        if validPoss4a:
            for pionsBlanc in pionsBlancs:
                if possiblity4a[0] == pionsBlanc.x and possiblity4a[1] == pionsBlanc.y:
                    validPoss4a = False
            for pionsNoir in pionsNoirs:
                if possiblity4a[0] == pionsNoir.x and possiblity4a[1] == pionsNoir.y:
                    validPoss4a = False


        # Passage des possibilités au tableau.
        if validPoss1:
            possiblities.append(possiblity1)
        if validPoss2:
            possiblities.append(possiblity2)
        if validPoss1a:
            possiblities.append(possiblity1a)
        if validPoss2a:
            possiblities.append(possiblity2a)
        if validPoss3a:
            possiblities.append(possiblity3a)
        if validPoss4a:
            possiblities.append(possiblity4a)



        return [possiblities, pionDown]  # Retour des différentes possibilité et du pion manger.

    def setPionDown(self, pionDown, pion):
        if pionDown is None:
            pionDown = [pion]
        else:
            pionDown.append(pion)
        return pionDown
    def move(self, x, y):
        self.x = x
        self.y = y
        self.canvas.tag_raise(self.oval)
        self.canvas.coords(self.oval, self.x + 5, self.y + 5, self.x + 55, self.y + 55)
