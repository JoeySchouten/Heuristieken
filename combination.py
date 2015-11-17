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
        output = open("output.csv", "wb")
        try:
            writer = csv.writer(output)
            for i in range(len(self.houses)):
                writer.writerow((self.houses[i].hoekpunt.x, self.houses[i].hoekpunt.y, self.houses[i].length, self.houses[i].width, self.houses[i].type))
        finally:
            output.close()
