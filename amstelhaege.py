class Point(object):
    int x
    int y

    """functie die snel punt levert voor dictionary keys in format [x,y]"""
    def getPoint(self):
        return self.x + "," + self.y

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
        setSize(8,8)

class Bungalow(House):
    def __init__(self):
        super().__init__()
        setSize(10,7.5)

class Villa(House):
    def __init__(self):
        super().__init__()
        setSize(10.5,11)
