import csv
from combination import Combination
import random
from vrijstand import checkVrijstand

# create object containing "dumb solution"
dumbsol = Combination(20, 4)
dumbsol.placeAll()
dumbsol.evalueer()
dumbsol.printToCSV()
