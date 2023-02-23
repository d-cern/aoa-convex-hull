import os
from Point import Point
from Line import Line

# !!!! must return the INDICES (as they are in the input file) of the convex hull points !!!! #
# TODO: change return values to indices
def ComputeConvexHull(points):
    # base cases: len(points) == 2 or 3
    if len(points) == 2:
        return points
    elif len(points) == 3:
        if points[3].IsAboveLine( Line(points[0], points[1])):
            return points
        


# finding lower tangent
#     # a = rightmost point of A
#     # b = leftmost point of B
#     #
#     # while(T=ab is not lower tangent to both convex hulls):
#     #     while(T is not lower tangent to A):
#     #         a = a - 1
#     #
#     #     while(T is not lower tangent to B):
#     #         b = b + 1
#     # rightmost of pointsA
#     aRight = pointsA[len(pointsA) - 1]
#     bLeft = pointsB[0]
#     T = Line(aRight, bLeft)


inputFileDir = '../data/input.csv'

# error check file path
if not os.path.exists(inputFileDir):
    print('Cannot find ' + inputFileDir + '.')
    quit()

# open input file
file = open(inputFileDir, 'r')

points = []

# read each line of the input file and store fields in respective attribute of Point
line = file.readline()
while line:
    coordinates = line.split(',')
    points.append(Point( float(coordinates[0]), float(coordinates[1]) ))
    line = file.readline()

file.close()

# split points list in half
# TODO: split should occur inside ComputeConvexHull()
# pointsA = points[ len(points) // 2: ]
# pointsB = points[ :len(points) // 2 ]

# compute convex hull points
# convexHullPoints = ComputeConvexHull(pointsA, pointsB)

# # debugging: print all points
# for i in points:
#     print(f'{i.x} {i.y}')
#
# # print function of line between two points
# z = Line(points[0], points[34])
