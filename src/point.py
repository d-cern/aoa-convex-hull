from Line import Line

class Point:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def IsAboveLine(self, l: Line):
        yLine = (l.slope * self.x) + l.y_intercept

        return bool(self.y > yLine)
