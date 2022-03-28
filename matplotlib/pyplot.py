import matplotlib.pyplot as plt
import numpy as np


xPoints = np.array([0, 6])
yPoints = np.array([0, 250])
plt.plot(xPoints, yPoints, 'H:r')


# *(point markers) --(line style) b(line colour) ms(marker size) mec(marker outline colour)
# mfc(marker inside colour) lw(line width)
yPoints = np.array([21, 59, 31, 96, 22, 160, 25])
plt.plot(yPoints, '*--b', ms=15, mec='r', mfc='y', lw=5)


yPoints = np.array([145, 153, 184, 12, 175, 132, 167])
plt.plot(yPoints, 'D-.y')

titleDict = {'font': 'serif', 'color': 'red', 'size': '15'}
labelDict = {'font': 'serif', 'color': 'blue', 'size': '10'}

plt.title("Some bullshit", fontdict=titleDict)
plt.ylabel("Height", fontdict=labelDict)
plt.xlabel("Width", fontdict=labelDict)

plt.grid(axis='y', ls='--', lw=1)
plt.show()
