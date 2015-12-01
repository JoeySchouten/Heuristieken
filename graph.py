
def mapMaken():
	import matplotlib.pyplot as plt
	import matplotlib.patches as patches

	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111, aspect='equal')
	plt.axis([0, 320, 0, 300])
	plt.axis('off')
	ax1.add_patch(patches.Rectangle((0, 0), 320, 300, facecolor="lightgreen", edgecolor="none"))
	ax1.add_patch(patches.Rectangle((200, 220), 16, 16, facecolor="gray", edgecolor="none"))
	ax1.add_patch(patches.Rectangle((100, 120), 15, 20, facecolor="brown", edgecolor="none"))
	ax1.add_patch(patches.Rectangle((10, 12), 22, 21, facecolor="black", edgecolor="none"))
	ax1.add_patch(patches.Rectangle((10, 120), 80, 20, facecolor="lightblue", edgecolor="none"))
	fig1.savefig('rect1.png', dpi=300, bbox_inches='tight')

def graphMaken():
	#TODO