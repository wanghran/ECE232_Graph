import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 11.0, 1.0)
y = np.arange(0.0, 11.0, 1.0)
X, Y = np.meshgrid(x, y)
z = np.zeros([11, 11])
z[9, 9] = 1.0
fig, ax = plt.subplots()
map = ax.pcolor(X, Y, z, cmap='seismic', vmax=z.max(), vmin=z.min())
ax.invert_yaxis()
ax.xaxis.tick_top()
fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(map, cax=cbar_ax)
ax.set_title('Heap map for reward function 1', y=1.08)
plt.show()
