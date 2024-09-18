print("Welcome to Line Comparison Computation Program on Master Branch")

import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2

    #UC 1
    def length(self):
        return math.sqrt((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2)

if __name__ == "__main__":
    point1 = Point(1, 2)
    point2 = Point(4, 6)
    line = Line(point1, point2)
    print(f"Length of the line: {line.length()}")