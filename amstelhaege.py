class Point(object):
    int x
    int y

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

class Bungalow(House):
    def __init__(self):
        super().__init__()
        setSize(10.0,7.5)

class Villa(House):
    def __init__(self):
        super().__init__()
        setSize(10.5,11.0)
