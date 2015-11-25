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

class Bungalow(House):
    def __init__(self):
        super(Bungalow, self).__init__()
        super(Bungalow, self).setSize(20,15)
        self.minVrij = 6
        self.type = "Bungalow"

class Villa(House):
    def __init__(self):
        super(Villa, self).__init__()
        super(Villa, self).setSize(21,22)
        self.minVrij = 12
        self.type = "Villa"

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
                self.data = dict()
                self.length = 300
                self.width = 320
                self.initializeMap()

    def initializeMap(self):
        for x in range(self.length):
            for y in range(self.width):
                self.data[x,y] = "leeg"

    def fill(self, keyx, keyy, vrij, width, length):
        # vul rijen met complete vrijstand
        for i in range(vrij):
            for n in range(width+2*vrij):
                self.data[keyx+i,keyy+n] = "moetvrij"
        #vul rijen met vrijstand|huis|vrijstand
        #set hoogte key opnieuw voor leesbare coordinates
        keyy+=vrij
        progress = 0
        for a in range(length):
            # loop vrijstand
            for b in range(vrij):
                self.data[keyx+progress,keyy+a] = "moetvrij"
                progress = progress + 1
            # loop huis
            for c in range(width):
                self.data[keyx+progress,keyy+a] = "huis"
                progress = progress + 1
            # loop vrijstand
            for d in range(vrij):
                self.data[keyx+progress,keyy+a] = "moetvrij"
                progress = progress + 1
        #vul rijen met complete vrijstand weer
        keyy= keyy+length
        for j in range(vrij):
            for n in range(width+2*vrij):
                self.data[keyx+i,keyy+n] = "moetvrij"
