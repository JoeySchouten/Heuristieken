import csv
from combination import Combination
import random

# create object containing "dumb solution"
dumbsol = Combination(60, 1)
dumbsol.placeAll()
dumbsol.printToCSV()
#print dumbsol.map.data
