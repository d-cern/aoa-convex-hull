import os
from point import Point
from line import Line


def compute_convex_hull(points):
    # base cases
    # -------------------
    if len(points) == 2:
        return points
    elif len(points) == 3:
        #print(f'points0 = {points[0].y_coord}')
        if points[2].is_above_line( Line(points[0], points[1])):
            return points
        else:
            return [points[0], points[2], points[1]]

    # divide
    # -------------------
    print(f'len = {len(points)}')
    a_cvx_hull = compute_convex_hull( points[len(points) // 2:] )
    b_cvx_hull = compute_convex_hull( points[:len(points) // 2] )

    # print(f'len = {len(a_cvx_hull)}')

    # copy a/b_cvx_hull
    cpy_a_cvx_hull = a_cvx_hull
    cpy_b_cvx_hull = b_cvx_hull

    # combine
    # -------------------
    not_lower_tangent = []

    # rightmost point of a_cvx_hull
    a_lower_right = len(a_cvx_hull) - 1

    # leftmost point of b_cvx_hull
    b_lower_left = 0

    # print('acvxhull________________')
    # print(f'{type(a_cvx_hull[a_lower_right])} ==== {a_cvx_hull[a_lower_right]}')

    line_T = Line( a_cvx_hull[a_lower_right], b_cvx_hull[b_lower_left] )
    a_lower_bool = False
    b_lower_bool = False

    # lower tangent | line_T.is_lower_tangent2(a_cvx_hull, b_cvx_hull):
    while not line_T.is_lower_tangent(a_cvx_hull) and not line_T.is_lower_tangent(b_cvx_hull):
        while not line_T.is_lower_tangent(a_cvx_hull):
            # a_cvx_hull.remove(a_lower_right)
            not_lower_tangent.append(a_cvx_hull.pop(a_lower_right))
            a_lower_right -= 1  # step in clockwise direction

            if len(a_cvx_hull) == 0:
                break

            # loop around to end of the list (avoid out of bounds error)
            if a_lower_right < 0:
                a_lower_right = len(a_cvx_hull) - 1

            line_T = Line(a_cvx_hull[a_lower_right], b_cvx_hull[b_lower_left])


        while not line_T.is_lower_tangent(b_cvx_hull):
            # b_cvx_hull.remove(b_lower_left)
            not_lower_tangent.append(b_cvx_hull.pop(b_lower_left))
            b_lower_left += 1  # step in counter-clockwise direction

            if len(b_cvx_hull) == 0:
                break

            # loop around to start of the list (avoid out of bounds error)
            if b_lower_left >= len(b_cvx_hull):
                b_lower_left = 0

            line_T = Line(a_cvx_hull[a_lower_right], b_cvx_hull[b_lower_left])


    # upper tangent     # TODO: finish compute upper tan
    not_upper_tangent = []

    a_upper_right = len(cpy_a_cvx_hull) - 1     # rightmost point of cpy_a_cvx_hull
    b_upper_left = 0      # leftmost point of cpy_b_cvx_hull

    line_T = Line(cpy_a_cvx_hull[a_upper_right], cpy_b_cvx_hull[b_upper_left])
    a_upper_bool = False
    b_upper_bool = False

    # line_T.is_upper_tangent2(cpy_a_cvx_hull, cpy_b_cvx_hull):
    while not line_T.is_upper_tangent(cpy_a_cvx_hull) and not line_T.is_upper_tangent(cpy_b_cvx_hull):
        while not line_T.is_upper_tangent(cpy_a_cvx_hull):
            # cpy_a_cvx_hull.remove(a_upper_right)
            not_upper_tangent.append(cpy_a_cvx_hull.pop(a_upper_right))
            a_upper_right += 1  # step in counter-clockwise direction

            if len(cpy_a_cvx_hull) == 0:
                break

            # loop around to start of the list (avoid out of bounds error)
            if a_upper_right >= len(cpy_a_cvx_hull):
                a_upper_right = 0

            line_T = Line(cpy_a_cvx_hull[a_upper_right], cpy_b_cvx_hull[b_upper_left])


        while not line_T.is_upper_tangent(cpy_b_cvx_hull):
            # cpy_b_cvx_hull.remove(b_upper_left)
            not_upper_tangent.append(cpy_b_cvx_hull.pop(b_upper_left))
            b_upper_left -= 1         # step in clockwise direction

            if len(cpy_b_cvx_hull) == 0:
                break

            # loop around to end of the list (avoid out of bounds error)
            if b_upper_left < 0:
                b_upper_left = len(cpy_b_cvx_hull) - 1

            line_T = Line(cpy_a_cvx_hull[a_upper_right], cpy_b_cvx_hull[b_upper_left])


        # y += 10
        # print(y)

    # combine
    #
    # [ b_upper , a_upper , .. , .. , a_lower , b_lower , .. , .. ]

    i = 0
    for p in range(0, len(not_lower_tangent)):
        if not_lower_tangent[p] in cpy_a_cvx_hull and not ( not_lower_tangent[p].idx == cpy_a_cvx_hull[a_upper_right] or not_lower_tangent[p].idx == cpy_b_cvx_hull[b_upper_left] ):
            cpy_a_cvx_hull.pop(p)

        if not_lower_tangent[p] in cpy_b_cvx_hull and not ( not_lower_tangent[p].idx == cpy_b_cvx_hull[a_upper_right] or not_lower_tangent[p].idx == cpy_b_cvx_hull[b_upper_left] ):
            cpy_b_cvx_hull.pop(p)

    for p in range(0, len(not_upper_tangent)):
        if not_upper_tangent[p] in a_cvx_hull and not ( not_upper_tangent[p].idx == a_cvx_hull[a_lower_right] or not_upper_tangent[p].idx == b_cvx_hull[b_lower_left] ):
            a_cvx_hull.pop(p)

        if not_upper_tangent[p] in b_cvx_hull and not (not_upper_tangent[p].idx == a_cvx_hull[a_lower_right] or not_upper_tangent[p].idx == b_cvx_hull[b_lower_left]):
            b_cvx_hull.pop(p)

    return a_cvx_hull + b_cvx_hull

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
        points.append(Point( float(coordinates[0]), float(coordinates[1]), int(i) ))
        line = file.readline()
        i += 1

    file.close()

    # compute convex hull points
    cvx_hull_points = compute_convex_hull(points)

    print(cvx_hull_points)

    for p in cvx_hull_points:
        print(p.idx)

    # for p in cvx_hull_points:
    #     print(p)

    # # debugging: print all points
    # for i in points:
    #     print(f'{i.x} {i.y}')
    #
    # # print function of line between two points
    # z = Line(points[0], points[34])


main()
