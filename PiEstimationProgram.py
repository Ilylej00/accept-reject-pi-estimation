import math
from numpy import random
#initialize counter for accepted points
count = 0
#create an array of 1000 2D points
points = random.uniform(size = (1000,2))
#iterate through all the points
for point in points:
    #calculate the distance from each point to center of circle
    dist = math.sqrt(pow(point[0]-.5,2) + pow(point[1]-.5,2))
    #check if distance is less than radius of circle and accept point if so
    if (dist < .5):
        count = count + 1;

#print the estimated pi val given the accepted and rejected point ratio
print(4*(count/1000))
