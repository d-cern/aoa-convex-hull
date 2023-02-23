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

    def is_lower_tangent(self, point):
        return point.is_above_line(self)

    def is_lower_tangent2(self, points_a, points_b):
        i = 0

        # If number of points is not equal, then there
        # can only be a difference of 1 between them.
        if len(points_a) > len(points_b):
            for i in range(0, len(points_b)):
                if not ( points_a[i].is_above_line(self) and points_b[i].is_above_line(self) ):
                    return False
            if points_a[i+1].is_above_line(self):
                return False

        elif len(points_a) < len(points_b):
            for i in range(0, len(points_a)):
                if not ( points_a[i].is_above_line(self) or points_b[i].is_above_line(self) ):
                    return False
            if points_b[i+1].is_above_line(self):
                return False

        else:
            for i in range(0, len(points_a)):
                if not (points_a[i].is_above_line(self) or points_b[i].is_above_line(self)):
                    return False

        return True
