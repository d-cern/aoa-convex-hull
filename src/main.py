import os
from Point import Point

def ComputeConvexHull(points):


def LowerTangent(a, b):
    # a = rightmost point of A
    # b = leftmost point of B
    #
    # while(T=ab is not lower tangent to both convex hulls):
    #     while(T is not lower tangent to A):
    #         a = a - 1
    #
    #     while(T is not lower tangent to B):
    #         b = b + 1



inputFileDir = '../data/input.csv'

# error check file path
if not os.path.exists(inputFileDir):
    print('Cannot find ' + inputFileDir + '.')
    quit()

# open input file
file = open(inputFileDir, 'r')

points = []

#Read each line of the input file.
#Storing the x-coordinates into x.
#Storing the y-coordinates into y.
line = file.readline()
while line:
    coordinates = line.split(',')
    points.append(Point(coordinates[0], coordinates[1]))
    line = file.readline()

file.close()


# for i in points:
#     print(i.x + ' ' + i.y)
