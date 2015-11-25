

def checkVrijstand(huis1, huis2):
	vrijstand = 0
	isLeft = False
	isRight = False
	isAbove = False
	isBelow = False
	# bereken hoekpunten van huis 1
	huis1xmin = huis1.hoekpunt.x
	huis1xmax = huis1.hoekpunt.x + huis1.width
	huis1ymin = huis1.hoekpunt.y
	huis1ymax = huis1.hoekpunt.y + huis1.length
	# bereken hoekpunten van huis 2
	huis2xmin = huis2.hoekpunt.x
	huis2xmax = huis2.hoekpunt.x + huis2.width
	huis2ymin = huis2.hoekpunt.y
	huis2ymax = huis2.hoekpunt.y + huis2.length
	# controleer of hoekpunten huis 2 binnen bereik huis 1 vallen
	if (huis2xmin > huis1xmin and huis2xmin < huis1xmax) or (huis2xmax > huis1xmin and huis2xmax < huis1xmax):
		if (huis2ymin > huis1ymin and huis2ymin < huis1ymax) or (huis2ymax > huis1ymin and huis2ymax < huis1ymax):
			# error
			return 0
	# als dat niet zo is: ga door
	# vergelijk x waarden van beide huizen
	# als x huis 1 groter is dan x huis 2:
	if huis1xmin > huis2xmin:
		# huis 2 staat links
		isLeft = True
	if huis1xmax < huis2xmin:
		isRight = True
	# vergelijk y waarden van beide huizen
	# als y huis 1 groter is dan y huis 2:
	if huis1ymin > huis2ymin:
		# huis 2 staat boven
		isAbove = True
	if huis1ymax < huis2ymin:
		isBelow = True
	# bereken vrijstand
	if isAbove == True:
		if isLeft == True:
			x = huis1xmin - huis2xmax
			y = huis1ymin - huis2ymax
			vrijstand = (x**2 + y**2)**0.5
		elif isRight == True:
			x = huis2xmin - huis1xmax
			y = huis1ymin - huis2ymax
			vrijstand = (x**2 + y**2)**0.5
		else:
			vrijstand = huis1ymin - huis2ymax
	elif isBelow == True:
		if isLeft == True:
			x = huis1xmin - huis2xmax
			y = huis2ymin - huis1ymax
			vrijstand = (x**2 + y**2)**0.5
		elif isRight == True:
			x = huis2xmin - huis1xmax
			y = huis2ymin - huis1ymax
			vrijstand = (x**2 + y**2)**0.5
		else:
			vrijstand = huis2ymin - huis1ymax
	else:
		if isLeft == True:
			vrijstand = huis1xmin - huis2xmax
		elif isRight == True:
			vrijstand = huis2xmin - huis1xmax
		else:
			pass
	return vrijstand
