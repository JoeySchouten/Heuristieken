import csv
from classes import *
import random

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

    # berekening voor de min/max lengtes van het water (gaan nu even uit van 1 lichaam)
    def randWaterCalc(bodies):
        watersizes = []
        minwater = 4800
        for x in range(bodies):
            surface[x] = int((1/bodies)*minwater)
        for n in range(bodies):
            inrange = False
            rangemin = 0
            rangemax = 0
            for i in range(1,200):
                ratio = (surface[n]/i)/i
                if inrange == False:
                    if ratio >= 1 and ratio <=4:
                        rangemin = i
                        inrange = True
                else:
                    if ratio < 1 or ratio > 4:
                        rangemax = i-1
                        break
            watersizes[n][0] = random.randint(rangemin,rangemax)
            watersizes[n][1] = minwater/watersizes[n][0]
        return watersizes

    def setSizes(self, sizearray):
        #gaat ervanuit dat de laatste 4 entries in de houselist water is
        n = 0
        for i in range(len(self.houses[-4 : (len(sizearray)) ])):
            self.houses[i].setSize(sizearray[n][0],sizearray[n][1])
            n = n + 1

    # initializes class and initializes map and house list as well
    def __init__(self, amt, bodies):
        self.map = Map()
        self.houses = []
        self.createHouseList(amt)
        self.setSizes(self.randWaterCalc(bodies))


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
