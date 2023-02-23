# from line import Line

# x:    x-coordinate
# y:    y-coordinate
# idx:  index of Point in input file
class Point:
    def __init__(self, x: float, y: float, idx: int):
        self.x = float(x)
        self.y = float(y)
        self.idx = int(idx)

    def is_above_line(self, l):
        y_line = (l.slope * self.x) + l.y_intercept

        return bool(self.y > y_line)
