import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 11.0, 1.0)
y = np.arange(0.0, 11.0, 1.0)
X, Y = np.meshgrid(x, y)
z = np.zeros([11, 11])
for i in range(1, 7):
    z[i, 4] = -100.0
z[9, 9] = 10.0
z[1, 5] = -100.0
z[1, 6] = -100.0
z[2, 6] = -100.0
z[3, 6] = -100.0
z[3, 7] = -100.0
z[3, 8] = -100.0
z[4, 8] = -100.0
z[5, 8] = -100.0
z[6, 8] = -100.0
z[7, 8] = -100.0
z[7, 7] = -100.0
z[7, 6] = -100.0
z[8, 6] = -100.0
fig, ax = plt.subplots()
map = ax.pcolor(X, Y, z, cmap='seismic', vmax=z.max(), vmin=z.min())
ax.invert_yaxis()
ax.xaxis.tick_top()
fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(map, cax=cbar_ax)
ax.set_title('Heap map for reward function 2', y=1.08)
plt.show()
