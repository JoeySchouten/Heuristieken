#Kijken of een huis (eengezins, bungalow, villa) genoeg vrijstand heeft
	pak coordinaat van huis (x, y) op in de "kaart"
	ga -1 op de y-as
	check de gehele x-as op vrijstand, + 1 meter extra voorbij het huis
	ga vervolgens naar beneden
	pak de lengte van het huis + 1
	ga terug over de x-as
	ga weer +1 verder dan de oorspronkelijke len van het huis
	ga weer omhoog via de y-as
	ga +1 verder dan vorige ronde
	doe dit zolang er geen huizen geraakt worden
	sla de vrijstand op in een variabele, trek daar de min vrijstaande waarde bij af

def totaleVrijstand:
	#coordinates in x,y format
    crawler = Eerste huis op eerste locatie
    # loop to place houses
	for i in range(len(self.houses)):
    	#blijven loopen door huizen