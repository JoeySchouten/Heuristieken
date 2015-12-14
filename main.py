#TODO: Alle grafieken e.d. goed krijgen voor alle algoritmes
#       Alles moet lijn-grafiek + bar-chart krijgen.
#       Alleen nog sim.annealing
#TODO: uitvogelen waarden sim. annealing etc.
#TODO: sim.annealing opnieuw draaien indien temp. onder bepaalde waarde
#TODO: sim.anneal. swappen bouwen
#       zie sim. anneal schuiven
#TODO: sim.anneal. schuiven+swappen bouwen
#       zie sim. anneal. schuiven
#TODO: Alles Runnen:
#       (Vraag desnoods familie/vrienden of zij het programma kunnen draaien een nachtje)
#       (Indien nodig kan ik wel een handleiding maken)
#           Randsample vrijstand:                   40(nu bezig)
#           Randsample waarde:                                      60(Jordi)
#           Schuiven vrijstand:                     40(Joey)        60(Jordi?)
#           Schuiven waarde:                        40              60(Jordi?)
#           Swappen vrijstand:      20              40              60
#           Swappen waarde:         20              40              60
#           Schuiven+Swappen vrijstand: 20, 40, 60
#           Schuiven+Swappen waarde: 20, 40, 60
#           Alles behalve Random Simulated annealing
#TODO: Analyseren data voor verslag + presentatie
#TODO: Beste methode (kaart+grafiek) selecteren per categorie (aantalhuizen + criterium)
#       Vrijstand:  20
#                   40
#                   60
#       Waarde:     20
#                   40
#                   60
#TODO: Presentatie
#TODO: Verslag
#TODO: Opschonen code
#       Code is mix v. Nederlands en Engels; pick one? Of is dat onnodig?

import csv
import sys
import random
import matplotlib.pyplot as plt
import math
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

# toegestane opties command line arguments
toegestanehuizen = [20,40,60]
toegestanemethoden = ["randsample", "schuiven", "swappen", "annealingschuiven", "schuifswap" ]
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
begintemperatuur = 1000
gestoldbij = 20

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
#plt.ion()
#plt.show()

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
        if iteratie%2500 == 0:
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

elif str(sys.argv[2]) == "schuifswap":
    plt.title('Amstelhaege Schuif-Swap-Hillclimber')
    combinatie = createRandom()
    # ga swappen
    while True:
        update = False
        gelukt = False
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

        # 20% swappen, 80% schuiven
        kans = random.randint(0,10)
        if kans < 8:
            if schuiven(combinatie) == True:
                gelukt = True
        else:
            if swappen(combinatie) == True:
                gelukt = True

        if gelukt == True:
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
        if iteratie%500 == 0 and best != 0:
            createBarChart(determineRange(bakjes), waardeperbakje, filename, graphtitle, criterium, iteratie)
            updateGraph(filename, iteraties, iteratie, uitkomsten, hoogstewaarde)
        iteratie += 1

elif str(sys.argv[2]) == "annealingschuiven":
    plt.title('Amstelhaege Simulated Annealing Schuiven')
    combinatie = createRandom()
    while True:
        iteratie += 1
        oldcombi = combinatie
        if schuiven(combinatie) == True:
            combinatie.evalueer()
            temp = combinatie.evaluatie
            verbetering = temp[criterium] - hoogstewaarde
            if verbetering < 0:
                temperatuur = begintemperatuur/iteratie
                kans = math.e**(verbetering/temperatuur)*100
                if random.random()*100 < kans:
                    # bewaar nieuwe combinatie
                    pass
                else:
                    # houd oude combi
                    combinatie = oldcombi
                    combinatie.evalueer()
                    temp = combinatie.evaluatie
            hoogstewaarde = temp[criterium]
        uitkomsten.append(hoogstewaarde)
        iteraties.append(iteratie)
        if temperatuur < gestoldbij:
            mapMaken(best.houses, filename, graphtitle, iteratie, hoogstewaarde)
            updateGraph(filename, iteraties, iteratie, uitkomsten, hoogstewaarde)
            sys.exit()
