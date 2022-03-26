import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints, 'H:r')


# *(point markers) --(line style) b(line colour) ms(marker size) mec(marker outline colour)
# mfc(marker inside colour) lw(line width)
ypoints = np.array([21,59,31,96,22,160,25])
plt.plot(ypoints, '*--b', ms=15, mec='r', mfc='y', lw=5)


ypoints = np.array([145,153,184,12,175,132,167])
plt.plot(ypoints, 'D-.y')

titleDict = {'font':'serif', 'color':'red', 'size':'15'}
labelDict = {'font':'serif', 'color':'blue', 'size':'10'}

plt.title("Some bullshit", fontdict=titleDict)
plt.ylabel("Heightyeryeryeryreyeryeryeryeyeryeyeryeyeryeryeyey", fontdict=labelDict)
plt.xlabel("Width", fontdict=labelDict)

plt.grid(axis = 'y', ls = '--', lw=1)
plt.show()
