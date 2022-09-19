import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from math import pi

L =12
delta = 0.35

X,Y,W,U = np.loadtxt('PlotData_'+str(delta)+'.txt', delimiter = '\t', unpack=True)
index = X.tolist() # index
eigenvalue = Y.tolist() # eigenvalue
entropy = W.tolist() # entropy
seom = U.tolist() # SEOM


large = 80; med = 50; small = 30
params = {'axes.titlesize': large,
          'axes.titlepad' : large,
          'legend.fontsize': med,
          #'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)


f = plt.figure()
f.set_figwidth(40)
f.set_figheight(25)

plt.scatter(index, entropy, c=eigenvalue, cmap='magma', s=400,edgecolor ="k", label = '')
plt.errorbar(index, entropy, yerr = seom,fmt='k',markersize='1',capsize=3, elinewidth=0.6)
plt.colorbar(orientation="vertical").set_label(
        label='Colorbar : Eigenvalues',size=40,weight='bold',labelpad=20)
plt.xlim([-30, 4150])
plt.ylim([0, 3.66])
plt.grid(linestyle='--', alpha=0.5)

'''
Axes tick size and color.

'''
ax = f.gca()
ax.tick_params(axis="x", direction="inout", length=30, width=4, color="k")
ax.tick_params(axis="y", direction="inout", length=30, width=4, color="k")

''' 

Add axes label to the top and the right.

'''
#ax.tick_params(bottom=True, top=True, left=True, right=True)
#ax.tick_params(labelbottom=True, labeltop=True, labelleft=True, labelright=True)


plt.xlabel("Index of eigenvalues",weight='bold', labelpad=60)
plt.ylabel("Entropy",weight='bold',labelpad=60)
plt.title("L="+str(L)+", Page value = "+str(np.around( (L/2)*np.log(2)-0.5,4))+
        ", $\delta$ ="+str(delta)+", cmap = energy,# Noise = 16")

#plt.yticks([-pi, -pi/2, -3*pi/4, -pi/4, 0, pi/4, 3*pi/4, pi/2, pi],
           #['$-\pi$', r'$-\pi/2$', r'$-3\pi/4$', r'$-\pi/4$', r'$0$', r'$\pi/4$', r'$3\pi/4$',
            #r'$\pi/2$', '$\pi$' ])

'''

Plot horizontal lines.

'''
#plt.axhline(y=3.11034138188, color='k', linestyle='-',linewidth = 2)
#plt.axhline(y=-3.11034138188, color='k', linestyle='-',linewidth = 2)
#plt.axhline(y=0, color='k', linestyle='-',linewidth = 2)


plt.savefig('entropy_index_'+str(delta)+'.png', dpi=100, bbox_inches='tight')