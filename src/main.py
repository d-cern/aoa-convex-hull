import os
from point import Point
from line import Line

# !!!! must return the INDICES (as they are in the input file) of the convex hull points !!!! #
# TODO: change return values to indices
def compute_convex_hull(points):
    # base cases: len(points) == 2 or 3
    if len(points) == 2:
        return points
    elif len(points) == 3:
        if points[3].is_above_line( Line(points[0], points[1])):
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
#     # rightmost of points_a
#     aRight = points_a[len(points_a) - 1]
#     bLeft = points_b[0]
#     T = Line(aRight, bLeft)

def main():

    input_file_dir = '../data/input.csv'

    # error check file path
    if not os.path.exists(input_file_dir):
        print('Cannot find ' + input_file_dir + '.')
        quit()

    # open input file
    file = open(input_file_dir, 'r')

    points = []
    i = 0

    # read each line of the input file and store fields in respective attribute of Point
    line = file.readline()
    while line:
        coordinates = line.split(',')
        points.append(Point( float(coordinates[0]), float(coordinates[1]), int(++i) ))
        line = file.readline()

    file.close()

    # split points list in half
    # TODO: split should occur inside ComputeConvexHull()
    # points_a = points[ len(points) // 2: ]
    # points_b = points[ :len(points) // 2 ]

    # compute convex hull points
    # convexHullPoints = ComputeConvexHull(points_a, points_b)

    # debugging: print all points
    for i in points:
        print(f'{i.x} {i.y}')
    #
    # # print function of line between two points
    # z = Line(points[0], points[34])


main()
