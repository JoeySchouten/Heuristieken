import csv
from combination import Combination
import random
from graph import *
import matplotlib.pyplot as plt
import sys

toegestanehuizen = [20,40,60]
toegestanemethoden = ["randsample", "schuiven", "swappen"]
aantalhuizen = int(sys.argv[1])
aantalwater = 4

uitkomsten = []
hoogstewaarde = 0
iteratie = 0
best = 0

#sys.argv[] -> 1: aantal huizen; 2:methode
if int(sys.argv[1]) not in toegestanehuizen:
    print "Incorrect aantal huizen opgegeven. Correct gebruik:"
    print "python main.py [aantal huizen (20, 40, of 60)] [methode (randsample, schuiven, swappen)]"
    sys.exit()
elif str(sys.argv[2]) not in toegestanemethoden:
    print "Incorrecte methode opgegeven. Correct gebruik:"
    print "python main.py [aantal huizen (20, 40, of 60)] [methode (randsample, schuiven, swappen)]"
    sys.exit()

# bouwen grafiek
plt.xlabel('Iteraties')
plt.ylabel('Waarde in Euro\'s')
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
            if temp[1] > hoogstewaarde:
                hoogstewaarde = temp[1]
                best = combinatie
                #mapMaken(best.houses)
                best.evalueer()
                best.printToCSV()
        uitkomsten.append(hoogstewaarde)
        plt.plot(iteratie, hoogstewaarde, '.-r')
        plt.draw()
        plt.savefig('graph.png', dpi=300, bbox_inches='tight')
        iteratie += 1

elif str(sys.argv[2]) == "schuiven":
    #schuifcode
    pass
elif str(sys.argv[2]) == "swappen":
    plt.title('Amstelhaege Swapping')
    while True:
        error = False
        combinatie = Combination(aantalhuizen, aantalwater)
        for i in range(len(combinatie.houses)):
            if combinatie.swapHouse(combinatie.houses[i], i) != True:
                error = True
        if error == False:
            combinatie.evalueer()
            temp = combinatie.evaluatie
            if temp[1] > hoogstewaarde:
                hoogstewaarde = temp[1]
                best = combinatie
                #mapMaken(best.houses)
                best.evalueer()
                best.printToCSV()
        uitkomsten.append(hoogstewaarde)
        plt.plot(iteratie, hoogstewaarde, '.-r')
        plt.draw()
        plt.savefig('graph.png', dpi=300, bbox_inches='tight')
        iteratie += 1
