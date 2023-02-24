# from point import Point

class Line:
    # Point(a): first point of line
    # Point(b): second point of line
    def __init__(self, a, b):
        # y = mx + b
        # b = y - mx
        self.pointA = a
        self.pointB = b
        self.slope = (a.y - b.y) / (a.x - b.x)
        self.y_intercept = a.y - (self.slope * a.x)
        # print(f'y = {self.slope}x + {self.y_intercept}')

    def is_lower_tangent(self, points):
        for p in points:
            if not p.is_above_line(self):
                return False

        return True

    def is_lower_tangent2(self, a_points, b_points):
        i = 0

        # If number of points is not equal, then there
        # can only be a difference of 1 between them.
        if len(a_points) > len(b_points):
            for i in range(0, len(b_points)):
                if not ( a_points[i].is_above_line(self) and b_points[i].is_above_line(self) ):
                    return False
            if a_points[i+1].is_above_line(self):
                return False

        elif len(a_points) < len(b_points):
            for i in range(0, len(a_points)):
                if not ( a_points[i].is_above_line(self) or b_points[i].is_above_line(self) ):
                    return False
            if b_points[i+1].is_above_line(self):
                return False

        else:
            for i in range(0, len(a_points)):
                if not (a_points[i].is_above_line(self) or b_points[i].is_above_line(self)):
                    return False

        return True

    def is_upper_tangent(self, points):
        return True         # TODO: implement

    def is_upper_tangent2(self, a_points, b_points):
        return True         # TODO: implement
