class Combination(object):
    def __init__(self, int amt):
        self.map = Map()
        self.houses = []
        createHouseList(amt)

    def createHouseList(int amt):
        for x in range(0.6*amt):
            self.houses.append(Eengezins())
        for x in range(0.25*amt):
            self.houses.append(Bungalow())
        for x in range(0.15*amt):
            self.houses.append(Villa())
        for x in range(4):
            self.houses.append(Water())

class Point(object):
    def __init__(self, int x, int y):
        self.x = x
        self.y = y

class Checkpoint(Point):
    def __init__(self):
        self.x = 0
        self.y = 0

class Map(object):
    def __init__(self):
        self.data = dict()
        float self.length = 150.0
        float self.width = 160.0
        self.checkpoint = Checkpoint()

    def initializeMap(self):
        for x in range(self.length):
            for y in range(self.width):
                self.data[x,y] = "leeg"

    def lookup(self, Point point):
        return self.data[point.x, point.y]


class House(object):
    """overkoepelende klasse voor alle soorten huizen; wordt zelf niet geintieerd, maar levert alle gezamelijke onderdelen
    door middel van inheritance"""
    def __init__(self):
        float self.length = 0
        float self.width = 0
        bool self.isVertical = False
        float self.minVrij = 0
        self.hoekpunt = Point()

    def setSize(float length, float width):
        self.length = length
        self.width = width

    def changeAlign(self):
        setSize(self.width, self.length)
        if self.isVertical = False:
            self.isVertical = True
        else:
            self.isVertical = False

    def place(self, int x, int y):


class Eengezins(House):
    def __init__(self):
        super().__init__()
        setSize(8.0,8.0)
        self.minVrij = 2.0

class Bungalow(House):
    def __init__(self):
        super().__init__()
        setSize(10.0,7.5)
        self.minVrij = 3.0

class Villa(House):
    def __init__(self):
        super().__init__()
        setSize(10.5,11.0)
        self.minVrij = 6.0

class Water(object):
