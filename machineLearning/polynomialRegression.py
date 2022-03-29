import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# for these data polynomial regression is fine to use
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]
myLine = numpy.linspace(1, 22, 100)

# for these data polynomial regression is useless
# x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
# y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
# myLine = numpy.linspace(1, 95, 100)

myModel = numpy.poly1d(numpy.polyfit(x, y, 3))

plt.scatter(x, y)
plt.plot(myLine, myModel(myLine))
plt.xlabel("Relationship (r) = {}".format(r2_score(y, myModel(x))))
plt.show()
