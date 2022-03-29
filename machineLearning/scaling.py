import pandas
import numpy
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("cars2.csv")

X = df[['Weight', 'Volume']]
y = df["CO2"]

# standard scaling (z = (x - u) / s)
# 'z' is the new value, 'x' is the original value, 'u' is the mean and 's' is the standard deviation.

# weightMean = numpy.mean(df["Weight"])
# weightStd = numpy.std(df["Weight"])
# scaledWeightValue = (df["Weight"] - weightMean) / weightStd
# print(scaledWeightValue)
scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)
