import numpy as np
import matplotlib.pyplot as plt

def p_map(value, name, policy_map):
    x = np.arange(0.0, 11.0, 1.0)
    y = np.arange(0.0, 11.0, 1.0)
    X, Y = np.meshgrid(x, y)
    z = np.zeros([11, 11])
    s = value.shape
    for i in range(s[0]):
        for j in range(s[1]):
            z[i, j] = value[i, j]
    fig, ax = plt.subplots()
    map = ax.pcolor(X, Y, z, cmap='seismic', vmax=z.max(), vmin=z.min())
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    fig.colorbar(map, cax=cbar_ax)
    ax.set_title(name, y=1.08)


    for i in range(s[0]):
        for j in range(s[1]):
            pos = i *10+ j

            if policy_map[pos] == 'right':
                ax.arrow(i+0.1,        #x start point
                        j+0.5,                      #y start point
                        0.8,       #change in x 
                        0,                      #change in y
                        head_width=0.4,         #arrow head width
                        head_length=0.1,        #arrow head length
                        width=0.06,              #arrow stem width
                        fc='yellow',             #arrow fill color
                        ec='yellow')
            elif policy_map[pos] == 'left':
                ax.arrow(i+1-0.1,        #x start point
                        j+0.5,                      #y start point
                        -0.8,       #change in x 
                        0,                      #change in y
                        head_width=0.4,         #arrow head width
                        head_length=0.1,        #arrow head length
                        width=0.06,              #arrow stem width
                        fc='yellow',             #arrow fill color
                        ec='yellow')
            elif policy_map[pos] == 'up':
                ax.arrow(i+0.5,        #x start point
                        j+1-0.1,                      #y start point
                        0,       #change in x 
                        -0.8,                      #change in y
                        head_width=0.4,         #arrow head width
                        head_length=0.1,        #arrow head length
                        width=0.06,              #arrow stem width
                        fc='yellow',             #arrow fill color
                        ec='yellow')
            else:
                ax.arrow(i+0.5,        #x start point
                        j+0.1,                      #y start point
                        0,       #change in x 
                        0.8,                      #change in y
                        head_width=0.4,         #arrow head width
                        head_length=0.1,        #arrow head length
                        width=0.06,              #arrow stem width
                        fc='yellow',             #arrow fill color
                        ec='yellow')                
    plt.show()
