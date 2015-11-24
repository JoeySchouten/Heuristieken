import csv
from combination import Combination
import random

# create object containing "dumb solution"
dumbsol = Combination(12, 1)
dumbsol.placeAll()
dumbsol.printToCSV()
dumbsol.totaleVrijstand()
#print dumbsol.map.data
