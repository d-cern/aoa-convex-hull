from Point import Point

class Line:
    def __init__(self, a: Point, b: Point):
        # y = mx + b
        # b = y - mx
        self.pointA = a
        self.pointB = b
        self.slope = (a.y - b.y) / (a.x - b.x)
        self.y_intercept = a.y - (self.slope * a.x)
        # print(f'y = {self.slope}x + {self.y_intercept}')

    def IsLowerTangent(self, point):
        return point.IsAboveLine(self)

    def IsLowerTangent2(self, pointsA, pointsB):
        i = 0

        # If number of points is not equal, then there
        # can only be a difference of 1 between them.
        if len(pointsA) > len(pointsB):
            for i in range(0, len(pointsB)):
                if not ( pointsA[i].isAboveLine(self) and pointsB[i].IsAboveLine(self) ):
                    return False
            if pointsA[i+1].IsAboveLine(self):
                return False

        elif len(pointsA) < len(pointsB):
            for i in range(0, len(pointsA)):
                if not ( pointsA[i].isAboveLine(self) or pointsB[i].IsAboveLine(self) ):
                    return False
            if pointsB[i+1].IsAboveLine(self):
                return False

        else:
            for i in range(0, len(pointsA)):
                if not (pointsA[i].isAboveLine(self) or pointsB[i].IsAboveLine(self)):
                    return False

        return True
