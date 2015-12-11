import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def updateGraph(filename, iteraties, iteratie, uitkomsten, hoogstewaarde):
	plt.figure(1)
	plt.plot(iteraties, uitkomsten, '-', color='steelblue')
	plt.suptitle("Hoogste huidige waarde: " + str(hoogstewaarde) + " Huidige iteratie: " + str(iteratie), fontsize=13)
	plt.draw()
	plt.savefig(filename + 'graph.png', dpi=300, bbox_inches='tight')
	plt.close(1)
	print "Grafiek bijgewerkt tot iteratie " + str(iteratie) + ". Hoogste Waarde: " + str(hoogstewaarde)

def mapMaken(huizen, filename, graphtitle, iteratie, hoogstewaarde):
	fig1 = plt.figure(2)
	ax1 = fig1.add_subplot(111, aspect='equal')
	plt.suptitle(graphtitle, fontsize=13)
	ax1.set_title("Uitkomst: " + str(hoogstewaarde) + " Iteratie: " + str(iteratie))
	plt.axis([0, 320, 0, 300])
	plt.axis('off')
	print "Kaart gemaakt!"

	# Shrink current axis by 20%
	box = ax1.get_position()
	ax1.set_position([box.x0, box.y0, box.width * 0.8, box.height])
	grey_patch = patches.Patch(color='gray', label='Eensgezinswoning')
	brown_patch = patches.Patch(color='brown', label='Bungalow')
	black_patch = patches.Patch(color='black', label='Villa')
	blue_patch = patches.Patch(color='dodgerblue', label='Water')
	# Put a legend to the right of the current axis
	ax1.legend(handles=[grey_patch, brown_patch, black_patch, blue_patch], loc='center left', bbox_to_anchor=(1, 0.5))

	ax1.add_patch(patches.Rectangle((0, 0), 320, 300, facecolor="palegreen", edgecolor="none"))

	for i in range(len(huizen)):
		if huizen[i].type == "Eengezins":
			ax1.add_patch(patches.Rectangle((huizen[i].hoekpunt.x, huizen[i].hoekpunt.y), huizen[i].width, huizen[i].length, facecolor="gray", edgecolor="none"))
		elif huizen[i].type == "Bungalow":
			ax1.add_patch(patches.Rectangle((huizen[i].hoekpunt.x, huizen[i].hoekpunt.y), huizen[i].width, huizen[i].length, facecolor="brown", edgecolor="none"))
		elif huizen[i].type == "Villa":
			ax1.add_patch(patches.Rectangle((huizen[i].hoekpunt.x, huizen[i].hoekpunt.y), huizen[i].width, huizen[i].length, facecolor="black", edgecolor="none"))
		elif huizen[i].type == "Water":
			ax1.add_patch(patches.Rectangle((huizen[i].hoekpunt.x, huizen[i].hoekpunt.y), huizen[i].width, huizen[i].length, facecolor="dodgerblue", edgecolor="none"))

	fig1.savefig(filename + '.png', dpi=300, bbox_inches='tight')
	plt.close(2)

def determineRange(bakjes):
	# ga over array met bakjes
	linkergrens = None
	rechtergrens = None
	bereik = []
	for i in range(len(bakjes)):
		# de eerst die niet 0 is -> linkergrens
		if bakjes[i] != 0 and linkergrens == None:
			linkergrens = i
		# dan als het bakje 0 is, we een linkergrens hebben, maar nog geen rechtergrens
		elif bakjes[i] == 0 and linkergrens != None and rechtergrens == None:
			rechtergrens = i
		elif bakjes[i] != 0 and rechtergrens != None:
			rechtergrens = i
	n = 0
	for i in range(linkergrens, rechtergrens):
		bereik.append([i])
		bereik[n].append(bakjes[i])
		n += 1
	return bereik


def createBarChart(bereik, waardeperbakje, filename, graphtitle, criterium, iteratie):
	aantalbalken = len(bereik)
	eindWaardes = []
	labellijst = []
	for i in range(len(bereik)):
		eindWaardes.append(bereik[i][1])
		labellijst.append(str(bereik[i][0] * waardeperbakje))
	plt.figure()
	fig, ax = plt.subplots()
	extraLabel= 1
	ind = np.arange(aantalbalken)
	width = 1
	rects1 = ax.bar(ind, eindWaardes, width, color='steelblue', yerr=extraLabel)
	ax.set_ylabel('Aantal oplossingen in bereik')
	if criterium == 0:
		ax.set_xlabel('Totale Vrijstand')
	else:
		ax.set_xlabel('Waarde in Euro\'s')
	plt.suptitle(graphtitle + " - Iteraties: " + str(iteratie), fontsize=13)
	ax.set_title('Aantal oplossingen per bereik; elke balk = ' + str(waardeperbakje))
	ax.set_xticks(ind)
	ax.set_xticklabels(labellijst,rotation='vertical')
	autolabel(rects1, ax)
	plt.savefig(filename + 'barchart.png', dpi=300, bbox_inches='tight')
	plt.close()
	print "Barchart bijgewerkt tot iteratie " + str(iteratie)


def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')
