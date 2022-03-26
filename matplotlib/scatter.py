# from turtle import color
import matplotlib.pyplot as plt
import numpy as np

# # day one, the age and speed of 13 cars:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y, color = 'red')

# # day two, the age and speed of 15 cars:

# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91])
# colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

# plt.scatter(x, y, c=colors)
# plt.title("Car age and speed corelation", size = 18)
# plt.xlabel("Car age", size = 15)
# plt.ylabel("Car speed", size = 15)


x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5, cmap='gist_rainbow')
plt.title("Random scatter with colormap", size = 17)
plt.colorbar()

plt.show()