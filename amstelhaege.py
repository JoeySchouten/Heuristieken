# create object containing "dumb solution"
dumbsol = Combination(20)

class Combination(object):
    # initializes class and initializes map and house list as well
    def __init__(self, int amt):
        self.map = Map()
        self.houses = []
        createHouseList(amt)

    # function to fill up house list in class, then shortens list if need be
    def createHouseList(int amt):
        for x in range(0.6*amt):
            self.houses.append(Eengezins())
        for x in range(0.25*amt):
            self.houses.append(Bungalow())
        for x in range(0.15*amt):
            self.houses.append(Villa())
        for x in range(4):
            self.houses.append(Water())
        len(self.houses) = amt + 4

    #function to place houses on map
    def placeAll(self):
        # coordinates in x,y format
        crawler = Point(0,0)
        # loop to place houses
        for i in range(len(self.houses)):
            while self.houses[i].geplaast == False:
                reqspacex=(2*self.houses[i].minVrij+self.houses[i].width)
                reqspacey=(2*self.houses[i].minVrij+self.houses[i].length)
                # check if crawler point is empty and if house can be placed (move to own boolean fucntion?)
                # TODO: does not check whether the min. free space is honoured
                # TODO: fill map data
                if (self.map.data[crawler.x,crawler.y] == "leeg" and
                (crawler.x + reqspacex !> self.map.width and
                (crawler.y + reqspacey !> self.map.length):
                    self.houses[i].place(crawler.x, crawler.y)
                    # offsets dictionary key to include vrijstand
                    keyx = crawler.x-self.houses[i].minVrij
                    keyy = crawler.y-self.houses[i].minVrij)
                    self.map.fill(keyx, keyy ,self.houses[i].minVrij, self.houses[i].width, self.houses[i].length)
                    crawler.setPoint(crawler.x+reqspacex, crawler.y+reqspacey)
                # else move crawler point and try again; if crawler is out of bounds, set x to 0, y++ (also make its own function?)
                else:
                    crawler.setPoint(crawler.x+1,crawler.y)
                    if crawler.x > self.map.width:
                        crawler.setPoint(0,crawler.y+1)

    #function to print to csv file for visualisation
    def printToCSV():

class Point(object):
    def __init__(self, int x, int y):
        self.x = x
        self.y = y

    def setPoint(self, int x, int y):
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

    def fill(self, int keyx, int keyy, int vrij, int width, int height):
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
        float self.length = 0
        float self.width = 0
        bool self.isVertical = False
        float self.minVrij = 0
        self.hoekpunt = Point()
        bool self.geplaatst = False

    def setSize(self, float length, float width):
        self.length = length
        self.width = width

    def changeAlign(self):
        setSize(self.width, self.length)
        if self.isVertical = False:
            self.isVertical = True
        else:
            self.isVertical = False

    def place(self, int x, int y):
        self.hoekpunt.setPoint(x,y)
        self.geplaatst = True

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
    def __init__(self):
        float self.length = 0
        float self.width = 0

    def setSize(self, float length, float width):
        self.length = length
        self.width = width
