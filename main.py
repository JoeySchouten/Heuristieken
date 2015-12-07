import csv
from combination import Combination
import random
from graph import *
import matplotlib.pyplot as plt

aantalhuizen = 60
aantalwater = 4
maxcombinaties = 20
plotymin = 22000000
plotymax = 30000000

uitkomsten = []
hoogstewaarde = 0
iteratie = 0
best = 0


while iteratie < maxcombinaties:
    error = False
    combinatie = Combination(aantalhuizen, aantalwater)
    #combinatie.placeAll()
    for i in range(len(combinatie.houses)):
        if combinatie.placeRandom(combinatie.houses[i], i) != True:
            error = True
    if error == False:
        combinatie.evalueer()
        temp = combinatie.evaluatie
        if temp[1] > hoogstewaarde:
            hoogstewaarde = temp[1]
            best = combinatie
    uitkomsten.append(hoogstewaarde)
    if iteratie == 0:
        combinatie.evalueer()
        temp = combinatie.evaluatie
        if temp[1] > hoogstewaarde:
            hoogstewaarde = temp[1]
            best = combinatie
        plt.xlabel('Iteraties')
        plt.ylabel('Waarde in Euro\'s')
        plt.title('Amstelhaege Random Sampling')
        plt.axis((0,maxcombinaties,plotymin,plotymax))  
        plt.ion()
        plotymin = hoogstewaarde
        plt.show()
    iteratie += 1
    plt.plot(iteratie, hoogstewaarde, '.-r')
    plt.draw()
    plt.show()
    plt.savefig('graph.png', dpi=300, bbox_inches='tight')

mapMaken(best.houses)
best.evalueer()
best.printToCSV()
