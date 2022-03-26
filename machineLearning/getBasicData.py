from turtle import numinput
import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

meanSpeed = numpy.mean(speed)
print(meanSpeed)

medianSpeed = numpy.median(speed)
print(medianSpeed)

modeSpeed = stats.mode(speed)
print(modeSpeed)

stdSpeed = numpy.std(speed) # std(σ) - standart deviation == √var
print(stdSpeed)

varSpeed = numpy.var(speed)# var(σ^2) - variance = std^2
print(varSpeed)

percSpeed = numpy.percentile(speed, 70) # Answer is 90.4 -- 70% of the people drive below 90.4 speed
print(percSpeed)