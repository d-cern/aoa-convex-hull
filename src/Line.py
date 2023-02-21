from Point import Point

class Line:
    def __init__(self, a: Point, b: Point):
        # y = mx + b
        # b = y - mx
        self.pointA = a
        self.pointB = b
        self.slope = (a.y - b.y) / (a.x - b.x)
        self.y_intercept = a.y - (self.slope * a.x)
