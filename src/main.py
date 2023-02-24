import os
from point import Point
from line import Line


def compute_convex_hull(points):
    # base cases
    # -------------------
    if len(points) == 2:
        return points
    elif len(points) == 3:
        if points[2].is_above_line( Line(points[0], points[1])):
            return points
        else:
            return [0, 2, 1]

    # divide
    # -------------------
    a_cvx_hull = compute_convex_hull( points[len(points) // 2:] )
    b_cvx_hull = compute_convex_hull( points[:len(points) // 2] )

    # combine
    # -------------------
    # rightmost point of a_cvx_hull
    a_right = len(a_cvx_hull) - 1
    # leftmost point of b_cvx_hull
    b_left = 0

    line_T = Line(a_right, b_left)

    # lower tangent
    while not line_T.is_lower_tangent2(a_cvx_hull, b_cvx_hull):
        while not line_T.is_lower_tangent(a_cvx_hull):
            a_right -= 1        # step in clockwise direction

        while not line_T.is_lower_tangent(b_cvx_hull):
            b_left += 1         # step in counter-clockwise direction

    # upper tangent     # TODO: finish compute uppertan
    # rightmost point of a_cvx_hull
    a_right = len(a_cvx_hull) - 1
    # leftmost point of b_cvx_hull
    b_left = 0


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
#     # rightmost of a_points


def main():

    INPUT_FILE_DIR = '../data/input.csv'

    # error check file path
    if not os.path.exists(INPUT_FILE_DIR):
        print('Cannot find ' + INPUT_FILE_DIR + '.')
        quit()

    # open input file
    file = open(INPUT_FILE_DIR, 'r')

    points = []
    i = 0

    # read each line of the input file and store fields in respective attribute of Point
    line = file.readline()
    while line:
        coordinates = line.split(',')
        points.append(Point( float(coordinates[0]), float(coordinates[1]), int(++i) ))
        line = file.readline()

    file.close()

    # compute convex hull points
    # convexHullPoints = ComputeConvexHull(a_points, b_points)

    # debugging: print all points
    for i in points:
        print(f'{i.x} {i.y}')
    #
    # # print function of line between two points
    # z = Line(points[0], points[34])


main()
