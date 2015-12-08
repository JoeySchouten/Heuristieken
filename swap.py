import csv
from combination import Combination
import random
from graph import *
import matplotlib.pyplot as plt

# function to swap a house
def swap(combinatie):

    for n in range(1, len(combinatie.houses)):
        huis1 = combinatie.houses[n]
        xH1 = huis1.hoekpunt.x
        yH1 = huis1.hoekpunt.y

        huis2 = combinatie.houses[random.randint(1, len(combinatie.houses))]
        while huis1 == huis2:
            huis2 = combinatie.houses[random.randint(1, len(combinatie.houses))]
        xH2 = huis2.hoekpunt.x
        yH2 = huis2.hoekpunt.y

        mogelijk = True

        # check if house 1 has enough space
        for i in range (len(combinatie.houses)):
            if i == huis2:
                pass
            else:
                xiH1 = combinatie.houses[i].hoekpunt.x
                yiH1 = combinatie.houses[i].hoekpunt.y
                #check if H1 left and right corners are within iH1's x-range
                if (xH1 - huis1.minVrij <= xiH1 <= xH1 + huis1.width + huis1.minVrij) or (xH1 - huis1.minVrij <= xiH1 + combinatie.houses[i].width <= xH1 + huis1.width + huis1.minVrij):
                    #check if H1 top and bottom corners are within iH1's y-range
                    if (yH1 - huis1.minVrij <= yiH1 <= yH1 + huis1.length + huis1.minVrij) or (yH1 - huis1.minVrij <= yiH1 + combinatie.houses[i].length <= yH1 + huis1.length + huis1.minVrij):
                        mogelijk = False
                #check if iH1 left and right corners are within H1's x-range
                if (xiH1 - combinatie.houses[i].minVrij <= xH1 <= xiH1 + combinatie.houses[i].width + combinatie.houses[i].minVrij) or (xiH1 - combinatie.houses[i].minVrij <= xH1 + huis1.width <= xiH1 + combinatie.houses[i].width + combinatie.houses[i].minVrij):
                    #check if iH1 top and bottom corners are within H1's y-range
                    if (yiH1 - combinatie.houses[i].minVrij <= yH1 <= yiH1 + combinatie.houses[i].length + combinatie.houses[i].minVrij) or (yiH1 - combinatie.houses[i].minVrij <= yH1 + huis1.length <= yiH1 + combinatie.houses[i].length + combinatie.houses[i].minVrij):
                        mogelijk = False

        # check if house 2 has enough space
        for i in range (len(combinatie.houses)):
            if i == huis1:
                pass
            else:
                xiH2 = combinatie.houses[i].hoekpunt.x
                yiH2 = combinatie.houses[i].hoekpunt.y
                #check if H2 left and right corners are within iH2's x-range
                if (xH2 - huis2.minVrij <= xiH2 <= xH2 + huis2.width + huis2.minVrij) or (xH2 - huis2.minVrij <= xiH2 + combinatie.houses[i].width <= xH2 + huis2.width + huis2.minVrij):
                    #check if H2 top and bottom corners are within H1's y-range
                    if (yH2 - huis2.minVrij <= yiH2 <= yH2 + huis2.length + huis2.minVrij) or (yH2 - huis2.minVrij <= yiH2 + combinatie.houses[i].length <= yH2 + huis2.length + huis2.minVrij):
                        mogelijk = False
                #check if iH2 left and right corners are within H2's x-range
                if (xiH2 - combinatie.houses[i].minVrij <= xH2 <= xiH2 + combinatie.houses[i].width + combinatie.houses[i].minVrij) or (xiH2 - combinatie.houses[i].minVrij <= xH2 + huis2.width <= xiH2 + combinatie.houses[i].width + combinatie.houses[i].minVrij):
                    #check if H1 top and bottom corners are within H2's y-range
                    if (yiH2 - combinatie.houses[i].minVrij <= yH2 <= yiH2 + combinatie.houses[i].length + combinatie.houses[i].minVrij) or (yiH2 - combinatie.houses[i].minVrij <= yH2 + huis2.length <= yiH2 + combinatie.houses[i].length + combinatie.houses[i].minVrij):
                        mogelijk = False

        if mogelijk == True:
            # swap x coordinates
            tempx = xH1
            xH1 = xH2
            xH2 = tempx

            # swap y coordinates
            tempy = yH
            yH1 = yH2
            yH2 = tempy

            # set new coordinates
            huis1.hoekpunt.setPoint(xH1, yH1)
            huis2.hoekpunt.setPoint(xH2, yH2)
