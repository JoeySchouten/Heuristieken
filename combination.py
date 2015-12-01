import csv
from classes import *
import random
from vrijstand import checkVrijstand
maxiteraties = 100

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
        del self.houses[(amt+bodies+1):]

    # berekening voor de min/max lengtes van het water
    def randWaterCalc(self, bodies):
        watersizes = []
        minwater = int(((self.map.width*self.map.length)*0.2)/bodies)
        for n in range(bodies):
            inrange = False
            foundrange = False
            rangemin = 0
            rangemax = 0
            for i in range(1,200):
                ratio = (minwater/i)/i
                if inrange == False:
                    if ratio >= 1 and ratio <=4:
                        rangemin = i
                        inrange = True
                elif inrange == True and foundrange == False:
                    if ratio < 1 or ratio > 4:
                        rangemax = i-1
                        foundrange = True
                else:
                    pass
            watersizes.append([])
            watersizes[n].append(random.randint(rangemin,rangemax))
            watersizes[n].append(minwater/watersizes[n][0])
        return watersizes

    def setWaterSizes(self, sizearray):
        #gaat ervanuit dat de laatste entries in de houselist water zijn
        n = 0
        for i in range(len(self.houses)):
            if self.houses[i].type == "Water":
                self.houses[i].setSize(sizearray[n][0],sizearray[n][1])
                n = n + 1

    # initializes class and initializes map and house list as well
    def __init__(self, amt, bodies):
        self.map = Map()
        self.houses = []
        self.bodies = bodies
        self.createHouseList(amt, bodies)
        if bodies > 0:
            self.watersizes = self.randWaterCalc(bodies)
            self.setWaterSizes(self.watersizes)
        self.evaluatie = []

    #function to place houses on map
    def placeAll(self):
        crawler = Point(0,0)
        miny = 0

        #range 1-12 doet het prima
        for x in range(len(self.houses)):
            #berekenen min. benodigde ruimte in totaal
            reqspacex = self.houses[x].minVrij * 2 + self.houses[x].width
            reqspacey = self.houses[x].minVrij * 2 + self.houses[x].length

            while self.houses[x].geplaatst == False:
                isLegal = True
                alignChanged = False

                # kijkt of point bestaat
                print "Kijken of punt ", crawler.x, crawler.y, "bestaat."
                while self.map.data.get((crawler.x, crawler.y)) == None:
                    crawler.move(self.map.width)
                    print "Punt bestaat niet, crawler verplaatst naar:", crawler.x, crawler.y
                print "Punt gevonden, controleren op ruimte:"

                # kijkt of point leeg is
                if self.map.data.get((crawler.x, crawler.y)) != None:
                    # kijkt of huis nog op de kaart past
                    if crawler.x + reqspacex > self.map.width:
                        crawler.x = 0
                        crawler.y = miny
                        print "Niet genoeg ruimte op x-as; crawler verplaatst naar ", crawler.x, crawler.y
                    elif crawler.y + reqspacey > self.map.length and changeAlign == True:
                        print "Niet genoeg ruimte op y-as; object wordt gedraaid."
                        self.houses[x].changeAlign()
                    elif crawler.y + reqspacey > self.map.length and changeAlign == True:
                        print "Niet genoeg ruimte op y-as; kaart vol. break."
                        break
                    else:
                        # controleren of gebied leeg is voor plaatsing huis
                        print "Genoeg ruimte op kaart vanaf dit punt. Controleren vrijstand:"
                        for z in range(reqspacex):
                            for y in range(reqspacey):
                                checkx = crawler.x + z
                                checky = crawler.y + y
                                if self.map.data.get((checkx, checky)) != "leeg":
                                    print "Punt", checkx, checky, "is niet leeg."
                                    isLegal = False
                    if isLegal == True:
                        #plaats huis
                        print "Gehele gebied is leeg. Plaatsen huis."
                        self.houses[x].place(crawler.x + self.houses[x].minVrij, crawler.y + self.houses[x].minVrij)
                        print "Invullen kaart"
                        #self.map.fill(crawler.x, crawler.y, self.houses[x].minVrij, self.houses[x].width, self.houses[x].length)
                        miny = crawler.y + reqspacey - self.houses[x].minVrij
                        crawler.setPoint((crawler.x + reqspacex-self.houses[x].minVrij), crawler.y)
                        print "Plaatsing gelukt, crawler verplaatst naar:", crawler.x, crawler.y
                    else:
                        crawler.move(self.map.width)
                        print "Plaatsing niet legaal, crawler verplaatst naar:", crawler.x, crawler.y
                else:
                    crawler.move(self.map.width)
                    print "Huidig punt is niet leeg, crawler verplaatst naar:", crawler.x, crawler.y

    # funtie voor het berekenen van de vrijstand van 1 huis
    def geefVrijstand(self, huis, index):
        vrijstand = 2000
        for i in range(len(self.houses)):
                if i == index:
                    pass
                else:
                    temp = checkVrijstand(huis, self.houses[i])
                    if temp < vrijstand:
                        vrijstand = temp
        return vrijstand

    def berekenWaarde(self, huis):
        if huis.extraVrij > 0:
            factor = 1 + ((huis.meerpermeter * huis.extraVrij)/100)
        else:
            factor = 1
        return huis.waarde * factor

    def evalueer(self):
        evaluatie = []
        vrijtotaal = 0
        geldtotaal = 0
        for i in range(len(self.houses)-self.bodies):
            #bereken vrijstand huis + sla op
            self.houses[i].extraVrij = self.geefVrijstand(self.houses[i], i)
            vrijtotaal = vrijtotaal + self.houses[i].extraVrij
            # bereken waarde huis
            geldtotaal = geldtotaal + self.berekenWaarde(self.houses[i])
        evaluatie.append(vrijtotaal)
        evaluatie.append(geldtotaal)
        self.evaluatie = evaluatie

    def placeRandom(self, huis, index):
        gelukt = False
        mogelijk = True
        iteraties = 0
        minx = 0 + huis.minVrij
        miny = 0 + huis.minVrij
        maxx = self.map.width - huis.minVrij
        maxy = self.map.length - huis.minVrij
        while gelukt == False:
            if iteratie == maxiteraties:
                return False
            # geef willekeurige waarden voor hoekpunt huis
            x = random.randint(minx,maxx)
            y = random.randint(miny,maxy)
            # controleer overlap met alle huizen
            for i in range(len(self.houses)):
                if i == index:
                    pass
                else:
                    if (self.houses[i].hoekpunt.x > x and self.houses[i].hoekpunt.x < x + huis.width) or ((self.houses[i].hoekpunt.x + self.houses[i].width) > x and (self.houses[i].x + self.houses[i].width) < x + huis.width):
        		        if (self.houses[i].hoekpunt.y > y and self.houses[i].hoekpunt.y < y + huis.length) or ((self.houses[i].hoekpunt.y + self.houses[i].length) > y and (self.houses[i].y + self.houses[i].length) < y + huis.y):
        			        # error-> plaatsen niet mogelijk
        			        mogelijk = False
            if mogelijk = True:
                huis.hoekpunt.setPoint(x,y)
                gelukt = True
            iteratie += 1
        return True


    #function to print to csv file for visualisation
    # output: corner x, corner y, length, width, type
    def printToCSV(self):
        output = open("output.csv", "wb")
        try:
            writer = csv.writer(output)
            for i in range(len(self.houses)):
                writer.writerow((self.houses[i].hoekpunt.x, self.houses[i].hoekpunt.y, self.houses[i].length, self.houses[i].width, self.houses[i].type))
            writer.writerow(("Totale Vrijstand:", self.evaluatie[0], "Totale Waarde:", self.evaluatie[1], "Wijkwaarden"))
        finally:
            output.close()
