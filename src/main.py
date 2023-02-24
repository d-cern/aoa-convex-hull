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

    # copy a/b_cvx_hull
    cpy_a_cvx_hull = a_cvx_hull
    cpy_b_cvx_hull = b_cvx_hull

    # combine
    # -------------------
    # rightmost point of a_cvx_hull
    a_len = len(a_cvx_hull)
    a_lower_right = a_len - 1
    # side_a[a_lower_right]

    # leftmost point of b_cvx_hull
    b_len = len(b_cvx_hull)
    b_lower_left = 0

    line_T = Line(a_cvx_hull[a_lower_right], b_cvx_hull[b_lower_left])

    # lower tangent
    while not line_T.is_lower_tangent2(a_cvx_hull, b_cvx_hull):
        while not line_T.is_lower_tangent(a_cvx_hull):
            a_lower_right -= 1        # step in clockwise direction
            line_T = Line(a_cvx_hull[a_lower_right], b_cvx_hull[b_lower_left])

            # loop around to end of the end list (avoid out of bounds error)
            if a_lower_right == 0:
                a_lower_right = a_len - 1

        while not line_T.is_lower_tangent(b_cvx_hull):
            b_lower_left += 1         # step in counter-clockwise direction
            line_T = Line(a_cvx_hull[a_lower_right], b_cvx_hull[b_lower_left])
            if b_lower_left == b_len:
                b_lower_left = 0


    # upper tangent     # TODO: finish compute upper tan
    a_upper_right = len(a_cvx_hull) - 1     # rightmost point of a_cvx_hull
    b_upper_left = 0      # leftmost point of b_cvx_hull

    line_T = Line(a_cvx_hull[a_upper_right], b_cvx_hull[b_upper_left])

    while not line_T.is_upper_tangent2(a_cvx_hull, b_cvx_hull):
        while not line_T.is_upper_tangent(a_cvx_hull):
            a_upper_right += 1        # step in counter-clockwise direction
            line_T = Line(a_cvx_hull[a_upper_right], b_cvx_hull[b_upper_left])
            if a_upper_right == a_len:
                a_upper_right = 0

        while not line_T.is_upper_tangent(b_cvx_hull):
            b_upper_left -= 1         # step in clockwise direction
            line_T = Line(a_cvx_hull[a_upper_right], b_cvx_hull[b_upper_left])
            if b_upper_left == 0:
                b_upper_left = b_len



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
