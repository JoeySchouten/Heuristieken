import math

def checkVrijstand(huis1, huis2):
	# init variablen voor vrijstand en om in op te slaan waar huis2 zich
	# ten opzichte van huis1 bevindt
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
	# zo ja: error, huizen mogen niet overlappen.
	if (huis2xmin > huis1xmin and huis2xmin < huis1xmax) or (huis2xmax > huis1xmin and huis2xmax < huis1xmax):
		if (huis2ymin > huis1ymin and huis2ymin < huis1ymax) or (huis2ymax > huis1ymin and huis2ymax < huis1ymax):
			# error
			return 0

	# vergelijk x waarden van beide huizen
	if huis1xmin > huis2xmin:
		# huis 2 staat links
		isLeft = True
	if huis1xmax < huis2xmin:
		# huis 2 staat rechts
		isRight = True

	# vergelijk y waarden van beide huizen
	if huis1ymin > huis2ymin:
		# huis 2 staat boven
		isAbove = True
	if huis1ymax < huis2ymin:
		# huis 2 staat onder
		isBelow = True

	# bereken vrijstand
	# wanneer huis2 boven huis1 staat:
	if isAbove == True:
		# wanneer huis2 ook links van huis1 staat (i.e. linksboven)
		if isLeft == True:
			x = huis1xmin - huis2xmax
			y = huis1ymin - huis2ymax
			vrijstand = (x**2 + y**2)**0.5
		# wanneer huis2 ook rechts van huis1 staat (i.e. rechtsboven)
		elif isRight == True:
			x = huis2xmin - huis1xmax
			y = huis1ymin - huis2ymax
			vrijstand = (x**2 + y**2)**0.5
		# anders staat huis2 direct boven huis1
		else:
			vrijstand = huis1ymin - huis2ymax

	# wanneer huis2 onder huis1 staat
	elif isBelow == True:
		if isLeft == True:
			# wanneer huis2 ook links van huis1 staat (i.e. linksonder)
			x = huis1xmin - huis2xmax
			y = huis2ymin - huis1ymax
			vrijstand = (x**2 + y**2)**0.5
		# wanneer huis2 ook rechts van huis1 staat (i.e. rechtsonder)
		elif isRight == True:
			x = huis2xmin - huis1xmax
			y = huis2ymin - huis1ymax
			vrijstand = (x**2 + y**2)**0.5
		# anders staat huis2 direct onder huis1
		else:
			vrijstand = huis2ymin - huis1ymax
	# anders staat huis 2 direct links of rechts van huis 1
	else:
		if isLeft == True:
			# wanneer huis2 links van huis1 staat
			vrijstand = huis1xmin - huis2xmax
		elif isRight == True:
			# wanneer huis2 rechts van huis1 staat
			vrijstand = huis2xmin - huis1xmax
		else:
			pass
	# floor ivm pythagoras-stelling die floats teruggeeft
	return math.floor(vrijstand)
