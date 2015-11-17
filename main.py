import csv
from combination import Combination

# create object containing "dumb solution"
dumbsol = Combination(20)
dumbsol.createHouseList(20)
dumbsol.map.initializeMap()
dumbsol.placeAll()
dumbsol.printToCSV()
