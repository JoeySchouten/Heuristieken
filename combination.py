import csv
from classes import *

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
        self.createHouseList(amt)

    #function to place houses on map
    def placeAll(self):
        # coordinates in x,y format
        crawler = Point(0,0)
        # loop to place houses
        for i in range(len(self.houses)):
            reqspacex=2*self.houses[i].minVrij+self.houses[i].width
            reqspacey=2*self.houses[i].minVrij+self.houses[i].length
            while self.houses[i].geplaatst == False:
                print crawler.x, crawler.y
                # check if crawler point exists
                if self.map.data.get(crawler.x, crawler.y) != None:
                    # if crawler point is not empty, go to next point
                    if (self.map.data.get(crawler.x, crawler.y) == "huis" or
                        self.map.data.get(crawler.x, crawler.y) == "moetvrij"):
                        crawler.setPoint(crawler.x+1, crawler.y)
                        if crawler.x > self.map.width:
                            crawler.setPoint(0, crawler.y+1)
                    # else if there is enough space, place house
                    elif crawler.x + reqspacex <= self.map.width and crawler.y + reqspacey <= self.map.length:
                        self.houses[i].place(crawler.x, crawler.y)
                        # offsets dictionary key to include vrijstand
                        keyx = crawler.x-self.houses[i].minVrij
                        keyy = crawler.y-self.houses[i].minVrij
                        self.map.fill(keyx, keyy, self.houses[i].minVrij, self.houses[i].width, self.houses[i].length)
                        crawler.setPoint(crawler.x+reqspacex, crawler.y)
                    # else go to next row
                    else:
                        crawler.setPoint(0, crawler.y+1)

    #function to print to csv file for visualisation
    # output: corner x, corner y, length, width, type
    def printToCSV(self):
        output = open("output.csv", "wb")
        try:
            writer = csv.writer(output)
            for i in range(len(self.houses)):
                writer.writerow((self.houses[i].hoekpunt.x, self.houses[i].hoekpunt.y, self.houses[i].length, self.houses[i].width, self.houses[i].type))
        finally:
            output.close()
