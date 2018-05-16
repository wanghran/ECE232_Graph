import numpy as np
import matplotlib.pyplot as plt


def heat_map(value, name):
    x = np.arange(0.0, 11.0, 1.0)
    y = np.arange(0.0, 11.0, 1.0)
    X, Y = np.meshgrid(x, y)
    z = np.zeros([11, 11])
    s = value.shape
    for i in range(s[0]):
        for j in range(s[1]):
            z[i, j] = value[i, j]
    fig, ax = plt.subplots()
    map = ax.pcolor(X, Y, z, cmap='RdBu', vmax=z.max(), vmin=z.min())
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    fig.colorbar(map, cax=cbar_ax)
    ax.set_title(name, y=1.08)
    plt.show()

