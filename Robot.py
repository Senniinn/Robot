# class d'un robot de base
import random
import time


class Robot():
    def __init__(self, nom, sante=100, competence="Simple Robot nul"):
        self.nom = nom
        self.sante = sante
        self.competence = competence
        self.tauxAttaque = 10
        self.tauxCritique = 0.1
        self.experience = 0
        self.lvl = 1
        self.maxHp = 100

    def sePresenter(self):
        print("Bonjour ! Je suis " + self.nom + " et je suis un " + self.competence)

    def attaquer(self, robot):
        if self.sante > 0:
            degats = self.tauxAttaque * self.lvl
            if (self.tauxCritique > random.random()):
                degats *= 2
            robot.sante -= degats

            if (robot.sante <= 0):
                self.gagnerExperience(6)
                robot.sante = 0
            else:
                self.gagnerExperience(2)

            #print("\nL'attage de " + self.nom + " a infliger " + str(degats) + " points de dégats")
            #print("Il reste " + str(robot.sante) + " points de vie à " + robot.nom)
            #time.sleep(1)

    def gagnerExperience(self, montant):
        if self.lvl == 1:
            self.experience += montant
            if self.experience >= 10:
                self.lvl += 1
                self.experience = self.experience - 10


class Equipe():
    def __init__(self, nom, robots):
        self.nom = nom
        self.equipe = []
        for robot in robots:
            self.equipe.append(robot)

    def ajouterRobot(self, robot):
        self.equipe.append(robot)

    def randRobot(self):
        equipevivante = []

        for robot in self.equipe:
            if (robot.sante > 0):
                equipevivante.append(robot)
        if len(equipevivante) > 0:
            robot = random.choice(equipevivante)
            return robot
        else:
            return None

    def membreVivant(self):
        membreVivant = []
        for robot in self.equipe:
            if robot.sante > 0:
                membreVivant.append(robot)

        return membreVivant

    def afficherHp(self):
        print("\nSanté pour l'équipe : " + self.nom)
        for robot in self.equipe:
            if (robot.sante == 0):
                print("Le robot " + robot.nom + " est mort.")
            else:
                print("Le robot " + robot.nom + " (lvl " + str(robot.lvl) + ") a : " + str(robot.sante) + " HP.")


class Partie():
    def __init__(self, test = False):
        if test:
            self.equipe1 = Equipe("FullSoldat", [RobotSoldat("un"), RobotSoldat("un"), RobotHybride("un"), RobotMedecin("un")])
            self.equipe2 = Equipe("healer", [RobotSoldat("deux"), RobotSoldat("deux"), RobotSoldat("deux"), RobotHybride("deux")])
        else:
            print("Duel entre le joueur 1 et le joueur 2: Combats de 4 robots dans chaque équpie !")
            nomEquipe1 = input("Joueur 1: choisir le nom de ton équipe :")
            self.equipe1 = self.creerEquipe(nomEquipe1)
            nomEquipe2 = input("Joueur 2: choisir le nom de ton équipe :")
            self.equipe2 = self.creerEquipe(nomEquipe2)

    def creerEquipe(self, nom):
        equipe = []
        for i in range(4):
            nomRobot = input("Créer un robot, renseigne lui son nom :")
            print("Joueur 1, Renseigne le type de robot que tu veux :")
            typeRobot = input("1 = Robot soldat | 2 = Robot médecin | 3 = Robot hybride")
            if (typeRobot == "1"):
                equipe.append(RobotSoldat(nomRobot))
            elif (typeRobot == "2"):
                equipe.append(RobotMedecin(nomRobot))

        return Equipe(nom, equipe)

    def creerEquipe2(self, nom):
        if nom == "Bleu":
            return Equipe(nom, [RobotSoldat("Rambo"), RobotSoldat("Huutai"), RobotMedecin("Docteur House")])
        else:
            return Equipe(nom, [RobotSoldat("Stravinsky"), RobotSoldat("Ramuz"), RobotMedecin("Olivier Mauvais")])

    def jouerTour(self):
        commencer = random.randint(0, 1)
        while len(self.equipe1.membreVivant()) > 0 and len(self.equipe2.membreVivant()) > 0:
            for robotIndex in range(len(self.equipe1.equipe)):
                if commencer == 0:
                    self.tour(self.equipe1.equipe, self.equipe2, robotIndex)
                    if len(self.equipe1.membreVivant()) > 0 and len(self.equipe2.membreVivant()) > 0:
                        self.tour(self.equipe2.equipe, self.equipe1, robotIndex)
                    else:
                        break
                else:
                    self.tour(self.equipe2.equipe, self.equipe1, robotIndex)
                    if len(self.equipe1.membreVivant()) > 0 and len(self.equipe2.membreVivant()) > 0:
                        self.tour(self.equipe1.equipe, self.equipe2, robotIndex)
                    else:
                        break

        return self.afficherVictoire()

    def tour(self, equipeAllie, equipeEnemie, index):
        if(equipeAllie[index].__class__.__name__ == "RobotHybride"):
            equipeAllie[index].action(equipeAllie, equipeEnemie)
        elif equipeAllie[index].__class__.__name__ == "RobotSoldat":
            equipeAllie[index].attaquer(equipeEnemie.randRobot())
        else:
            equipeAllie[index].soigner(equipeAllie)

    def afficherVictoire(self):
        if len(self.equipe1.membreVivant()) > 0:
            #print("\nL'equipe " + self.equipe1.nom + " a gagné\n")
            #self.equipe1.afficherHp()
            #self.equipe2.afficherHp()
            return 1
        else:
            #print("\nL'equipe " + self.equipe2.nom + " a gagné\n")
            #self.equipe1.afficherHp()
            #self.equipe2.afficherHp()
            return 2


class RobotMedecin(Robot):
    def __init__(self, nom, sante=90, competence="soigner"):
        Robot.__init__(self, nom, sante, competence)
        self.tauxSoin = 45
        self.maxHp = 90

    def soigner(self, monEquipe):
        if (self.sante == 0):
            pass
            #print(self.nom + " est mort")
        else:
            robotMinHp = None
            minHp = 100
            for robot in monEquipe:
                if (robot.sante > 0 and robot.sante < robot.maxHp and robot.sante <= minHp):
                    minHp = robot.sante
                    robotMinHp = robot

            if robotMinHp != None:
                if (self.tauxCritique > random.random()):
                    robotMinHp.sante += self.tauxSoin * 2 * self.lvl
                else:
                    robotMinHp.sante += self.tauxSoin * self.lvl

                if (robotMinHp.sante > robotMinHp.maxHp):
                    robotMinHp.sante = robotMinHp.maxHp
                if (self.sante < self.maxHp):
                    self.sante -= 10

                self.gagnerExperience(5)

                #print("\n" + robotMinHp.nom + " a regagné " + str(robotMinHp.sante - minHp) + " points de vie")
                #time.sleep(1)


class RobotSoldat(Robot):
    def __init__(self, nom, sante=100, competence="attaquer"):
        Robot.__init__(self, nom, sante, competence)
        self.tauxAttaque = 25


class RobotHybride(RobotMedecin):
    def __init__(self, nom, sante=100, competence="hybride"):
        RobotMedecin.__init__(self, nom, sante, competence)
        self.maxHp = 100
        self.tauxAttaque = 25
        self.tauxSoin = 20

    def action(self, equipeAllie, equipeEnemie):
        rand = random.randint(0, 1)
        if rand == 0:
            self.attaquer(equipeEnemie.randRobot())
        else:
            self.soigner(equipeAllie)

stat = 0
total = 0
for i in range(15000):
    p = Partie(True)
    result = p.jouerTour()
    if result == 1:
        stat += 1
    total += 1

print("L'equipe bleu a gagné : " + str(stat / total * 100) + " % des parties")
rand = random.randint(0, 1)
