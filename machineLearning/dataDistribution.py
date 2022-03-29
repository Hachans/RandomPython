import numpy
import matplotlib.pyplot as plt

# # random float values from 0.0 to 5.0
# x = numpy.random.uniform(0.0, 5.0, 100000)
# plt.subplot(1,2,1)
# plt.hist(x, 100)

# # random float values with mean 5.0 and standard deviation 1.0
# x = numpy.random.normal(5.0, 1.0, 100000)
# plt.subplot(1,2,1)
# plt.hist(x, 100)


x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y)

plt.show()
