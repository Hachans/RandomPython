import matplotlib.pyplot as plt
import numpy as np

xPoints = np.array([0, 5])
yPoints = np.array([0, 40])
plt.subplot(1,2,1)
plt.title("Bizzly")
plt.plot(xPoints, yPoints, '*-.b', ms=10)


xPoints = np.array([1,2,3,4,5])
yPoints = np.array([34, 12, 39, 11, 22])
plt.subplot(1,2,2)
plt.title("Jizzly")
plt.plot(xPoints, yPoints, '*-.b', ms=10)

plt.suptitle("Life of \'Bizzly\' and \'Jizzly\'")


# xPoints = np.array([10, 50])
# yPoints = np.array([10, 50])
# plt.subplot(2,1,1)
# plt.plot(xPoints, yPoints, '*-.b', ms=10)


# xPoints = np.array([10, 50])
# yPoints = np.array([10, 50])
# plt.subplot(2,1,2)
# plt.plot(xPoints, yPoints, '*-.b', ms=10)

plt.show()