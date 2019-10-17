# class d'un robot de base
import random
import time


# Class Robot : Chaque robot aura un nom, de la santé, une compétence qui est sa description, un niveau d'attaque
# Chaque robot aura une chance de faire un coup critique
# Système d'expérience a chaque coup et quand un robot tue un autre
class Robot():
    def __init__(self, nom, sante=100, competence="Simple Robot"):
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

    # Un robot attaque un robot adverse aléatoirement, suivant son niveau ou si il fait un coup critique les dégats infliger changent | Il gagne de l'expérience.
    def attaquer(self, robot):
        degats = self.tauxAttaque * self.lvl
        if (self.tauxCritique > random.random()):
            degats *= 2
        robot.sante -= degats

        if (robot.sante <= 0):
            self.gagnerExperience(6)
            robot.sante = 0
        else:
            self.gagnerExperience(2)

        print("\nL'attage de " + self.nom + "(niveau :" + str(self.lvl) + ") a infliger " + str(
            degats) + " points de dégats")
        print("Il reste " + str(robot.sante) + " points de vie à " + robot.nom)
        time.sleep(0.5)

    # Un robot gagne de l'expérience jusqu'à 10, il monte ensuite de niveau, la monté de niveau augmentera ses dégats.
    def gagnerExperience(self, montant):
        if self.lvl == 1:
            self.experience += montant
            if self.experience >= 10:
                self.lvl += 1
                self.experience = self.experience - 10


# Robot médecin, il soigne ses alliés la majeur partie du temps. Il attaque quand toute son équipe est full hp et quand le reste de son equipe est mort.
class RobotMedecin(Robot):
    def __init__(self, nom, sante=90, competence="medecin"):
        Robot.__init__(self, nom, sante, competence)
        self.tauxSoin = 45
        self.maxHp = 90

    def soigner(self, equipeAllie, equipeEnemie):
        robot_min_hp = None
        min_hp = 100
        for robot in equipeAllie:
            if 0 < robot.sante < robot.maxHp and robot.sante <= min_hp:
                min_hp = robot.sante
                robot_min_hp = robot

        if robot_min_hp is not None:
            if self.tauxCritique > random.random():
                robot_min_hp.sante += self.tauxSoin * 2 * self.lvl
            else:
                robot_min_hp.sante += self.tauxSoin * self.lvl

            if robot_min_hp.sante > robot_min_hp.maxHp:
                robot_min_hp.sante = robot_min_hp.maxHp
            if self.sante < self.maxHp:
                self.sante -= 10

            self.gagnerExperience(5)
            print("\n" + self.nom + " a soigné " + robot_min_hp.nom)
            print(robot_min_hp.nom + " a regagné " + str(robot_min_hp.sante - min_hp) + " points de vie")
            time.sleep(0.5)
        else:
            self.attaquer(equipeEnemie.randRobot())


# Robot qui attaque plus fort d'autre robot
class RobotSoldat(Robot):
    def __init__(self, nom, sante=100, competence="soldat"):
        Robot.__init__(self, nom, sante, competence)
        self.tauxAttaque = 25


# Robot qui attaque et soigne | Il attaque à 50% et il soigne à 50%
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
            self.soigner(equipeAllie, equipeEnemie)


# Robot qui attaque normalement tant qu'il n'a pas chargé son attaque spéciale
# sinon il lance un sort qui attaque tous les ennemies
class RobotMage(Robot):
    def __init__(self, nom, sante=70, competence="mage"):
        Robot.__init__(self, nom, sante, competence)
        self.maxHp = 70
        self.energie = 0
        self.tauxAttaque = 15
        self.degatsSorts = 25

    def gagnerEnergie(self):
        self.energie += 5 * self.lvl

    def lancerSort(self, equipeEnemie):
        print(self.nom + " lance son attaque spéciale\n")
        for robot in equipeEnemie.membreVivant():
            degats = self.degatsSorts * self.lvl
            if (self.tauxCritique > random.random()):
                degats *= 2
            robot.sante -= degats
            if robot.sante < 0:
                print(robot.nom + " est mort")
                robot.sante = 0
            else:
                print(robot.nom + " a perdu " + str(degats) + " points de vie")
        self.energie = 0
        time.sleep(0.5)


# Une équipe possède un nom et une liste de robot
class Equipe():
    def __init__(self, nom, robots):
        self.nom = nom
        self.equipe = []
        for robot in robots:
            self.equipe.append(robot)

    def ajouterRobot(self, robot):
        self.equipe.append(robot)

    # Selectionne un robot aléatoire dans une équipe (le robot doit être vivant)
    def randRobot(self):
        if len(self.membreVivant()) > 0:
            robot = random.choice(self.membreVivant())
            return robot
        else:
            return None

    # Méthode qui retourne les robots vivants dans une équipe
    def membreVivant(self):
        membre_vivants = []
        for robot in self.equipe:
            if robot.sante > 0:
                membre_vivants.append(robot)

        return membre_vivants

    # Affiche les points de vie des robots d'une équipe
    def afficherHp(self):
        print("\nSanté pour l'équipe : " + self.nom)
        for robot in self.equipe:
            if robot.sante == 0:
                print("Le robot " + robot.nom + " est mort.")
            else:
                print("Le robot " + robot.nom + " (lvl " + str(robot.lvl) + ") a : " + str(robot.sante) + " HP.")


# Déroulement d'une partie en tour par tour | Chaque équipe possède 4 robots
class Partie():
    # Si on veut lancer une partie normale on crée une partie sans paramètre
    # Si on veut lancer des parties de tests on lance une partie avec le paramètre à True
    def __init__(self, test=False):
        if test:
            self.equipe1 = Equipe("FullSoldat", [RobotSoldat("Soldat equipe1"), RobotSoldat("Soldat equipe1.2"),
                                                 RobotHybride("Hybride 1"), RobotMedecin("Medecin 1"),
                                                 RobotMage("Mage 1")])
            self.equipe2 = Equipe("healer", [RobotSoldat("Soldat equipe2"), RobotSoldat("Soldat equipe 2.2"),
                                             RobotSoldat("Hybride 2"), RobotHybride("Medecin 2"), RobotMage("Mage 2")])
        else:
            print("Duel entre le joueur 1 et le joueur 2: Combats de 4 robots dans chaque équpie !")
            nomEquipe1 = input("Joueur 1: choisir le nom de ton équipe :")
            self.equipe1 = self.creerEquipe(nomEquipe1)
            nomEquipe2 = input("Joueur 2: choisir le nom de ton équipe :")
            self.equipe2 = self.creerEquipe(nomEquipe2)

    # En début de partie chaque joueur devra constituer son équipe, choisir quatres robots de la classe qu"il veut et lui donner un nom.
    def creerEquipe(self, nom):
        equipe = []
        for i in range(4):
            nomRobot = input("Créer un robot, renseigne lui son nom :")
            print("Joueur 1, Renseigne le type de robot que tu veux :")
            typeRobot = input("1 = Robot soldat | 2 = Robot médecin | 3 = Robot hybride | 4 = Robot Mage")
            if (typeRobot == "1"):
                equipe.append(RobotSoldat(nomRobot))
            elif (typeRobot == "2"):
                equipe.append(RobotMedecin(nomRobot))
            elif (typeRobot == "3"):
                equipe.append(RobotHybride(nomRobot))
            elif (typeRobot == "4"):
                equipe.append(RobotMage(nomRobot))

        return Equipe(nom, equipe)

    # La partie commence, elle s'arrête quand une équipe a plus de robots vivant. Le joueur qui commence est décider aléatoirement.
    # Une fois qu'un robot a effectuer une action, c'est à l'équipe adverse de jouer.
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

    # Action que doit effectuer un robot suivant sa classe.
    def tour(self, equipeAllie, equipeEnemie, index):
        if equipeAllie[index].sante > 0:
            if equipeAllie[index].__class__.__name__ == "RobotHybride":
                equipeAllie[index].action(equipeAllie, equipeEnemie)
            elif equipeAllie[index].__class__.__name__ == "RobotSoldat":
                equipeAllie[index].attaquer(equipeEnemie.randRobot())
            elif equipeAllie[index].__class__.__name__ == "RobotMage":
                if equipeAllie[index].energie >= 9:
                    equipeAllie[index].lancerSort(equipeEnemie)
                else:
                    equipeAllie[index].attaquer(equipeEnemie.randRobot())
                equipeAllie[index].gagnerEnergie()
            elif equipeAllie[index].__class__.__name__ == "RobotMedecin":
                equipeAllie[index].soigner(equipeAllie, equipeEnemie)

    def afficherVictoire(self):
        if len(self.equipe1.membreVivant()) > 0:
            print("\nL'equipe " + self.equipe1.nom + " a gagné\n")
            self.equipe1.afficherHp()
            self.equipe2.afficherHp()
            return 1
        else:
            print("\nL'equipe " + self.equipe2.nom + " a gagné\n")
            self.equipe1.afficherHp()
            self.equipe2.afficherHp()
            return 2


for i in range(1):
    p = Partie()
    result = p.jouerTour()
