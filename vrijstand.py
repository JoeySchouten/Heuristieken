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

	Maak er 1 functie van die je over een object trekt; een for loop die over de array met huizen gaat is zo gebouwd en is wss beter buiten de functie te plaatsen.

def berekenVrijstand(self, house):
	crawler = house.hoekpunt.x, (house.hoekpunt.y - 1)
	spiraal = 0
	vrijstand = 0

	# variabele die aangeeft of er nog vrije ruimte is
	heeftRuimte = True
	while heeftRuimte == True:
		for j in range(house.width + spiraal):
			if self.map.data.get((crawler.x, crawler.y)) != None
				crawler.x += 1
			else:
				heeftRuimte = False
				break
		for k in range(house.length + spiraal):
			if heeftRuimte == False:
				break
			elif self.map.data.get((crawler.x, crawler.y)) != None:
				crawler.y += 1
			else:
				heeftRuimte = False
				break
		spiraal += 1
		for l in range(house.width + spiraal):
			if heeftRuimte == False:
				break
			elif self.map.data.get((crawler.x, crawler.y)) != None:
				crawler.x -= 1
			else:
				heeftRuimte = False
				break
		for m in range(house.length + spiraal):
			if heeftRuimte == False:
				break
			elif self.map.data.get((crawler.x, crawler.y)) != None
				crawler.y -= 1
			else:
				heeftRuimte = False
				break
		spiraal += 1
		vrijstand += 1
	return vrijstand - house.minVrij

def totaleVrijstand(self):
	for i in range(len(self.houses)):
		self.houses[i].extraVrij = berekenVrijstand(self.houses[i])
