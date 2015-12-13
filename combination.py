from classes import *
import random
from vrijstand import checkVrijstand

class Combination(object):
    # function to fill up house list in class, then shortens list if need be
    def createHouseList(self, amt, bodies):
        for x in range(bodies):
            self.houses.append(Water())
        for x in range(int(0.15*amt)):
            self.houses.append(Villa())
        for x in range(int(0.25*amt)):
            self.houses.append(Bungalow())
        for x in range(int(0.6*amt)):
            self.houses.append(Eengezins())
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
        self.evaluatie = [0,0]

    # funtie voor het berekenen van de vrijstand van 1 huis
    def geefVrijstand(self, huis, index):
        vrijstand = 2000
        for i in range(len(self.houses) - self.bodies):
                if i == index:
                    pass
                else:
                    temp = checkVrijstand(huis, self.houses[i])
                    if temp < vrijstand:
                        vrijstand = temp
        return vrijstand - huis.minVrij

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
        for i in range(len(self.houses) - self.bodies):
            #bereken vrijstand huis + sla op
            self.houses[i].extraVrij = self.geefVrijstand(self.houses[i], i)
            vrijtotaal += self.houses[i].extraVrij
            # bereken waarde huis
            geldtotaal += self.berekenWaarde(self.houses[i])
        evaluatie.append(vrijtotaal)
        evaluatie.append(geldtotaal)
        self.evaluatie = evaluatie

    def placeRandom(self, huis, index):
        gelukt = False
        mogelijk = True
        maxiteraties = 1000
        iteraties = 0
        minx = 0 + huis.minVrij
        miny = 0 + huis.minVrij
        maxx = self.map.width - (huis.minVrij + huis.width)
        maxy = self.map.length - (huis.minVrij + huis.length)
        while gelukt == False:
            if iteraties == maxiteraties:
                return False
            # geef willekeurige waarden voor hoekpunt huis
            xH1 = random.randint(minx,maxx)
            yH1 = random.randint(miny,maxy)
            mogelijk = True

            # controleer overlap met alle huizen
            for i in range(len(self.houses)):
                if i == index:
                    pass
                else:
                    xH2 = self.houses[i].hoekpunt.x
                    yH2 = self.houses[i].hoekpunt.y
                    #check if H2 left and right corners are within H1's x-range
                    if (xH1 - huis.minVrij <= xH2 <= xH1 + huis.width + huis.minVrij) or (xH1 - huis.minVrij <= xH2+self.houses[i].width <= xH1 + huis.width + huis.minVrij):
                        #check if H2 top and bottom corners are within H1's y-range
                        if (yH1 - huis.minVrij <= yH2 <= yH1 + huis.length + huis.minVrij) or (yH1 - huis.minVrij <= yH2+self.houses[i].length <= yH1 + huis.length + huis.minVrij):
                            mogelijk = False
                    #check if H1 left and right corners are within H2's x-range
                    if (xH2 - self.houses[i].minVrij <= xH1 <= xH2 + self.houses[i].width + self.houses[i].minVrij) or (xH2 - self.houses[i].minVrij <= xH1+huis.width <= xH2 + self.houses[i].width + self.houses[i].minVrij):
                        #check if H1 top and bottom corners are within H2's y-range
                        if (yH2 - self.houses[i].minVrij <= yH1 <= yH2+self.houses[i].length + self.houses[i].minVrij) or (yH2 - self.houses[i].minVrij <= yH1+huis.length <= yH2 + self.houses[i].length + self.houses[i].minVrij):
                            mogelijk = False
                    # checken van water om 'kruisingen' te voorkomen
                    # betekent dat beide delen wel in elkaars bereik liggen, maar de punten zelf niet.
            if mogelijk == True:
                huis.hoekpunt.setPoint(xH1,yH1)
                gelukt = True
            iteraties += 1
        return True
