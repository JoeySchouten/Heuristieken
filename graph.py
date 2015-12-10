import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def updateGraph(filename, iteraties, iteratie, uitkomsten, hoogstewaarde):
	plt.figure(1)
	plt.plot(iteraties, uitkomsten, '-r')
	plt.suptitle("Hoogste huidige waarde: " + str(hoogstewaarde) + " Huidige iteratie: " + str(iteratie), fontsize=13)
	plt.draw()
	plt.savefig(filename + 'graph.png', dpi=300, bbox_inches='tight')

def mapMaken(huizen, filename):
	fig1 = plt.figure(2)
	ax1 = fig1.add_subplot(111, aspect='equal')
	plt.axis([0, 320, 0, 300])
	plt.axis('off')
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
		if bakjes[i] != 0 and linkergrens = None:
			linkergrens = i
		elif bakjes[i] == 0 and linkergrens != None:
			rechtergrens = i
		elif bakjes[i] != 0 and rechtergrens != None:
			rechtergrens = i
	n = 0
	for i in range(linkergrens, rechtergrens):
		bereik.append([i])
		bereik[n].append(bakjes[i])
		n += 1
	return bereik


def createBarChart(bereik, waardeperbakje, filename):
	aantalbalken = len(bereik)
	eindWaardes = []
	labellijst = []
	for i in range(len(bereik)):
		eindWaardes.append(bereik[i][1])
		labellijst.append(str(bereik[i][0] * waardeperbakje) + "-" + str((bereik[i][0] + 1)*waardeperbakje))
	extraLabel= 1
	ind = np.arange(aantalbalken)
	width = 1
	fig, ax = plt.subplots()
	rects1 = ax.bar(ind, eindWaardes, width, color='c', yerr=extraLabel)
	ax.set_ylabel('Waarde in Euro\'s')
	ax.set_title('Hoogste huidige waarde voor alle algoritmes')
	ax.set_xticks(ind + 0.5)
	ax.set_xticklabels(labellijst)

	autolabel(rects1)
	plt.savefig(filename + 'barchart.png', dpi=300, bbox_inches='tight')


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')
