import csv
from combination import Combination
import random

# create object containing "dumb solution"
dumbsol = Combination(60, 4)
print int((dumbsol.map.width*dumbsol.map.length)*0.2)
#dumbsol.placeAll()
#dumbsol.printToCSV()
#print dumbsol.map.data
