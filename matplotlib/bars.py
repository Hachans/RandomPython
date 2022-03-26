import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.random.randint(20, size=(4))

plt.bar(x,y, color='red', width=0.5)
# plt.barh(x,y, color='blue', height=0.5)

plt.show()