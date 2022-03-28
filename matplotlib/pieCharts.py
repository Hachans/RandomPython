import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
myLabels = ["Apples", "Bananas", "Oranges", "Kiwis"]
myExplode = [0, 0.2, 0, 0]
myColors = ["Red", "Yellow", "Orange", "Green"]
plt.pie(y, labels=myLabels, colors=myColors, explode=myExplode, startangle=10, shadow=True)
plt.legend()
plt.legend(title="Fruits", loc="upper left")
plt.show()
