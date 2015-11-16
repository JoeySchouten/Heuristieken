import csv

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setPoint(self, x, y):
        self.x = x
        self.y = y

class Map(object):
    def __init__(self):
        self.data = dict()
        self.length = 300
        self.width = 320

    def initializeMap(self):
        for x in range(self.length):
            for y in range(self.width):
                self.data[x,y] = True

    def fill(self, keyx, keyy, vrij, width, height):
        # vul rijen met complete vrijstand
        for i in range(vrij):
            for n in range(width+2*vrij):
                self.data[keyx+i,keyy+n] = "moetvrij"
        #vul rijen met vrijstand|huis|vrijstand
        #set hoogte key opnieuw voor leesbare coordinates
        keyy= keyy+vrij
        for a in range(height):
            # loop vrijstand
            for b in range(vrij):
                self.data[keyx+b,keyy+a] = "moetvrij"
            # loop huis
            for c in range(width):
                self.data[keyx+b+c,keyy+a] = "huis"
            # loop vrijstand
            for d in range(vrij):
                self.data[keyx+b+c+d,keyy+a] = "moetvrij"
        #vul rijen met complete vrijstand weer
        keyy= keyy+height
        for j in range(vrij):
            for n in range(width+2*vrij):
                self.data[keyx+i,keyy+n] = "moetvrij"


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

    def setSize(self, length, width):
        self.length = length
        self.width = width

class Combination(object):
    # function to fill up house list in class, then shortens list if need be
    def createHouseList(self, amt):
        for x in range(int(0.6*amt)):
            self.houses.append(Eengezins())
        for x in range(int(0.25*amt)):
            self.houses.append(Bungalow())
        for x in range(int(0.15*amt)):
            self.houses.append(Villa())
        for x in range(4):
            self.houses.append(Water())
        return len(self.houses) == amt + 4

    # initializes class and initializes map and house list as well
    def __init__(self, amt):
        self.map = Map()
        self.houses = []

    #function to place houses on map
    def placeAll(self):
        # coordinates in x,y format
        crawler = Point(0,0)
        # loop to place houses
        for i in range(len(self.houses)):
            while self.houses[i].geplaatst == False:
                reqspacex=(2*self.houses[i].minVrij+self.houses[i].width)
                reqspacey=(2*self.houses[i].minVrij+self.houses[i].length)
                # check if crawler point is empty and if house can be placed (move to own boolean fucntion?)
                # TODO: does not check whether the min. free space is honoured
                # TODO: fill map data
                if (self.map.data.get(crawler.x, crawler.y) and
                crawler.x + reqspacex <= self.map.width and
                crawler.y + reqspacey <= self.map.length):
                    self.houses[i].place(crawler.x, crawler.y)
                    print(crawler.x, crawler.y)
                    # offsets dictionary key to include vrijstand
                    keyx = crawler.x-self.houses[i].minVrij
                    keyy = crawler.y-self.houses[i].minVrij
                    self.map.fill(keyx, keyy, self.houses[i].minVrij, self.houses[i].width, self.houses[i].length)
                    crawler.setPoint(crawler.x+reqspacex, crawler.y)
                # else move crawler point and try again; if crawler is out of bounds, set x to 0, y++ (also make its own function?)
                else:
                    crawler.setPoint(crawler.x+1,crawler.y)
                    if crawler.x > self.map.width:
                        crawler.setPoint(0,crawler.y+1)

    #function to print to csv file for visualisation
    # output: corner x, corner y, length, width, type
    def printToCSV(self):
        output = open("output.csv", "w")
        try:
            writer = csv.writer(output)
            for i in range(len(self.houses)):
                writer.writerow((self.houses[i].hoekpunt.x, self.houses[i].hoekpunt.y, self.houses[i].length, self.houses[i].width, self.houses[i].type))
        finally:
            output.close()


# create object containing "dumb solution"
dumbsol = Combination(20)
dumbsol.createHouseList(20)
dumbsol.map.initializeMap()
dumbsol.placeAll()
dumbsol.printToCSV()
