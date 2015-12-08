import csv
from combination import Combination
import random
from graph import *
import matplotlib.pyplot as plt

attempts = 0
maxattempts = 100

# maak een random beginsituatie
error = True
combinatie = Combination(aantalhuizen, aantalwater)
while error == True:
    error = False
    for i in range(len(combinatie.houses)):
        if combinatie.placeRandom(combinatie.houses[i], i) != True:
            error = True
combinatie.evalueer()
tempeval = combinatie.evaluatie
if tempeval[1] > hoogstewaarde:
    hoogstewaarde = tempeval[1]
    best = combinatie
uitkomsten.append(hoogstewaarde)

while attempts < maxattempts:
    # kies een willekeurig huis (shuffle array en dan de 1e)
    random.shuffle(combinatie.houses)
    # bereken extra vrijstand van huis
    temp = combinatie.geefVrijstand(combinatie.houses[0], 0)
    if temp > 0:
        huis = combinatie.houses[0]
        hoek = combinatie.houses[0].hoekpunt
        #   kies plaats om naar toe te schuiven
        newx = random.randint(hoek.x - temp, hoek.x + temp)
        newy = random.randint(hoek.y - temp, hoek.y + temp)
        #   indien mogelijk: verplaats
        mogelijk = True
        for i in range(1, len(combinatie.houses)):
                xH2 = combinatie.houses[i].hoekpunt.x
                yH2 = combinatie.houses[i].hoekpunt.y
                #check if H2 left and right corners are within H1's x-range
                if (newx - huis.minVrij <= xH2 <= newx + huis.width + huis.minVrij) or (newx - huis.minVrij <= xH2+combinatie.houses[i].width <= newx + huis.width + huis.minVrij):
                    #check if H2 top and bottom corners are within H1's y-range
                    if (newy - huis.minVrij <= yH2 <= newy + huis.length + huis.minVrij) or (newy - huis.minVrij <= yH2+combinatie.houses[i].length <= newy + huis.length + huis.minVrij):
                        mogelijk = False
                #check if H1 left and right corners are within H2's x-range
                if (xH2 - combinatie.houses[i].minVrij <= newx <= xH2 + combinatie.houses[i].width + combinatie.houses[i].minVrij) or (xH2 - combinatie.houses[i].minVrij <= newx+huis.width <= xH2 + combinatie.houses[i].width + combinatie.houses[i].minVrij):
                    #check if H1 top and bottom corners are within H2's y-range
                    if (yH2 - combinatie.houses[i].minVrij <= newy <= yH2+combinatie.houses[i].length + combinatie.houses[i].minVrij) or (yH2 - combinatie.houses[i].minVrij <= newy+huis.length <= yH2 + combinatie.houses[i].length + combinatie.houses[i].minVrij):
                        mogelijk = False
                # checken van water om 'kruisingen' te voorkomen
                # betekent dat beide delen wel in elkaars bereik liggen, maar de punten zelf niet.
        if mogelijk == True:
            huis.hoekpunt.setPoint(newx,newy)
    else:
        # indien geen: opnieuw huis kiezen
        pass
    attempts += 1
# bereken waarde; indien hoger, bewaren en opnieuw. Anders verwerpen en opnieuw
