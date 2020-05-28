import math
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

#emptyList for all pi estimations
numList = []

#how many random points are tested
testPoints = 2000
#how many attempts at pi desired
totalAttempts = 1000

for i in range(totalAttempts):
    #counter for points in circle
    count = 0
    #create an array of 2D points spread over a 1x1 square
    points = random.uniform(size = (testPoints,2))
    #iterate through all the points
    for point in points:
        #calculate the distance from each point to center of circle
        dist = math.sqrt(pow(point[0]-.5,2) + pow(point[1]-.5,2))
        #check if distance is less than radius of circle and accept point if so
        if (dist < .5):
            count = count + 1
    #add this estimation to our list
    numList.append(4*(count/testPoints))

#creates a distribution plot of our pi estimations
sns.distplot(numList, hist=False)
plt.show()
