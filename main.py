import csv
from combination import Combination
import random
from vrijstand import checkVrijstand

hoogstewaarde = 0
iteratie = 0
maxcombinaties = 10
uitkomsten = []
# create object containing "dumb solution"
while iteratie < maxcombinaties:
    error = False
    combinatie = Combination(20, 4)
    combinatie.placeAll()
    for i in range(len(combinatie.houses)):
        if combinatie.placeRandom(combinatie.houses[i], i) != True:
            error = True
    if error == False:
        combinatie.evalueer()
        temp = combinatie.evaluatie
        if temp[1] > hoogstewaarde:
            hoogstewaarde = temp[1]
    uitkomsten.append(hoogstewaarde)
    iteratie += 1
