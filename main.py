import csv
import sys
import random
import matplotlib.pyplot as plt
from combination import Combination
from graph import *
from schuiven import schuiven
from swap import swapHouse

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
            uitkomsten.append(hoogstewaarde)
            plt.plot(iteratie, hoogstewaarde, '.-r')
            plt.draw()
            plt.savefig('graph.png', dpi=300, bbox_inches='tight')
    return combinatie

def informWrongUsage():
    print "Incorrect aantal huizen opgegeven. Correct gebruik:"
    print "python main.py [aantal huizen] [methode] [score]"
    print "aantal huizen: 20, 40 of 60"
    print "methode: randsample, schuiven of swappen"
    print "score: waarde of vrijstand"
    sys.exit()

toegestanehuizen = [20,40,60]
toegestanemethoden = ["randsample", "schuiven", "swappen"]
toegestanescore = ["waarde", "vrijstand"]
aantalhuizen = int(sys.argv[1])
aantalwater = 4
uitkomsten = []
hoogstewaarde = 0
iteratie = 0
maxverwerpen = 100
verwerpen = 0
randommapper = 500
best = 0
# 0 = scoren op vrijstand; 1 = scoren op waarde in euro's
criterium = 0

#  afvangen hoeveelheid arguments!
if len(sys.argv) > 4:
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

# bouwen grafiek
graphcolour = 'r'
plt.figure(1)
plt.xlabel('Iteraties')
plt.ylabel('Waarde in Euro\'s')
plt.suptitle("Hoogste huidige waarde: " + str(hoogstewaarde) + " Huidige iteratie: " + str(iteratie), fontsize=13)
plt.ion()
plt.show()

if sys.argv[2] == "randsample":
    plt.title('Amstelhaege Random Sampling')
    while True:
        error = False
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
                if iteratie % randommapper == 0:
                    filename = str(sys.argv[1]) + str(sys.argv[2])
                    mapMaken(best.houses, filename)
        uitkomsten.append(hoogstewaarde)
        plt.figure(1)
        plt.plot(iteratie, hoogstewaarde, '.-r')
        plt.suptitle("Hoogste huidige waarde: " + str(hoogstewaarde) + " Huidige iteratie: " + str(iteratie), fontsize=13)
        plt.draw()
        plt.savefig('graph.png', dpi=300, bbox_inches='tight')
        iteratie += 1

elif str(sys.argv[2]) == "schuiven":
    plt.title('Amstelhaege Schuif-Hillclimber')
    combinatie = createRandom()
    # ga schuiven
    while True:
        if verwerpen > maxverwerpen:
            verwerpen = 0
            hoogstewaarde = 0
            if best != 0 and best.evaluatie[criterium] < combinatie.evaluatie[criterium]:
                best = combinatie
                filename = str(sys.argv[1]) + str(sys.argv[2])
                mapMaken(best.houses,filename)
            elif best == 0:
                best = combinatie
                filename = str(sys.argv[1]) + str(sys.argv[2])
                mapMaken(best.houses, filename)
            if graphcolour == 'r':
                graphcolour = 'b'
            else:
                graphcolour = 'r'
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
        plt.figure(1)
        plt.plot(iteratie, hoogstewaarde, '.-' + graphcolour)
        if best != 0 and best.evaluatie[criterium] > hoogstewaarde:
            plt.suptitle("Hoogste huidige waarde: " + str(best.evaluatie[criterium]) + " Huidige iteratie: " + str(iteratie), fontsize=13)
        else:
            plt.suptitle("Hoogste huidige waarde: " + str(hoogstewaarde) + " Huidige iteratie: " + str(iteratie), fontsize=13)
        plt.draw()
        plt.savefig('graph.png', dpi=300, bbox_inches='tight')
        iteratie += 1

elif str(sys.argv[2]) == "swappen":
    plt.title('Amstelhaege Swap-Hillclimber')
    combinatie = createRandom()
    # ga swappen
    while True:
        if verwerpen > maxverwerpen:
            verwerpen = 0
            hoogstewaarde = 0
            if best != 0 and best.evaluatie[criterium] < combinatie.evaluatie[criterium]:
                best = combinatie
                filename = str(sys.argv[1]) + str(sys.argv[2])
                mapMaken(best.houses,filename)
            elif best == 0:
                best = combinatie
                filename = str(sys.argv[1]) + str(sys.argv[2])
                mapMaken(best.houses, filename)
            if graphcolour == 'r':
                graphcolour = 'b'
            else:
                graphcolour = 'r'
            combinatie = createRandom()
        if swapHouse(combinatie) == True:
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
        plt.figure(1)
        plt.plot(iteratie, hoogstewaarde, '.-' + graphcolour)
        if best != 0 and best.evaluatie[criterium] > hoogstewaarde:
            plt.suptitle("Hoogste huidige waarde: " + str(best.evaluatie[criterium]) + " Huidige iteratie: " + str(iteratie), fontsize=13)
        else:
            plt.suptitle("Hoogste huidige waarde: " + str(hoogstewaarde) + " Huidige iteratie: " + str(iteratie), fontsize=13)
        plt.draw()
        plt.savefig('graph.png', dpi=300, bbox_inches='tight')
        iteratie += 1
