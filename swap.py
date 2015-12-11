from combination import Combination
import random
from vrijstand import checkVrijstand

# function to swap a house
def swappen(combinatie):
    random.shuffle(combinatie.houses)
    huis1 = combinatie.houses[0]
    huis2 = combinatie.houses[1]
    while huis1.type == huis2.type or huis1.type == "Water" or huis2.type == "Water":
        random.shuffle(combinatie.houses)
        huis1 = combinatie.houses[0]
        huis2 = combinatie.houses[1]
    xH1 = huis1.hoekpunt.x
    yH1 = huis1.hoekpunt.y
    xH2 = huis2.hoekpunt.x
    yH2 = huis2.hoekpunt.y

    swap(huis1, huis2)
    mogelijk = True

    if xH1 - huis1.minVrij < 0 or xH1 + huis1.width + huis1.minVrij > combinatie.map.width:
        mogelijk = False
    elif yH1 - huis1.minVrij < 0 or yH1 + huis1.length + huis1.minVrij > combinatie.map.length:
        mogelijk = False
    elif xH2 - huis2.minVrij < 0 or xH2 + huis2.width + huis2.minVrij > combinatie.map.width:
        mogelijk = False
    elif yH2 - huis2.minVrij < 0 or yH2 + huis2.length + huis2.minVrij > combinatie.map.length:
        mogelijk = False

    if mogelijk == True:
        for i in range(2, len(combinatie.houses)):
            if checkVrijstand(huis1, combinatie.houses[i]) < huis1.minVrij:
                mogelijk = False
            elif checkVrijstand(huis2, combinatie.houses[i]) < huis2.minVrij:
                mogelijk = False

    if mogelijk != True:
        swap(huis1, huis2)
        return False
    return True

def swap(huis1, huis2):
    xH1 = huis1.hoekpunt.x
    yH1 = huis1.hoekpunt.y
    xH2 = huis2.hoekpunt.x
    yH2 = huis2.hoekpunt.y
    # swap x coordinates
    tempx = xH1
    xH1 = xH2
    xH2 = tempx
    # swap y coordinates
    tempy = yH1
    yH1 = yH2
    yH2 = tempy
    # set new coordinates
    huis1.hoekpunt.setPoint(xH1, yH1)
    huis2.hoekpunt.setPoint(xH2, yH2)
