import numpy as np
import matplotlib.pyplot as plt


def value_map(value, name):
    x = np.arange(0.0, 10.0, 1.0)
    y = np.arange(0.0, 10.0, 1.0)
    X, Y = np.meshgrid(x, y)
    z = np.zeros([10, 10])
    s = value.shape
    for i in range(s[0]):
        for j in range(s[1]):
            z[i, j] = value[i, j]
    fig, ax = plt.subplots()
    table = ax.table(cellText=z, loc='center')
    ax.axis('off')
    ax.axis('tight')
    fig.patch.set_visible(False)
    ax.set_title(name, y=1.0)
    table.auto_set_font_size(False)
    table.set_fontsize(6)
    table.scale(1.5, 2)
    plt.show()
