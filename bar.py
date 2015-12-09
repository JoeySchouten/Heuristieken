import numpy as np
import matplotlib.pyplot as plt

N = 4
eindWaardes = (20000000, 350000000, 30000000, 350000000)
extraLabel= 1

ind = np.arange(N) 
width = 1      

fig, ax = plt.subplots()
rects1 = ax.bar(ind, eindWaardes, width, color='c', yerr=extraLabel)


ax.set_ylabel('Waarde in Euro\'s')
ax.set_title('Hoogste huidige waarde voor alle algoritmes')
ax.set_xticks(ind + 0.5)
ax.set_xticklabels(('Randsample', 'Schuiven', 'Swappen', 'Annealing'))

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
plt.savefig('barchar.png', dpi=300, bbox_inches='tight')
plt.show()
