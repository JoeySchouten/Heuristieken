import sys
import random
import matplotlib.pyplot as plt
import math
import copy
from combination import Combination
from graph import *
from schuiven import schuiven
from swap import swappen

def createRandom():
    error = True
    while error == True:
        error = False
        # probeer random kaart te bouwen tot het lukt
        combinatie = Combination(aantalhuizen, aantalwater)
        random.shuffle(combinatie.houses)
        for i in range(len(combinatie.houses)):
            if combinatie.placeRandom(combinatie.houses[i], i) != True:
                error = True
        if error == False:
            combinatie.evalueer()
            temp = combinatie.evaluatie
            hoogstewaarde = temp[1]
            best = combinatie
            best.evalueer()
            plt.draw()
            plt.savefig('graph.png', dpi=300, bbox_inches='tight')
    return combinatie

def informWrongUsage():
    print "Incorrect aantal huizen opgegeven. Correct gebruik:"
    print "python main.py [aantal huizen] [methode] [score]"
    print "aantal huizen: 20, 40 of 60"
    print "methode: randsample, schuiven, swappen of annealingschuiven"
    print "score: waarde of vrijstand"
    sys.exit()

def annealingKans(nieuw, oud, temperatuur):
    # bereken verschil, wanneer de nieuwe lager is dan de oude -> negatieve waarde
    # bijv nieuw = 20, oud = 25, verschil is -5
    verschil = nieuw - oud
    #wanneer nieuwe beter is dan oude (hoger dus), sowieso aannemen
    if verschil > 0:
        kans = 1.0
    else:
        kans = (math.exp(verschil/temperatuur))
    #print kans
    return kans

# toegestane opties command line arguments
toegestanehuizen = [20,40,60]
toegestanemethoden = ["randsample", "schuiven", "swappen", "annealingschuiven"]
toegestanescore = ["waarde", "vrijstand"]

aantalhuizen = int(sys.argv[1])
aantalwater = 4
uitkomsten = []
iteraties = []
hoogstewaarde = 0
iteratie = 0
maxverwerpen = 100
verwerpen = 0
best = 0

# waarden Simulated Annealing
begintemperatuur = 150
afkoeling = 0.012
gestoldbij = 10

# 0 = scoren op vrijstand; 1 = scoren op waarde in euro's
criterium = 0

#  afvangen hoeveelheid arguments!
if len(sys.argv) != 4:
    informWrongUsage()
# sys.argv[] -> 1: aantal huizen; 2:methode; 3: score criterium
if int(sys.argv[1]) not in toegestanehuizen:
    informWrongUsage()
elif str(sys.argv[2]) not in toegestanemethoden:
    informWrongUsage()
elif str(sys.argv[3]) not in toegestanescore:
    informWrongUsage()

if str(sys.argv[3]) == "waarde":
    criterium = 1

# barchart waarden
bakjes = []
waardeperbakje = 0
aantalbakjes = 0
if criterium == 1:
    waardeperbakje = 250000
    aantalbakjes = 500
elif criterium == 0:
    waardeperbakje = 25
    aantalbakjes = 30
for i in range(aantalbakjes):
    bakjes.append(0)

# bouwen grafiek
graphcolour = 'r'
plt.figure(1)
plt.xlabel('Iteraties')
plt.ylabel('Waarde in Euro\'s')
plt.suptitle("Hoogste huidige waarde: " + str(hoogstewaarde) + " Huidige iteratie: " + str(iteratie), fontsize=13)
filename = 'output/' + str(sys.argv[3]) + "/" + str(sys.argv[1]) + str(sys.argv[2])
graphtitle = str(sys.argv[2]) + " " + str(sys.argv[1])

if sys.argv[2] == "randsample":
    plt.title('Amstelhaege Random Sampling')
    while True:
        error = False
        update = False
        combinatie = Combination(aantalhuizen, aantalwater)
        for i in range(len(combinatie.houses)):
            if combinatie.placeRandom(combinatie.houses[i], i) != True:
                error = True
        if error == False:
            combinatie.evalueer()
            temp = combinatie.evaluatie
            if temp[criterium] > hoogstewaarde:
                hoogstewaarde = temp[criterium]
                best = combinatie
                best.evalueer()
                mapMaken(best.houses, filename, graphtitle, iteratie, hoogstewaarde)
                update = True
        index = int(combinatie.evaluatie[criterium] / waardeperbakje)
        if error != True:
            bakjes[index] += 1
        uitkomsten.append(hoogstewaarde)
        iteraties.append(iteratie)
        if update == True:
            updateGraph(filename, iteraties, iteratie, uitkomsten, hoogstewaarde)
        if iteratie%2500 == 0 and best != 0:
            createBarChart(determineRange(bakjes), waardeperbakje, filename, graphtitle, criterium, iteratie)
            updateGraph(filename, iteraties, iteratie, uitkomsten, hoogstewaarde)
            mapMaken(best.houses, filename, graphtitle, iteratie, hoogstewaarde)
        iteratie += 1

elif str(sys.argv[2]) == "schuiven":
    plt.title('Amstelhaege Schuif-Hillclimber')
    combinatie = createRandom()
    # ga schuiven
    while True:
        update = False
        if verwerpen > maxverwerpen:
            verwerpen = 0
            if best != 0 and best.evaluatie[criterium] < combinatie.evaluatie[criterium]:
                best = combinatie
                mapMaken(best.houses, filename, graphtitle, iteratie, hoogstewaarde)
                update = True
            elif best == 0:
                best = combinatie
                mapMaken(best.houses, filename, graphtitle, iteratie, hoogstewaarde)
                update = True
            index = int(combinatie.evaluatie[criterium] / waardeperbakje)
            bakjes[index] += 1
            combinatie = createRandom()
        if schuiven(combinatie) == True:
            combinatie.evalueer()
            temp = combinatie.evaluatie
            if temp[criterium] > hoogstewaarde:
                hoogstewaarde = temp[criterium]
                verwerpen = 0
            else:
                verwerpen +=1
        else:
            verwerpen +=1
        uitkomsten.append(hoogstewaarde)
        iteraties.append(iteratie)
        if update == True:
            updateGraph(filename, iteraties, iteratie, uitkomsten, hoogstewaarde)
        if iteratie%2500 == 0 and best != 0:
            createBarChart(determineRange(bakjes), waardeperbakje, filename, graphtitle, criterium, iteratie)
            updateGraph(filename, iteraties, iteratie, uitkomsten, hoogstewaarde)
        iteratie += 1

elif str(sys.argv[2]) == "swappen":
    plt.title('Amstelhaege Swap-Hillclimber')
    combinatie = createRandom()
    # ga swappen
    while True:
        update = False
        if verwerpen > maxverwerpen:
            verwerpen = 0
            if best != 0 and best.evaluatie[criterium] < combinatie.evaluatie[criterium]:
                best = combinatie
                mapMaken(best.houses, filename, graphtitle, iteratie, hoogstewaarde)
                update = True
            elif best == 0:
                best = combinatie
                mapMaken(best.houses, filename, graphtitle, iteratie, hoogstewaarde)
                update = True
            index = int(combinatie.evaluatie[criterium] / waardeperbakje)
            bakjes[index] += 1
            combinatie = createRandom()
        if swappen(combinatie) == True:
            combinatie.evalueer()
            temp = combinatie.evaluatie
            if temp[criterium] > hoogstewaarde:
                hoogstewaarde = temp[criterium]
                verwerpen = 0
            else:
                verwerpen +=1
        else:
            verwerpen +=1
        uitkomsten.append(hoogstewaarde)
        iteraties.append(iteratie)
        if update == True:
            updateGraph(filename, iteraties, iteratie, uitkomsten, hoogstewaarde)
        if iteratie%2500 == 0 and best != 0:
            createBarChart(determineRange(bakjes), waardeperbakje, filename, graphtitle, criterium, iteratie)
            updateGraph(filename, iteraties, iteratie, uitkomsten, hoogstewaarde)
        iteratie += 1

elif str(sys.argv[2]) == "annealingschuiven":
    plt.title('Amstelhaege Simulated Annealing Schuiven')
    olddelta = 0
    delta = 0
    while True:
        combinatie = createRandom()
        random.shuffle(combinatie.houses)
        oldcombi = copy.deepcopy(combinatie)
        temperatuur = begintemperatuur
        huidigewaarden = []
        huidigeiteraties = []
        while temperatuur > gestoldbij:
            update = False
            iteratie += 1
            if iteratie%4500 == 0:
                update = True
            if schuiven(combinatie) == True:
                combinatie.evalueer()
                if criterium == 1:
                    delta = int(combinatie.evaluatie[criterium] / 25000)
                    kans = annealingKans(delta, olddelta, temperatuur)
                else:
                    kans = annealingKans(combinatie.evaluatie[criterium], oldcombi.evaluatie[criterium], temperatuur)
                if random.random() < kans:
                    # bewaar nieuwe combinatie
                    oldcombi = copy.deepcopy(combinatie)
                    olddelta = copy.copy(delta)
                else:
                    # houd oude combi
                    combinatie = copy.deepcopy(oldcombi)
                    combinatie.evalueer()
                    temp = combinatie.evaluatie
                hoogstewaarde = combinatie.evaluatie[criterium]
            uitkomsten.append(hoogstewaarde)
            iteraties.append(iteratie)
            huidigewaarden.append(hoogstewaarde)
            huidigeiteraties.append(iteratie)
            temperatuur *= 1-afkoeling
        if best == 0:
            best = oldcombi
        if oldcombi.evaluatie[criterium] >= best.evaluatie[criterium]:
            best = oldcombi
            mapMaken(best.houses, filename, graphtitle, iteratie, hoogstewaarde)
            updateGraph(filename + "single", huidigeiteraties, iteratie, huidigewaarden, hoogstewaarde)
            updateGraph(filename, iteraties, iteratie, uitkomsten, hoogstewaarde)
        index = int(combinatie.evaluatie[criterium] / waardeperbakje)
        bakjes[index] += 1
        if update == True:
            createBarChart(determineRange(bakjes), waardeperbakje, filename, graphtitle, criterium, iteratie)
