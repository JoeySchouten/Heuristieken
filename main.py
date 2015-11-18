import csv
from combination import Combination
import random

# berekening voor de min/max lengtes van het water (gaan nu even uit van 1 lichaam)
watersizes = []
minwater = 4800
inrange = False
rangemin = 0
rangemax = 0
for i in range(1,200):
    current = minwater/i
    ratio = current/i
    if inrange == False:
        if ratio >= 1 and ratio <=4:
            rangemin = i
            inrange = True
    else:
        if ratio < 1 or ratio > 4:
            rangemax = i-1
            break
# code om water willekeurig te sizen (even hardcoded voor 20); moet een losse functie worden waar ook meerdere eenheden werken
# geeft 2-dimensionale array terug
waterlength = random.randint(rangemin,rangemax)
waterwidth = minwater/waterlength
watersizes[0][0]=waterlength
watersizes[0][1]=waterwidth

# create object containing "dumb solution"
dumbsol = Combination(20)
dumbsol.houses[21].setSize(watersizes[0][0],watersizes[0][1])
dumbsol.placeAll()
dumbsol.printToCSV()
