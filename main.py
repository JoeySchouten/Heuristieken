import csv
from combination import Combination
import random

# create object containing "dumb solution"
dumbsol = Combination(20, 1)
dumbsol.placeAll()
dumbsol.printToCSV()
