import csv
from classes import *
import random

class Combination(object):
    # function to fill up house list in class, then shortens list if need be
    def createHouseList(self, amt, bodies):
        for x in range(int(0.6*amt)):
            self.houses.append(Eengezins())
        for x in range(int(0.25*amt)):
            self.houses.append(Bungalow())
        for x in range(int(0.15*amt)):
            self.houses.append(Villa())
        for x in range(bodies):
            self.houses.append(Water())
        return len(self.houses) == amt + bodies

    # berekening voor de min/max lengtes van het water (gaan nu even uit van 1 lichaam)
    def randWaterCalc(self, bodies):
        watersizes = []
        minwater = 4800
        surface = []
        for x in range(bodies):
            surface.append(int((1/bodies)*minwater))
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
            watersizes.append([])
            watersizes[n].append(random.randint(rangemin,rangemax))
            watersizes[n].append(minwater/watersizes[n][0])
        return watersizes

    def setWaterSizes(self, sizearray):
        #gaat ervanuit dat de laatste 4 entries in de houselist water is
        n = 0
        for i in range(len(self.houses[-self.bodies : (len(sizearray)) ])):
            self.houses[i].setSize(sizearray[n][0],sizearray[n][1])
            n = n + 1

    # initializes class and initializes map and house list as well
    def __init__(self, amt, bodies):
        self.map = Map()
        self.houses = []
        self.bodies = bodies
        self.createHouseList(amt, bodies)
        self.setWaterSizes(self.randWaterCalc(bodies))

    #function to place houses on map
    def placeAll(self):
        crawler = Point(0,0)
        for x in range(len(self.houses)):
            reqspacex = self.houses[x].minVrij * 2 + self.houses[x].width
            reqspacey = self.houses[x].minVrij * 2 + self.houses[x].length
            while self.houses[x].geplaatst == False:
                isLegal = True
                # kijkt of point bestaat
                while self.map.data.get(crawler.x, crawler.y) == None:
                    crawler.move(self.map.width)
                # kijkt of point leeg is
                if self.map.data.get(crawler.x, crawler.y) != None:
                    # kijkt of huis nog op de kaart past
                    if crawler.x + reqspacex > self.map.width:
                        crawler.x = 0
                        crawler.y += 1
                    elif crawler.y + reqspacey > self.map.length:
                        break
                    else:
                        for i in range(reqspacex):
                            for n in range(reqspacey):
                                if self.map.data.get(crawler.x + i, crawler.y + n) != True:
                                    isLegal = False
                        if isLegal == True:
                            #plaats huis
                            self.houses[x].place(crawler.x + self.houses[x].minVrij, crawler.y + self.houses[x].minVrij)
                            print i, crawler.x, crawler.y
                            self.map.fill(crawler.x, crawler.y, self.houses[x].minVrij, self.houses[x].width, self.houses[x].length)
                            crawler.setPoint(crawler.x + reqspacex, crawler.y)
                        else:
                            crawler.move(self.map.width)
                else:
                    crawler.move(self.map.width)


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
