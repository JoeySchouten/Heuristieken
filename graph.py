import matplotlib.pyplot as plt
import matplotlib.patches as patches

def mapMaken(huizen):
	fig1 = plt.figure()
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

	fig1.savefig('map.png', dpi=300, bbox_inches='tight')
