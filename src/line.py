#from point import Point

class Line:
    # Point(a): first point of line
    # Point(b): second point of line
    def __init__(self, a, b):
        print(f'Line __init__ b = {type(b)}')
        # y = mx + b
        # b = y - mx
        self.point_a = a
        self.point_b = b
        self.slope = (a.y_coord - b.y_coord) / (a.x_coord - b.x_coord)
        self.y_intercept = a.y_coord - (self.slope * a.x_coord)
        # print(f'y = {self.slope}x + {self.y_intercept}')

    def is_lower_tangent(self, points):
        for p in points:
            if not p.is_above_line(self):
                return False

        return True

    def is_upper_tangent(self, points):
        for p in points:
            if p.is_above_line(self):
                return False

        return True

    # def is_lower_tangent2(self, a_points, b_points):
    #     i = 0
    #
    #     # If number of points is not equal, then there
    #     # can only be a difference of 1 between them.
    #     if len(a_points) > len(b_points):
    #         for i in range(0, len(b_points)):
    #             if not ( a_points[i].is_above_line(self) or b_points[i].is_above_line(self) ):
    #                 return False
    #         if not a_points[i+1].is_above_line(self):
    #             return False
    #
    #     elif len(a_points) < len(b_points):
    #         for i in range(0, len(a_points)):
    #             if not ( a_points[i].is_above_line(self) or b_points[i].is_above_line(self) ):
    #                 return False
    #         if not b_points[i+1].is_above_line(self):
    #             return False
    #
    #     else:
    #         for i in range(0, len(a_points)):
    #             if not (a_points[i].is_above_line(self) or b_points[i].is_above_line(self)):
    #                 return False
    #
    #     return True



    def is_upper_tangent2(self, a_points, b_points):
        i = 0

        # If number of points is not equal, then there
        # can only be a difference of 1 between them.
        if len(a_points) > len(b_points):
            for i in range(0, len(b_points)):
                if a_points[i].is_above_line(self) or b_points[i].is_above_line(self):
                    return False
            if i == 0:
                return a_points[i].is_above_line(self)
            else:
                return a_points[i + 1].is_above_line(self)

        elif len(a_points) < len(b_points):
            for i in range(0, len(a_points)):
                if a_points[i].is_above_line(self) or b_points[i].is_above_line(self):
                    return False
            # if i == 0:
            #     return b_points[i].is_above_line(self)
            else:
                return b_points[i + 1].is_above_line(self)

        else:
            for i in range(0, len(a_points)):
                if a_points[i].is_above_line(self) or b_points[i].is_above_line(self):
                    return False

        return True
