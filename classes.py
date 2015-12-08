from random import randint

class House(object):
    """overkoepelende klasse voor alle soorten huizen; wordt zelf niet geintieerd, maar levert alle gezamelijke onderdelen
    door middel van inheritance"""
    def __init__(self):
        self.length = 0
        self.width = 0
        self.isVertical = False
        self.minVrij = 0
        self.hoekpunt = Point(0,0)
        self.geplaatst = False
        self.extraVrij = 0
        self.waarde = 0
        self.meerpermeter = 0

    def setSize(self, length, width):
        self.length = length
        self.width = width

    def changeAlign(self):
        setSize(self.width, self.length)
        if self.isVertical == False:
            self.isVertical = True
        else:
            self.isVertical = False

    def place(self, x, y):
        self.hoekpunt.setPoint(x,y)
        self.geplaatst = True

class Eengezins(House):
    def __init__(self):
        super(Eengezins, self).__init__()
        super(Eengezins, self).setSize(16,16)
        self.minVrij = 4
        self.type = "Eengezins"
        self.waarde = 285000
        self.meerpermeter = 3

class Bungalow(House):
    def __init__(self):
        super(Bungalow, self).__init__()
        super(Bungalow, self).setSize(20,15)
        self.minVrij = 6
        self.type = "Bungalow"
        self.waarde = 399000
        self.meerpermeter = 4

class Villa(House):
    def __init__(self):
        super(Villa, self).__init__()
        super(Villa, self).setSize(21,22)
        self.minVrij = 12
        self.type = "Villa"
        self.waarde = 610000
        self.meerpermeter = 6

class Water(House):
    def __init__(self):
        super(Water, self).__init__()
        self.type = "Water"
        self.minVrij = 1

    def setSize(self, length, width):
        self.length = length
        self.width = width

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setPoint(self, x, y):
        self.x = x
        self.y = y

    def move(self, mapWidth):
        self.x += 1
        if self.x > mapWidth:
            self.x = 0
            self.y += 1

class Map(object):
    def __init__(self):
        self.length = 300
        self.width = 320


def createRandom():
    error = True
    while error == True:
        error = False
        # probeer random kaart te bouwen tot het lukt
        combinatie = Combination(aantalhuizen, aantalwater)
        for i in range(len(combinatie.houses)):
            if combinatie.placeRandom(combinatie.houses[i], i) != True:
                error = True
        if error == False:
            combinatie.evalueer()
            temp = combinatie.evaluatie
            hoogstewaarde = temp[1]
            best = combinatie
            best.evalueer()
            best.printToCSV()
            uitkomsten.append(hoogstewaarde)
            plt.plot(iteratie, hoogstewaarde, '.-r')
            plt.draw()
            plt.savefig('graph.png', dpi=300, bbox_inches='tight')
    return combinatie
